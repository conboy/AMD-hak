import { useEffect, useState } from 'react';
import supabase from './supabaseClient';

const useAuth = () => {
    const [user, setUser] = useState(null);
    const [loading, setLoading] = useState(true);
    const [profile, setProfile] = useState(null);
  
    useEffect(() => {
      const checkSession = async () => {
        const { data: { session }, error } = await supabase.auth.getSession();
        if (error) console.error('Error getting session:', error);
        setUser(session?.user ?? null);
        setLoading(false);
  
        if (session) {
          const { user } = session;
          const { data: githubProfile, error } = await supabase.from('profiles').select('*').eq('id', user.id).single();
          if (error) {
            console.error('Error fetching GitHub profile:', error);
          } else {
            setProfile(githubProfile);
          }
        } else {
          await supabase.auth.signInWithOAuth({
            provider: 'github',
            options: {
              redirectTo: `${window.location.origin}/callback`, // Redirect to the callback page
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
  
    return { user, loading, profile };
  };
  
  export default useAuth;