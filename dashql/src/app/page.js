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

  console.log(user)

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
                  <td>{ticket.assigned_to ? ticket.assigned_to : <button className="btn btn-sm btn-primary">Assign Me</button>}</td>
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
