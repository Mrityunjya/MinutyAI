import React from "react";

const Transcription = ({ text }) => {
  return (
    <div className="transcription-card">
      <h3 className="section-title">Live Transcription</h3>
      <p className="transcription-text">{text || "Waiting for input..."}</p>
    </div>
  );
};

export default Transcription;
