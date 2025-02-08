import './Header.css'
import logo from '../../assets/logo.jpeg';

function Header() {
    return (
        <div className="header-container">
        <div className="header-text">
         <h1>Map Your Degree</h1> 
        </div>
        <div className="logo"> 
        <img src={logo} alt="Logo" width="100px"/>
        </div>
        </div>
    )
}

export default Header;