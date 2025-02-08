import { useState } from 'react'
//import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import './App.css'
import Header from './Pages/Login/Header'
import Login from './Pages/Login/Login.jsx'

function App() {

  return (
    <>
    <Header></Header>
    <Login/>
    </>
  )
}

export default App