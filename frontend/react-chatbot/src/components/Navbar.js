import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="navbar">
      <h2>LoanEase</h2>

      <div className="nav-links">
        <Link to="/">Home</Link>
        <Link to="/history">Loan History</Link>
        <Link to="/about">About</Link>
      </div>

      <button className="logout-btn">Logout</button>
    </nav>
  );
};

export default Navbar;


