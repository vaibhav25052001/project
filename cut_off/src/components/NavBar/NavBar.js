import React from "react";
import "../NavBar/NavBar.css";
import { Link } from "react-router-dom";
function NavBar() {
  return (
    <div className="nav-container">
      <div className="heading-container">
        <Link to="/" style={{ textDecoration: "none" }}>
          <h1>College Predictor</h1>
        </Link>
      </div>
      <div className="btn-container">
        <Link to="/iit">
          <button className="btn , btniit">IIT</button>
        </Link>
        <Link to="/nit">
          <button className="btn , btnnit">NIT</button>
        </Link>
        <Link to="/topcollege">
          <button className="btn btnNext">Top Colleges</button>
        </Link>
      </div>
    </div>
  );
}
export default NavBar;