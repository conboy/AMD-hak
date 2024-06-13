"use client";
import React from 'react';
import Navbar from '../components/Navbar';
import useAuth from '../lib/useAuth';

const Profile = () => {
  const { user, loading } = useAuth();

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <span className="loading loading-infinity loading-lg"></span>
      </div>
    );
  }

  if (!user) {
    return <div>Redirecting to GitHub login...</div>;
  }

  // Placeholder for gamified data
  const points = 1250;
  const level = 5;
  const xp = 75; // Current XP percentage towards the next level
  const achievements = [
    { title: 'Bug Buster', description: 'Fixed 100 bugs' },
    { title: 'Security Sentry', description: 'Resolved 50 security vulnerabilities' },
    { title: 'Code Guardian', description: 'Achieved 100% test coverage' },
  ];
  const recentActivities = [
    { activity: 'Fixed a SQL injection vulnerability', date: '2024-06-10' },
    { activity: 'Resolved a XSS vulnerability', date: '2024-06-09' },
    { activity: 'Patched a buffer overflow issue', date: '2024-06-08' },
  ];

  return (
    <>
      <Navbar user={user} />
      <main className="p-8">
        <div className="max-w-4xl mx-auto">
          <div className="card bg-base-200 shadow-xl p-8 mb-8">
            <div className="flex items-center space-x-4">
              <div className="avatar">
                <div className="w-24 rounded-full ring ring-primary ring-offset-base-100 ring-offset-2">
                  <img src={user.user_metadata.avatar_url} alt="GitHub Avatar" />
                </div>
              </div>
              <div>
                <h1 className="text-3xl font-bold">{user.user_metadata.full_name}</h1>
                <p className="text-lg text-gray-500">@{user.user_metadata.preferred_username}</p>
              </div>
            </div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="card bg-base-200 shadow-xl p-8">
              <h2 className="text-2xl font-bold mb-4">Gamification</h2>
              <div className="stats stats-vertical md:stats-horizontal shadow">
                <div className="stat">
                  <div className="stat-title">Points</div>
                  <div className="stat-value">{points}</div>
                </div>
                <div className="stat">
                  <div className="stat-title">Level</div>
                  <div className="stat-value">{level}</div>
                </div>
              </div>
              <div className="mt-4">
                <h3 className="text-lg font-bold">XP Progress</h3>
                <div className="relative pt-1">
                  <div className="overflow-hidden h-4 mb-4 text-xs flex rounded bg-gray-200">
                    <div
                      style={{ width: `${xp}%` }}
                      className="shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-green-500"
                    ></div>
                  </div>
                  <p className="text-center">{xp}% to next level</p>
                </div>
              </div>
            </div>

            <div className="card bg-base-200 shadow-xl p-8">
              <h2 className="text-2xl font-bold mb-4">Achievements</h2>
              <ul className="list-disc pl-5 space-y-2">
                {achievements.map((achievement, index) => (
                  <li key={index}>
                    <span className="font-semibold">{achievement.title}:</span> {achievement.description}
                  </li>
                ))}
              </ul>
            </div>

            <div className="card bg-base-200 shadow-xl p-8 md:col-span-2">
              <h2 className="text-2xl font-bold mb-4">Recent Activities</h2>
              <ul className="list-disc pl-5 space-y-2">
                {recentActivities.map((activity, index) => (
                  <li key={index}>
                    <span className="font-semibold">{activity.activity}</span> - <span className="text-gray-500">{activity.date}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      </main>
    </>
  );
};  

export default Profile;
