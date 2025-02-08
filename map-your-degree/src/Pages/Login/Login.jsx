import './login.css';
import { Link } from "react-router-dom";

function Login() {
  return (
    <div className="login-container">
      <h2>Login</h2>
      <form>
        <input 
          type="text" 
          placeholder="Username" 
          name="username" 
          required 
        />
        <input 
          type="password" 
          placeholder="Password" 
          name="password" 
          required 
          />
          <button type="submit" className="login-btn">
            Login
          </button>
          <Link to="/create-account">
            <button type="button" className="create-account-btn">
              Create an Account
            </button>
          </Link>
          <Link to="/home" className="go-home-btn">
          <button type="button">
            Go to Homepage
          </button>
        </Link>
        </form>
      </div>

      
  );
}

export default Login;
