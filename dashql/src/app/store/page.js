// src/pages/store.js
"use client";
import React from 'react';
import Navbar from '../components/Navbar';
import useAuth from '../lib/useAuth';

// Placeholder data for store items
const storeItems = [
  {
    id: 1,
    name: 'AMD T-Shirt',
    points: 500,
    imageUrl: 'https://amdfanstore.com/wp-content/uploads/2021/01/amd-shirt-01-800x800.jpg',
  },
  {
    id: 2,
    name: 'AMD Hoodie',
    points: 1000,
    imageUrl: 'https://amdfanstore.com/wp-content/uploads/2021/01/amd-hoodie-01-800x800.jpg',
  },
  {
    id: 3,
    name: 'AMD Hat',
    points: 300,
    imageUrl: 'https://amdfanstore.com/wp-content/uploads/2021/01/amd-hat-01-800x800.jpg',
  },
  {
    id: 4,
    name: 'AMD Mug',
    points: 200,
    imageUrl: 'https://amdfanstore.com/wp-content/uploads/2021/01/amd-mug-01-800x800.jpg',
  },
  {
    id: 5,
    name: 'AMD Mousepad',
    points: 150,
    imageUrl: 'https://amdfanstore.com/wp-content/uploads/2021/01/amd-mousepad-01-800x800.jpg',
  },
  {
    id: 6,
    name: 'AMD Sticker Pack',
    points: 100,
    imageUrl: 'https://amdfanstore.com/wp-content/uploads/2021/01/amd-sticker-pack-01-800x800.jpg',
  },
  {
    id: 7,
    name: 'AMD Backpack',
    points: 1200,
    imageUrl: 'https://amdfanstore.com/wp-content/uploads/2021/01/amd-backpack-01-800x800.jpg',
  },
  {
    id: 8,
    name: 'AMD Water Bottle',
    points: 250,
    imageUrl: 'https://amdfanstore.com/wp-content/uploads/2021/01/amd-water-bottle-01-800x800.jpg',
  },
  {
    id: 9,
    name: 'AMD Keychain',
    points: 50,
    imageUrl: 'https://amdfanstore.com/wp-content/uploads/2021/01/amd-keychain-01-800x800.jpg',
  },
  {
    id: 10,
    name: 'AMD Phone Case',
    points: 400,
    imageUrl: 'https://amdfanstore.com/wp-content/uploads/2021/01/amd-phone-case-01-800x800.jpg',
  },
  {
    id: 11,
    name: 'AMD Notebook',
    points: 300,
    imageUrl: 'https://amdfanstore.com/wp-content/uploads/2021/01/amd-notebook-01-800x800.jpg',
  },
  {
    id: 12,
    name: 'AMD Socks',
    points: 200,
    imageUrl: 'https://amdfanstore.com/wp-content/uploads/2021/01/amd-socks-01-800x800.jpg',
  },
  {
    id: 13,
    name: 'AMD Beanie',
    points: 250,
    imageUrl: 'https://amdfanstore.com/wp-content/uploads/2021/01/amd-beanie-01-800x800.jpg',
  },
  {
    id: 14,
    name: 'AMD Pen',
    points: 100,
    imageUrl: 'https://amdfanstore.com/wp-content/uploads/2021/01/amd-pen-01-800x800.jpg',
  },
  {
    id: 15,
    name: 'AMD Mouse',
    points: 800,
    imageUrl: 'https://amdfanstore.com/wp-content/uploads/2021/01/amd-mouse-01-800x800.jpg',
  },
];

const Store = () => {
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

  return (
    <>
      <Navbar user={user} />
      <main className="p-8 bg-base-200 min-h-screen">
        <div className="max-w-6xl mx-auto">
          <div className="text-center mb-8">
            <h1 className="text-4xl font-bold">Store</h1>
            <p className="text-gray-600">Redeem your points for awesome AMD merchandise</p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {storeItems.map((item) => (
              <div key={item.id} className="card bg-base-100 shadow-xl">
                <figure>
                  <img src={item.imageUrl} alt={item.name} className="w-full h-48 object-cover" />
                </figure>
                <div className="card-body">
                  <h2 className="card-title">{item.name}</h2>
                  <p>{item.points} points</p>
                  <div className="card-actions justify-end">
                    <button className="btn btn-primary">Redeem</button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </main>
    </>
  );
};

export default Store;
