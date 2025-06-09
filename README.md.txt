# Face Recognition + RAG AI Hackathon

## Overview
A full-stack AI platform that registers, recognizes faces in real-time, and answers queries using Retrieval-Augmented Generation (RAG).

## Tech Stack
- Frontend: React.js
- Backend: Node.js (WebSockets + APIs)
- Face Recognition: Python (`face_recognition`, `cv2`)
- RAG Engine: Python (LangChain, FAISS, OpenAI)
- Database: SQLite (or MongoDB)
- Logging: Python's `logging` module

## Features
- Register face from webcam
- Live recognition with multiple faces
- Chat-based queries like:
  - "Who was the last person registered?"
  - "When was Karthik registered?"
- Logging of all major events

## Setup Instructions
```bash
# 1. Install Python dependencies
cd face_recognition/
pip install -r requirements.txt

# 2. Start face recognition APIs
python registernrecognize.py

# 3. Start Node.js server
cd backend/
npm install
node app.js

# 4. Start frontend
cd frontend/
npm install
npm start
