import React from "react";
import IIT1 from '../../images/IIT1.jpg'
import "../BgImage/BgImage.css";
function BgImage() {
  return (
    <div className="bg-container">
      <img src={IIT1} alt="bgi" className="bg-image" />
    </div>
  );
}

export default BgImage;