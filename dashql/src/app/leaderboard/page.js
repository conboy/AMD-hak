"use client";
import React, { useEffect, useState } from 'react';
import Navbar from '../components/Navbar';
import useAuth from '../lib/useAuth';
import supabase from '../lib/supabaseClient';

const Leaderboard = () => {
  const { user, loading } = useAuth();
  const [leaderboardData, setLeaderboardData] = useState([]);
  const [loadingData, setLoadingData] = useState(true);

  useEffect(() => {
    const fetchLeaderboardData = async () => {
      const { data, error } = await supabase
        .from('points')
        .select('*')
        .order('points', { ascending: false });

      if (error) {
        console.error('Error fetching leaderboard data:', error);
      } else {
        setLeaderboardData(data);
      }
      setLoadingData(false);
    };

    if (user) {
      fetchLeaderboardData();
    }
  }, [user]);

  if (loading || loadingData) {
    return (
      <div className="flex items-center justify-center">
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
        <div className="max-w-6xl mx-auto pt-8">
          <div className="text-center pt-8 mb-8">
            <h1 className="text-4xl font-bold">Leaderboard</h1>
            <p className="text-gray-600">Check out the top contributors and their achievements</p>
          </div>
          <div className="overflow-x-auto">
            <table className="table">
              <thead>
                <tr>
                  <th>Rank</th>
                  <th>Avatar</th>
                  <th>Name</th>
                  <th>Coins</th>
                </tr>
              </thead>
              <tbody>
                {leaderboardData.map((user, index) => (
                  <tr key={user.user_name}>
                    <td>
                      {index + 1 === 1 && '🥇'}
                      {index + 1 === 2 && '🥈'}
                      {index + 1 === 3 && '🥉'}
                      {index + 1 > 3 && index + 1}
                    </td>
                    <td>
                      <div className="avatar">
                        <div className="w-12 rounded-full ring ring-primary ring-offset-base-100 ring-offset-2">
                          <img src={`https://avatars.dicebear.com/api/initials/${user.user_name}.svg`} alt={user.user_name} />
                        </div>
                      </div>
                    </td>
                    <td>{user.user_name}</td>
                    <td>{user.points}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </main>
    </>
  );
};

export default Leaderboard;
