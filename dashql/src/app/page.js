"use client"
import React, { useEffect } from 'react';
import Navbar from "./components/Navbar";
import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://cipubdiqomjtsdayksmf.supabase.co'
const supabaseKey = process.env.SUPABASE_KEY
const supabase = createClient(supabaseUrl, supabaseKey)

// Register this immediately after calling createClient!
// Because signInWithOAuth causes a redirect, you need to fetch the
// provider tokens from the callback.
supabase.auth.onAuthStateChange((event, session) => {
  if (session && session.provider_token) {
    window.localStorage.setItem('oauth_provider_token', session.provider_token)
  }

  if (session && session.provider_refresh_token) {
    window.localStorage.setItem('oauth_provider_refresh_token', session.provider_refresh_token)
  }

  if (event === 'SIGNED_OUT') {
    window.localStorage.removeItem('oauth_provider_token')
    window.localStorage.removeItem('oauth_provider_refresh_token')
  }
})

// let { data: issues, error } = await supabase
//   .from('tickets')
//   .select('*')
          

// console.log(issues)


export default function Home() {
  useEffect(() => {
    const signIn = async () => {
      await supabase.auth.signInWithOAuth({
        provider: 'github',
        options: {
          scopes: 'repo gist notifications'
        }
      });
    };

    signIn();
  }, []);
  return (
    <>
      <Navbar />    
      {/* <main>
        <div className="overflow-x-auto">
          <table className="table">

            <thead>
            <tr>
              <th>Ticket #</th>
              <th>Name</th>
            </tr>
            </thead>
            <tbody>

              {issues.map((issue) => (
                <tr key={issue.id}>
                  <td>{issue.id}</td>
                  <td>{issue.message}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </main> */}
    </>
  );
}
