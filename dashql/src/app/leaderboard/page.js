// src/pages/leaderboard.js
"use client";
import React from 'react';
import Navbar from '../components/Navbar';
import useAuth from '../lib/useAuth';

// Placeholder data
const leaderboardData = [
  {
    id: 1,
    name: 'Conrad',
    coins: 1500,
    level: 10,
    achievements: ['Bug Buster', 'Security Sentry'],
    avatarUrl: 'https://via.placeholder.com/150',
  },
  {
    id: 2,
    name: 'Ian',
    coins: 1200,
    level: 8,
    achievements: ['Code Guardian', 'Speedy Solver'],
    avatarUrl: 'https://via.placeholder.com/150',
  },
  {
    id: 3,
    name: 'Luka',
    coins: 900,
    level: 7,
    achievements: ['The Fixer', 'Ultimate Debugger'],
    avatarUrl: 'https://via.placeholder.com/150',
  },
  {
    id: 3,
    name: 'Vivek',
    coins: 900,
    level: 7,
    achievements: ['Patch Master', 'Firewall Fortifier'],
    avatarUrl: 'https://via.placeholder.com/150',
  },
  {
    id: 3,
    name: 'Charlie',
    coins: 900,
    level: 7,
    achievements: ['Data Defender', 'Patch Prodigy'],
    avatarUrl: 'https://via.placeholder.com/150',
  },
  // Add more users as needed
];

const Leaderboard = () => {
  const { user, loading } = useAuth();

  if (loading) {
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
      <div className="max-w-6xl mx-auto pt-">
          <div className="text-center mb-8">
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
                  <th>Level</th>
                  <th>Coins</th>
                  <th>Achievements</th>
                </tr>
              </thead>
              <tbody>
                {leaderboardData.map((user, index) => (
                  <tr key={user.id}>
                    <td>
                      {index + 1 === 1 && '🥇'}
                      {index + 1 === 2 && '🥈'}
                      {index + 1 === 3 && '🥉'}
                      {index + 1 > 3 && index + 1}
                    </td>
                    <td>
                      <div className="avatar">
                        <div className="w-12 rounded-full ring ring-primary ring-offset-base-100 ring-offset-2">
                          <img src={user.avatarUrl} alt={user.name} />
                        </div>
                      </div>
                    </td>
                    <td>{user.name}</td>
                    <td>{user.level}</td>
                    <td>{user.coins}</td>
                    <td>
                      <ul className="list-disc pl-5 space-y-1">
                        {user.achievements.map((achievement, i) => (
                          <li key={i}>{achievement}</li>
                        ))}
                      </ul>
                    </td>
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
