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
                <th>Ticket #</th>
                <th>Name</th>
              </tr>
            </thead>
            <tbody>
              {tickets.map(ticket => (
                <tr key={ticket.id}>
                  <td>{ticket.id}</td>
                  <td>{ticket.name}</td>
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
