import React from "react";
import "../TopColleges/TopColleges.css";
import NavBar from "../../components/NavBar/NavBar.js";
import IitImage from "../../components/IitImage/IitImage.js";
import NitImage from "../../components/NitImage/NitImage.js";

function TopCollege() {
  return (
    <div>
      <NavBar />
      <div className="college-container">
        <IitImage />
        <NitImage />
      </div>
    </div>
  );
}

export default TopCollege;