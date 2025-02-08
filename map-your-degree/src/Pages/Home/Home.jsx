import './Home.css';
function Home() {
    return (
      <div className="degree-container">
        <h2>Choose Your Degree Plan</h2>
        <form>
          <input type="major" placeholder="Major" />
          <input type="concentration" placeholder="Concentration" />
          <button type="submit">Submit</button>
        </form>
      </div>
    );
  }
  
  export default Home;