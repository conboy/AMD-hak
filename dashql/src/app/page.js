import Navbar from "./components/Navbar";
import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://cipubdiqomjtsdayksmf.supabase.co'
const supabaseKey = process.env.SUPABASE_KEY
const supabase = createClient(supabaseUrl, supabaseKey)


let { data: issues, error } = await supabase
  .from('tickets')
  .select('*')
          

console.log(issues)
export default function Home() {

  return (
    <>
      <Navbar />    
      <main>
        <div className="overflow-x-auto">
          <table className="table">
            {/* head */}
            <thead>
            <tr>
              <th>Ticket #</th>
              <th>Name</th>
            </tr>
            </thead>
            <tbody>
              {/* body */}
              {issues.map((issue) => (
                <tr key={issue.id}>
                  <td>{issue.id}</td>
                  <td>{issue.message}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </main>
    </>
  );
}
