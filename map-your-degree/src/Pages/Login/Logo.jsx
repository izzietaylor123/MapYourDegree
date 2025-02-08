import logo from '../../assets/logo.jpeg';
import '../Login/Logo.css';

function Logo() {
    return (
    <div className="logo"> 
    <img src={logo} alt="Logo" width="100px"/>
    </div>
    )
}

export default Logo;
