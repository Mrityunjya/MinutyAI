import React from "react";

const Sentiment = ({ data }) => {
  return (
    <div className="sentiment-card">
      <h3 className="section-title">Sentiment Analysis</h3>
      <div className="sentiment-stats">
        <p><strong>Positive:</strong> {data.positive ? (data.positive * 100).toFixed(1) : "0"}%</p>
        <p><strong>Negative:</strong> {data.negative ? (data.negative * 100).toFixed(1) : "0"}%</p>
        <p><strong>Neutral:</strong> {data.neutral ? (data.neutral * 100).toFixed(1) : "0"}%</p>
      </div>
    </div>
  );
};

export default Sentiment;

