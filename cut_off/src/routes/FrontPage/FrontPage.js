import React from "react";
import BgImage from "../../components/BgImage/BgImage.js";
import NavBar from "../../components/NavBar/NavBar.js";

function FrontPage() {
  return (
    <div className="frontPage-container">
      <NavBar />
      <BgImage />
    </div>
  );
}
export default FrontPage;