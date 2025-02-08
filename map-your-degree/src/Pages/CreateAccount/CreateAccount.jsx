import '.CreatAccount.css'
function CreateAccount() {
    return (
      <div className="create-account-container">
        <h2>Create an Account</h2>
        <form>
          <input type="text" placeholder="Username" />
          <input type="email" placeholder="Email" />
          <input type="password" placeholder="Password" />
          <button type="submit">Sign Up</button>
        </form>
      </div>
    );
  }
  
  export default CreateAccount;