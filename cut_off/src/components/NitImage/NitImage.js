import React from "react";
import "../NitImage/NitImage.css";
function NitImage() {
  return (
    <div className="nitImage-container">
      <div className="nitheading">
        <p>Top NIT's (NIT based on NIRF Ranking)</p>
      </div>

      <div className="nitimageContainer">
        <div className="data">
          <p>NIT Trichi</p>
          <div className="image">
            <img src="../../images/NIT-Tiruchirappalli.jpeg" alt="hi" />
          </div>
        </div>
        <div className="data">
          <p>NIT Rourkela</p>
          <div className="image">
            <img src="../../images/NIT-Rourkela.webp" alt="" />
          </div>
        </div>
        <div className="data">
          <p>NIT Warangal</p>
          <div className="image">
            <img src="../../images/NIT-Warangal.jpeg" alt="" />
          </div>
        </div>
        <div className="data">
          <p>NIT Calicut</p>
          <div className="image">
            <img src="../../images/NIT-Calicut.webp" alt="" />
          </div>
        </div>
        <div className="data">
          <p>NIT Jaipur</p>
          <div className="image">
            <img src="../../images/NIT-Jaipur.png" alt="" />
          </div>
        </div>
        <div className="data">
          <p>NIT Silchar</p>
          <div className="image">
            <img src="../../images/NIT-Silchar.jpeg" alt="" />
          </div>
        </div>
      </div>
    </div>
  );
}

export default NitImage;