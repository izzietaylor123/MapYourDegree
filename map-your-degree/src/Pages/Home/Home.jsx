import './Home.css';
import { Link } from "react-router-dom";

function Home() {
    return (
      <div className="degree-container">
        <h2>Choose Your Degree Plan</h2>
        <form>
          <input type="major" placeholder="Major" />
          <input type="concentration" placeholder="Concentration" />
          <Link to="/degree-results" >
          <button type="submit">Submit</button>
          </Link>
        </form>
      </div>
    );
  }
  
  export default Home;