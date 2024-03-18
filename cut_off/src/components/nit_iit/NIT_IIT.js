import React, { useState } from "react";
import { useParams } from "react-router";
import "../nit_iit/NIT_IIT.css";

function NIT_IIT() {
  const [category, setCatogary] = useState("");
  const [gender, setGender] = useState("");
  const [Quota, setQuota] = useState("");
  const [Round, setRound] = useState("");
  const [open, setOpen] = useState("");
  const [close, setClose] = useState("");

  const userID = useParams();
  const name = userID.id;

  const handleSubmit = (e) => {
    e.preventDefault();
    const data={
      category,Quota,gender,Round,open,close
    }
    fetch('/predict', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body:JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error('Error:', error));
  };

  return (
    <div className="NIT_IIT-container">
      <div className="heading">
        <h1>College Predictor System</h1>
      </div>
      {/* --------------------------------- */}
      <div className="data-container">
        <div className="col-md">
          <div className="form-floating">
            <select
              className="form-select"
              id="floatingSelectGrid"
              value={category}
              onChange={(event) => setCatogary(event.target.value)}
            >
              <option selected>Select Your category</option>
              <option value="General">General</option>
              <option value="OBC-NCL">OBC-NCL</option>
              <option value="SC">SC</option>
              <option value="ST">ST</option>
              <option value="General-PWD">General-PWd</option>
              <option value="OBC-NCL-PWD">OBC-NCL-PWD</option>
              <option value="SC-PWD">SC-PWD</option>
              <option value="ST-PWD">ST-PWD</option>
              <option value="General-EWS">General-EWS</option>
              <option value="General-EWS-PWD">General-EWS-PWD</option>
            </select>
          </div>
        </div>

        {name === "nit" ? (
          <div className="col-md">
            <div className="form-floating">
              <select
                className="form-select"
                id="floatingSelectGrid"
                value={Quota}
                onChange={(event) => setQuota(event.target.value)}
              >
                <option selected>Select Your Quota</option>
                {/* <option value="All India">All India</option> */}
                <option value="Home State">Home State</option>
                <option value="Other State">Other State</option>
                <option value="Andra Pradesh">Andhra Pradesh </option>
                <option value="Goa">Goa</option>
                <option value="Jammu Kashmir">Jammu & Kashmir</option>
                <option value="Ladakh">Ladakh</option>
              </select>
            </div>
          </div>
        ) : (
          <div className="col-md">
            <div className="form-floating">
              <select
                className="form-select"
                id="floatingSelectGrid"
                value={Quota}
                onChange={(event) => setQuota(event.target.value)}
              >
                <option selected>Select Your Quota</option>
                <option value="All India">All India</option>
              </select>
            </div>
          </div>
        )}
        <div className="col-md">
          <div className="form-floating">
            <select
              className="form-select"
              id="floatingSelectGrid"
              value={gender}
              onChange={(event) => setGender(event.target.value)}
            >
              <option selected>Choose Your Gender</option>
              <option value="Neutral">Neutral</option>
              <option value="Female">Female</option>
            </select>
          </div>
        </div>
        <div className="col-md">
          <div className="form-floating">
            <select
              className="form-select"
              id="floatingSelectGrid"
              value={Round}
              onChange={(event) => setRound(event.target.value)}
            >
              <option selected>Preferred Round Number</option>
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
              <option value="3">4</option>
              <option value="3">5</option>
              <option value="3">6</option>
              <option value="3">7</option>
            </select>
          </div>
        </div>
        <div className="form-floating mb-3">
          <input
            type="number"
            className="form-control form-select"
            id="floatingInput"
            placeholder="Enter Your Opening Rank"
            value={open}
            onChange={(event) => setOpen(event.target.value)}
          />
        </div>
        <div className="form-floating mb-3">
          <input
            type="number"
            className="form-control form-select"
            id="floatingInput"
            placeholder="Enter Your Closing Rank"
            value={close}
            onChange={(event) => setClose(event.target.value)}
          />
        </div>
        <div className="btn">
          <button onClick={handleSubmit}>Tap To Predict College</button>
        </div>
      </div>
    </div>
  );
}
export default NIT_IIT;