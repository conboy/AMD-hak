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
    imageUrl: 'https://cdn11.bigcommerce.com/s-dlgvmcszyl/images/stencil/338x338/products/170/548/1397924_AMD_TWA_T-Shirt_front__01068.1654812387.png?c=1',
  },
  {
    id: 2,
    name: 'AMD Hoodie',
    points: 1000,
    imageUrl: 'https://cdn11.bigcommerce.com/s-dlgvmcszyl/images/stencil/558x558/products/189/599/AMD_Brand_CustomHoodie__44995.1683927734.jpg?c=1',
  },
  {
    id: 3,
    name: 'AMD Hat',
    points: 300,
    imageUrl: 'https://cdn11.bigcommerce.com/s-dlgvmcszyl/images/stencil/558x558/products/203/643/AMD-1033_BlackCap_front__15561.1706566899.1280.1280__23234.1706825517.jpg?c=1',
  },
  {
    id: 4,
    name: 'AMD Mug',
    points: 200,
    imageUrl: 'https://cdn11.bigcommerce.com/s-dlgvmcszyl/images/stencil/558x558/products/217/688/AMD_AsobuExplorer_Black__26894.1707412382.jpg?c=1',
  },
  {
    id: 5,
    name: 'AMD Mousepad',
    points: 150,
    imageUrl: 'https://cdn11.bigcommerce.com/s-dlgvmcszyl/images/stencil/558x558/products/141/459/MousePad__24992.1604431144.jpg?c=1',
  },
  {
    id: 6,
    name: 'AMD Sticker Pack',
    points: 100,
    imageUrl: 'https://cdn11.bigcommerce.com/s-dlgvmcszyl/images/stencil/558x558/products/227/714/AMD_FanStore_VinylStickers__77506.1714073219.png?c=1',
  },
  {
    id: 7,
    name: 'AMD Backpack',
    points: 1200,
    imageUrl: 'https://cdn11.bigcommerce.com/s-dlgvmcszyl/images/stencil/558x558/products/209/702/AMD_backpack_3__94990.1712263720.jpg?c=1',
  },
  {
    id: 8,
    name: 'AMD Water Bottle',
    points: 250,
    imageUrl: 'https://cdn11.bigcommerce.com/s-dlgvmcszyl/images/stencil/338x338/products/215/680/AMD_AsobuCanyon_Black__12464.1707410724.jpg?c=1',
  },
  {
    id: 9,
    name: 'AMD Fanny Pack',
    points: 50,
    imageUrl: 'https://cdn11.bigcommerce.com/s-dlgvmcszyl/images/stencil/558x558/products/192/605/Osprey_HipPack_AMD__61224.1686854952.png?c=1',
  },
  {
    id: 10,
    name: 'AMD Carhartt Shirt',
    points: 400,
    imageUrl: 'https://cdn11.bigcommerce.com/s-dlgvmcszyl/images/stencil/558x558/products/213/670/AMD_CarharttShirt_1__70394.1707246443.jpg?c=1',
  },
  {
    id: 11,
    name: 'AMD Fullzip',
    points: 300,
    imageUrl: 'https://cdn11.bigcommerce.com/s-dlgvmcszyl/images/stencil/558x558/products/180/569/eddie-bauer-full-zip-mens__77011.1665671111.png?c=1',
  },
  {
    id: 12,
    name: 'AMD Socks',
    points: 200,
    imageUrl: 'https://cdn11.bigcommerce.com/s-dlgvmcszyl/images/stencil/338x338/products/173/554/AMD-Socks__34541.1660324908.png?c=1',
  },
  {
    id: 13,
    name: 'AMD Pride Shirt',
    points: 250,
    imageUrl: 'https://cdn11.bigcommerce.com/s-dlgvmcszyl/images/stencil/338x338/products/148/477/pride-front__67496.1607373314.jpg?c=1',
  },
  {
    id: 14,
    name: 'AMD Pride Sunglasses',
    points: 100,
    imageUrl: 'https://cdn11.bigcommerce.com/s-dlgvmcszyl/images/stencil/338x338/products/193/609/AMD_Sunglasses_2__76671.1691688577.jpg?c=1',
  },
  {
    id: 15,
    name: 'AMD Dog Tags',
    points: 800,
    imageUrl: 'https://cdn11.bigcommerce.com/s-dlgvmcszyl/images/stencil/338x338/products/164/522/TYP4812PO-BB19835-PPS__06757.1647973051.JPG?c=1',
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
