# AI Meeting Minutes Generator

## Overview

The **AI Meeting Minutes Generator** is a web application that uses Artificial Intelligence to automatically generate accurate meeting minutes from meeting transcripts. The project employs **FastAPI** for the backend and **React** for the frontend, providing an intuitive interface for generating and viewing meeting summaries.

## Features

- **Automatic Meeting Summarization**: Summarize long meetings into concise and relevant minutes.
- **Searchable Minutes**: Generate minutes that are easy to search and navigate.
- **Real-Time Processing**: Summarize meeting transcripts as the meeting progresses.
- **User-Friendly Interface**: A clean and responsive UI for interacting with meeting summaries.

## Tech Stack

- **Frontend**: React.js
  - React hooks, state management, and UI components
  - Integration with backend API for retrieving and displaying meeting minutes

- **Backend**: FastAPI
  - RESTful API for handling requests such as generating meeting minutes
  - Integration with AI models for text summarization

- **AI/ML Models**:
  - Text summarization model (e.g., OpenAI GPT-3 or GPT-4)

## Setup Instructions

### Prerequisites

Ensure you have the following installed:
- Python 3.x
- Node.js and npm
- A preferred code editor (e.g., VSCode)

### Backend Setup (FastAPI)

1. Clone the repository:
    ```bash
    git clone <repository_url>
    cd backend
    ```

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

The backend should now be running at `http://localhost:8000`.

### Frontend Setup (React)

1. Navigate to the frontend directory:
    ```bash
    cd frontend
    ```

2. Install the required dependencies:
    ```bash
    npm install
    ```

3. Run the React development server:
    ```bash
    npm start
    ```

The frontend should now be running at `http://localhost:3000`.

## API Endpoints

### `/generate_minutes`
- **Method**: POST
- **Description**: Generates meeting minutes from the provided meeting transcript.
- **Request**: Meeting transcript text.
- **Response**: Generated meeting minutes.

### `/summarize_minutes`
- **Method**: POST
- **Description**: Summarizes the provided meeting minutes into a concise version.
- **Request**: Meeting minutes text.
- **Response**: Summarized meeting minutes.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

---

For more information, feel free to contact the project maintainers or refer to the documentation.
