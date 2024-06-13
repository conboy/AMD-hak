"use client"
import React, { useEffect, useState } from 'react';
import Navbar from './components/Navbar';
import useAuth from './lib/useAuth';
import supabase from './lib/supabaseClient';
import 'daisyui/dist/full.css';

const Home = () => {
  const { user, loading } = useAuth();
  const [tickets, setTickets] = useState([]);
  const [loadingTickets, setLoadingTickets] = useState(true);
  const [selectedTicket, setSelectedTicket] = useState(null);
  const [modalVisible, setModalVisible] = useState(false);

  useEffect(() => {
    if (user) {
      const fetchTickets = async () => {
        const { data, error } = await supabase.from('tickets').select('*');
        if (error) {
          console.error('Error fetching tickets:', error);
        } else {
          setTickets(data);
        }
        setLoadingTickets(false);
      };

      fetchTickets();
    }
  }, [user]);

  const assignToUser = async (ticketId) => {
    if (user && user.user_metadata && user.user_metadata.user_name) {
      const { user_name } = user.user_metadata;
      const { data, error } = await supabase
        .from('tickets')
        .update({ assigned_to: user_name })
        .eq('id', ticketId);

      if (error) {
        console.error('Error updating ticket:', error);
      } else {
        setTickets(prevTickets => 
          prevTickets.map(ticket => 
            ticket.id === ticketId ? { ...ticket, assigned_to: user_name } : ticket
          )
        );
      }
    }
  };

  const getStatusClass = (status) => {
    switch (status) {
      case 'False Positive':
        return 'badge-md badge-warning';
      case 'Fixed':
        return 'badge-md badge-error';
      case 'Open':
      default:
        return 'badge-md badge-success';
    }
  };

  const handleRowClick = async (ticketId) => {
    const { data, error } = await supabase.from('tickets').select('*').eq('id', ticketId).single();
    if (error) {
      console.error('Error fetching ticket details:', error);
    } else {
      setSelectedTicket(data);
      setModalVisible(true);
    }
  };

  const closeModal = () => {
    setModalVisible(false);
    setSelectedTicket(null);
  };

  const generateGitHubLink = (uri, startLine, endLine) => {
    if (!uri || !startLine) return 'N/A';
    const repoUrl = 'https://github.com/tensorflow/tensorflow/blob/master/'
    const baseUrl = uri.split('#')[0];
    return `${repoUrl}${baseUrl}#L${startLine}${endLine && endLine !== 'N/A' ? `-L${endLine}` : ''}`;
  };

  const updatePointsAndStatus = async (status) => {
    if (!user || !selectedTicket) return;
    const { user_name } = user.user_metadata;
    const { security_severity } = selectedTicket;

    // Fetch the existing user points record
    let { data: pointsData, error: pointsError } = await supabase
      .from('points')
      .select('*')
      .eq('user_name', user_name)
      .single();

    if (pointsError && pointsError.code !== 'PGRST116') {
      console.error('Error fetching points:', pointsError);
      return;
    }

    // If no record exists, create a new one
    if (!pointsData) {
      const { data, error } = await supabase
        .from('points')
        .insert([{ user_name, points: security_severity, number_solved: 1 }]);
      if (error) {
        console.error('Error inserting points:', error);
        return;
      }
    } else {
      // Update the existing record
      const { data, error } = await supabase
        .from('points')
        .update({
          points: pointsData.points + security_severity,
          number_solved: pointsData.number_solved + 1
        })
        .eq('user_name', user_name);
      if (error) {
        console.error('Error updating points:', error);
        return;
      }
    }

    // Update the ticket status
    const { data: ticketData, error: ticketError } = await supabase
      .from('tickets')
      .update({ status })
      .eq('id', selectedTicket.id);

    if (ticketError) {
      console.error('Error updating ticket status:', ticketError);
      return;
    }

    // Update the local state
    setTickets(prevTickets =>
      prevTickets.map(ticket =>
        ticket.id === selectedTicket.id ? { ...ticket, status } : ticket
      )
    );
    closeModal();
  };

  if (loading || loadingTickets) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <span className="loading loading-infinity loading-lg"></span>
      </div>
    );
  }

  if (!user) {
    return <div>Redirecting to GitHub login...</div>;
  }

  return (
    <>
      <Navbar user={user} />
      <main>
        <div className="overflow-x-auto">
          <table className="table">
            <thead>
              <tr>
                <th>🎫</th>
                <th>Bounty</th>
                <th>Status</th>
                <th>Rule ID</th>
                <th>Description</th>
                <th>Assigned to</th>
              </tr>
            </thead>
            <tbody>
              {tickets.map(ticket => (
                <tr key={ticket.id} onClick={() => handleRowClick(ticket.id)}>
                  <td>{ticket.id}</td>
                  <td>{ticket.security_severity} 🪙</td>
                  <td><span className={getStatusClass(ticket.status)}>{ticket.status}</span></td>
                  <td>{ticket.ruleId}</td>
                  <td>{ticket.message_text}</td>
                  <td>
                    {ticket.assigned_to ? (
                      ticket.assigned_to
                    ) : (
                      <button 
                        className="btn btn-xs btn-primary"
                        onClick={(e) => {
                          e.stopPropagation();
                          assignToUser(ticket.id);
                        }}
                      >
                        Assign Me
                      </button>
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        {modalVisible && selectedTicket && (
          <div className="modal modal-open">
            <div className="modal-box w-11/12 max-w-5xl">
              <h3 className="font-bold text-lg">Ticket #{selectedTicket.id}</h3>
              <h3 className="font-bold text-lg pt-2">🪙 {selectedTicket.security_severity}</h3>
              <div className="py-4">
                <p><strong>Rule ID:</strong> {selectedTicket.ruleId || 'N/A'}</p>
                <p><strong>Message Text:</strong> {selectedTicket.message_text || 'N/A'}</p>
                <p><strong>Description:</strong> {selectedTicket.fullDescription || 'N/A'}</p>
                <p><strong>Level:</strong> {selectedTicket.level || 'N/A'}</p>
                <p><strong>Tags:</strong> {selectedTicket.tags || 'N/A'}</p>
                <p><strong>Kind:</strong> {selectedTicket.kind || 'N/A'}</p>
                <p><strong>Precision:</strong> {selectedTicket.precision || 'N/A'}</p>
                <p><strong>Problem Severity:</strong> {selectedTicket.problem_severity || 'N/A'}</p>
                <p><strong>Security Severity:</strong> {selectedTicket.security_severity || 'N/A'}</p>
                <p><strong>Sub-severity:</strong> {selectedTicket.sub_severity || 'N/A'}</p>
              </div>
              <div className="flex justify-center space-x-4">
                <a href={generateGitHubLink(selectedTicket.uri, selectedTicket.startLine, selectedTicket.endLine)} target="_blank" rel="noopener noreferrer">
                  <button className="btn btn-neutral">Github Link</button>
                </a>
                <button className="btn btn-error" onClick={() => updatePointsAndStatus('False Positive')}>False Positive ❌</button>
                <button className="btn btn-success" onClick={() => updatePointsAndStatus('Fixed')}>Fixed ✅</button>
                <button className="btn btn-square" onClick={closeModal}>
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M6 18L18 6M6 6l12 12" /></svg>
                </button>
              </div>
            </div>
          </div>
        )}
      </main>
    </>
  );
};

export default Home;
