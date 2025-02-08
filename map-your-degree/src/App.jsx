import { useState } from 'react'
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import './App.css'
import Header from './Pages/Login/Header'
import Login from './Pages/Login/Login.jsx'
import CreateAccount from './Pages/CreateAccount/CreateAccount.jsx';

function App() {
  return (
    <> 
    <Header />
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/create-account" element={<CreateAccount />} />
      </Routes>
    </Router>
    </>
  )
}

export default App