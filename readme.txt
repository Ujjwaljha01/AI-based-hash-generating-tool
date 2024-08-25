

---

# AI-Enhanced Hash Generation Tool

## Description
A web-based tool that generates both traditional and AI-enhanced hashes. The tool includes security analysis to evaluate the strength of generated hashes.

## Features
- **AI-Based Hashing:** Leverages a neural network to generate unique hashes.
- **Traditional Hashing:** Supports MD5, SHA-256, SHA-512, bcrypt, and HMAC.
- **Security Analysis:** Provides entropy and length analysis of hashes.

## Tech Stack
- **Frontend:** React
- **Backend:** Flask (Python)
- **Database:** SQLite (optional)
- **AI Model:** TensorFlow

## Setup Instructions

### Backend (Python)
1. **Clone the repository:**
   ```bash
   git clone <repo-link>
   ```
2. **Navigate to the backend folder:**
   ```bash
   cd backend
   ```
3. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```
4. **Activate the environment and install dependencies:**
   ```bash
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   ```
5. **Run the Flask server:**
   ```bash
   flask run
   ```

### Frontend (React)
1. **Navigate to the frontend folder:**
   ```bash
   cd ../frontend
   ```
2. **Install dependencies:**
   ```bash
   npm install
   ```
3. **Start the React server:**
   ```bash
   npm start
   ```

## Usage
1. Open your browser and go to `http://localhost:3000`.
2. Enter the input data and select the hashing method.
3. Click on "Generate Traditional Hash" or "Generate AI Hash" to see the results.

## License
This project is open-source and available under the [MIT License](LICENSE).

---

