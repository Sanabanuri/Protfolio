# Sanaullah Farooq - Backend Developer Portfolio

A professional, modern portfolio website built with **FastAPI** (Backend) and **HTML/CSS/JS** (Frontend).

## Features
- **FastAPI Backend**: Robust API with contact form handling and database integration.
- **Modern Frontend**: Responsive design, dark mode, glassmorphism, and smooth animations.
- **SQLite Database**: Stores contact form messages.

## Project Structure
```
d:/My Portfolio/
├── app/                 # Backend source code
│   ├── main.py          # App entry point
│   ├── routers/         # API endpoints
│   ├── models/          # Database models
│   ├── schemas/         # Pydantic schemas
│   ├── database.py      # Database connection
│   └── config.py        # Configuration
├── static/              # Frontend assets
│   ├── css/             # Stylesheets
│   ├── js/              # JavaScript files
│   └── index.html       # Landing page
├── requirements.txt     # Python dependencies
└── README.md            # You are here
```

## How to Run Using `uv`

This project uses `uv` for fast dependency management.

### 1. Prerequisites
- Python 3.8+ installed.
- `uv` installed. If not, install it:
  ```bash
  pip install uv
  # or
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```

### 2. Setup Environment & Install Dependencies
Initialize a virtual environment and install dependencies in one step:

```bash
# Create a virtual environment and verify python version
uv venv

# Activate the environment (Windows)
.venv\Scripts\activate

# Activate the environment (Mac/Linux)
source .venv/bin/activate

# Install dependencies from requirements.txt
uv pip install -r requirements.txt
```

### 3. Run the Application
Start the FastAPI server using `uv run python -m uvicorn` (this ensures Uvicorn runs correctly within the environment):

```bash
uv run python -m uvicorn app.main:app --reload
```

The server will start at `http://127.0.0.1:8000`.

### 4. Access the Website
Open your web browser and go to:
[http://localhost:8000](http://localhost:8000)

## API Documentation
FastAPI provides automatic interactive API documentation. You can access it at:
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)
