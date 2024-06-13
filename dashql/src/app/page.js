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
              <h3 className="font-bold text-lg">Ticket Details</h3>
              <div className="py-4">
                <p><strong>Rule ID:</strong> {selectedTicket.ruleId || 'N/A'}</p>
                <p><strong>Message Text:</strong> {selectedTicket.message_text || 'N/A'}</p>
                <p><strong>Description:</strong> {selectedTicket.fullDescription || 'N/A'}</p>
                <p>
                  <strong>GitHub Link:</strong>{' '}
                  <a href={generateGitHubLink(selectedTicket.uri, selectedTicket.startLine, selectedTicket.endLine)} target="_blank" rel="noopener noreferrer">
                    {generateGitHubLink(selectedTicket.uri, selectedTicket.startLine, selectedTicket.endLine)}
                  </a>
                </p>
                <p><strong>URI:</strong> {selectedTicket.uri || 'N/A'}</p>
                <p><strong>Start Line:</strong> {selectedTicket.startLine || 'N/A'}</p>
                <p><strong>Start Column:</strong> {selectedTicket.startColumn || 'N/A'}</p>
                <p><strong>End Line:</strong> {selectedTicket.endLine || 'N/A'}</p>
                <p><strong>End Column:</strong> {selectedTicket.endColumn || 'N/A'}</p>
                <p><strong>Level:</strong> {selectedTicket.level || 'N/A'}</p>
                <p><strong>Tags:</strong> {selectedTicket.tags || 'N/A'}</p>
                <p><strong>Kind:</strong> {selectedTicket.kind || 'N/A'}</p>
                <p><strong>Precision:</strong> {selectedTicket.precision || 'N/A'}</p>
                <p><strong>Problem Severity:</strong> {selectedTicket.problem?.severity || 'N/A'}</p>
                <p><strong>Security Severity:</strong> {selectedTicket['security-severity'] || 'N/A'}</p>
                <p><strong>Sub-severity:</strong> {selectedTicket['sub-severity'] || 'N/A'}</p>
              </div>
              <div className="modal-action">
                <button className="btn btn-primary" onClick={closeModal}>Close</button>
              </div>
            </div>
          </div>
        )}
      </main>
    </>
  );
};

export default Home;
