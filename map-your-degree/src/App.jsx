import { useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import './App.css'
import Logo from './Pages/Login/Logo.jsx'
import Header from './Pages/Login/Header'
import Login from './Pages/Login/Login.jsx'
import CreateAccount from './Pages/CreateAccount/CreateAccount.jsx';

function App() {
  return (
    <>
    
      <div className="header-wrapper">
        <Header />
      </div>

      <div className="logo-wrapper">
    <Logo /> 
    </div>

      <div className="content">
        <Router>
          <Routes>
            <Route path="/" element={<Login />} />
            <Route path="/create-account" element={<CreateAccount />} />
          </Routes>
        </Router>
      </div>
    </>
  );
}

export default App;