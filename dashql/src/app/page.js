"use client"
import React from 'react';
import Navbar from './components/Navbar';
import useAuth from './lib/useAuth';

const Home = () => {
  const { user, loading } = useAuth();

  if (loading) {
    return <div>Loading...</div>; // You can replace this with a loader/spinner
  }

  if (!user) {
    return <div>Redirecting to GitHub login...</div>;
  }

  return (
    <>
      <Navbar />
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
              {/* Replace with your dynamic data */}
              <tr>
                <td>1</td>
                <td>Sample Issue</td>
              </tr>
            </tbody>
          </table>
        </div>
      </main>
    </>
  );
};

export default Home;
