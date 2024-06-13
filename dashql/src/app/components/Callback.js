import { useEffect } from 'react';
import { useRouter } from 'next/router';
import supabase from '../lib/supabaseClient';

const Callback = () => {
  const router = useRouter();

  useEffect(() => {
    const hash = window.location.hash;
    const params = new URLSearchParams(hash.replace('#', ''));
    const access_token = params.get('access_token');
    const refresh_token = params.get('refresh_token');

    if (access_token && refresh_token) {
      supabase.auth.setSession({
        access_token,
        refresh_token
      }).then(({ error }) => {
        if (error) {
          console.error('Error setting session:', error);
        } else {
          router.push('/'); // Redirect to the home page or any other page
        }
      });
    }
  }, [router]);

  return (
    <div className="flex items-center justify-center min-h-screen">
      <span className="loading loading-infinity loading-lg"></span>
    </div>
  );
};

export default Callback;