"use client"
import React, { useEffect, useState } from 'react';
import Navbar from './components/Navbar';
import useAuth from './lib/useAuth';
import supabase from './lib/supabaseClient';

const Home = () => {
  const { user, loading } = useAuth();
  const [tickets, setTickets] = useState([]);
  const [loadingTickets, setLoadingTickets] = useState(true);

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

  console.log(user);

  return (
    <>
      <Navbar user={user} />
      {/* Main content */}
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
                <tr key={ticket.id}>
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
                        onClick={() => assignToUser(ticket.id)}
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
      </main>
    </>
  );
};

export default Home;
