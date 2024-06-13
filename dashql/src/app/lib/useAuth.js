import { useEffect, useState } from 'react';
import supabase from './supabaseClient';

const useAuth = () => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const checkSession = async () => {
      const { data: { session }, error } = await supabase.auth.getSession();
      if (error) console.error('Error getting session:', error);
      setUser(session?.user ?? null);
      setLoading(false);

      if (!session) {
        await supabase.auth.signInWithOAuth({
          provider: 'github',
          options: {
            scopes: 'repo gist notifications',
          },
        });
      }
    };

    checkSession();

    const { data: authListener } = supabase.auth.onAuthStateChange((_event, session) => {
      setUser(session?.user ?? null);
      setLoading(false);
    });

    return () => {
      authListener?.unsubscribe && authListener.unsubscribe();
    };
  }, []);

  return { user, loading };
};

export default useAuth;