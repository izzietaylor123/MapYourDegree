import './Home.css';
function Choose_degree() {
    return (
      <div className="degree-container">
        <h2>Choose your degree plan</h2>
        <form>
          <input type="major" placeholder="Major" />
          <input type="concentration" placeholder="Concentration" />
          <input type="minor" placeholder="Minor" />
          <button type="submit">Sign Up</button>
        </form>
      </div>
    );
  }
  
  export default CreateAccount;