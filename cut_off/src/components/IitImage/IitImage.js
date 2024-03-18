import React from "react";
import "../IitImage/IitImage.css";
function IitImage() {
  return (
    <div className="iitImage-container">
      <div className="iitheading">
        <p>Top IIT's (IIT based on NIRF Ranking)</p>
      </div>
      <div className="iitimageContainer">
        <div className="data">
          <p>IIT Madras</p>
          <div className="image">
            <img src="../../images/IIT-Madras.avif" alt="" />
          </div>
        </div>
        <div className="data">
          <p>IIT Delhi</p>
          <div className="image">
            <img src="../../images/IIT-Delhi.jpeg" alt="" />
          </div>
        </div>
        <div className="data">
          <p>IIT Bombay</p>
          <div className="image">
            <img src="../../images/IIT-Bombay.jpeg" alt="" />
          </div>
        </div>
        <div className="data">
          <p>IIT Kanpur</p>
          <div className="image">
            <img src="../../images/IIT-Kanpur.jpeg" alt="" />
          </div>
        </div>
        <div className="data">
          <p>IIT Roorkee</p>
          <div className="image">
            <img src="../../images/IIT-Roorkee.webp" alt="" />
          </div>
        </div>
        <div className="data">
          <p>IIT Kharagpur</p>
          <div className="image">
            <img src="../../images/IIT-Kharagpur.avif" alt="" />
          </div>
        </div>
      </div>
    </div>
  );
}

export default IitImage;