import './login.css';
//import { Link } from "react-router-dom";

const Login = () => {
  return (
    <div className="login-page">
    <h1 className="website-header">Map Your Degree</h1>
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
        <button type="button" className="create-account-btn">
        <a href="/create-account">Create an Account</a>
        </button>
      </form>
    </div>
    </div>
  );
}

export default Login;
