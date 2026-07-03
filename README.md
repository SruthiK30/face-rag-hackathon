# Face RAG Hackathon Project

A face recognition system combined with Retrieval-Augmented Generation (RAG), built for a hackathon. The system recognizes a face and uses an LLM-powered RAG pipeline to retrieve and generate relevant information about the recognized person.

## What It Does
- Detects and recognizes faces from an image/video feed
- Matches the recognized face against a stored database of known individuals
- Retrieves relevant context/data tied to that person
- Uses OpenAI's API to generate a natural-language response based on the retrieved information

## Architecture
See `architecture.png` for the full system design and data flow.

## Project Structure
- `face_recognition/` — face detection and recognition logic
- `rag_engine/` — retrieval-augmented generation pipeline (OpenAI API integration)
- `backend/` — server/API logic connecting the pieces together
- `frontend/` — user interface
- `database/` — stores known face data / retrieval records
- `logs/` — runtime logs

## Tech Stack
- Python
- OpenAI API (LLM for the RAG generation step)
- Face recognition library (OpenCV / face_recognition)
- HTML/CSS/JS frontend

## Setup
1. Clone this repo
2. Create a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   *(Add a `requirements.txt` if you don't have one — list what `backend/`, `face_recognition/`, and `rag_engine/` actually import)*
4. Create a `.env` file inside `rag_engine/` with your own OpenAI API key:
   ```
   OPENAI_API_KEY=your_key_here
   ```
   **Never commit this file** — it's already in `.gitignore`.
5. Run the backend:
   ```bash
   python backend/<your_main_file>.py
   ```

## Security Note
If you fork or clone this repo, always use your own API key and never commit `.env` files.

## Status
Built during a hackathon — combines computer vision (face recognition) with RAG to demonstrate personalized, context-aware information retrieval.
