import React, { useState } from 'react';
import './App.css';

function App() {
  const [file, setFile] = useState(null);
  const [transcript, setTranscript] = useState('');
  const [summary, setSummary] = useState('');
  const [sentiment, setSentiment] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  // Handle file upload
  const handleFileUpload = async (event) => {
    const uploadedFile = event.target.files[0];
    setFile(uploadedFile);

    // File validation
    if (!uploadedFile) {
      setError("Please select a file.");
      return;
    }

    const fileType = uploadedFile.type;
    const fileSize = uploadedFile.size;

    // Check if the file is an audio file (e.g., mp3, wav)
    if (!fileType.startsWith('audio/')) {
      setError("Please upload a valid audio file.");
      return;
    }

    // Limit file size to 10MB (adjust this value as needed)
    if (fileSize > 10 * 1024 * 1024) {
      setError("File size exceeds the maximum limit of 10MB.");
      return;
    }

    const formData = new FormData();
    formData.append("file", uploadedFile);

    setLoading(true);
    setError(''); // Reset error message

    try {
      const response = await fetch("http://localhost:8000/process_audio/", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Failed to process the file');
      }

      const data = await response.json();

      setTranscript(data.transcript || '');
      setSummary(data.summary || '');
      setSentiment(data.sentiment || '');
    } catch (error) {
      setError('An error occurred while processing the file. Please try again.');
      console.error('Error during file upload:', error);
    } finally {
      setLoading(false);
    }
  };

  // Clear all the states (optional)
  const handleClear = () => {
    setFile(null);
    setTranscript('');
    setSummary('');
    setSentiment('');
    setError('');
  };

  return (
    <div className="App">
      <h1 className="ai-title">AI Meeting Minutes Generator</h1>

      {/* File input */}
      <input type="file" className="file-input" onChange={handleFileUpload} />

      {file && (
        <div>
          <h3 className="file-info">Selected File: {file.name}</h3>
          <p className="file-size">Size: {Math.round(file.size / 1024)} KB</p>
        </div>
      )}

      {/* Progress bar */}
      {loading && (
        <div className="progress-container">
          <div className="progress-bar" style={{ width: '50%' }}></div> {/* Dynamically adjust width */}
        </div>
      )}

      {/* Error message */}
      {error && <p className="error-message">{error}</p>}

      {/* Showing the transcript */}
      {transcript && (
        <div className="transcript-card">
          <h2 className="section-title">Transcript</h2>
          <p>{transcript}</p>
        </div>
      )}

      {/* Showing the summary */}
      {summary && (
        <div className="summary-card">
          <h2 className="section-title">Summary</h2>
          <p>{summary}</p>
        </div>
      )}

      {/* Showing the sentiment */}
      {sentiment && (
        <div className="sentiment-box">
          <h2 className="section-title">Sentiment Analysis</h2>
          <p>{sentiment}</p>
        </div>
      )}

      {/* Clear button */}
      <button className="clear-button" onClick={handleClear}>Clear</button>
    </div>
  );
}

export default App;
