import { Link } from "react-router-dom";
import "./Navbar.css";

const Navbar = () => {
  return (
    <nav className="navbar">
      <h2 className="logo">LoanEase</h2>

      <div className="nav-links">
        <Link to="/">Home</Link>
        <Link to="/history">Loan History</Link>
        <Link to="/about">About</Link>
      </div>
    </nav>
  );
};

export default Navbar;
