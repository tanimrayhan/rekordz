from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# ===============================
# CORS (ALLOW NETLIFY)
# ===============================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # lock later
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ===============================
# DATA MODEL
# ===============================
class Note(BaseModel):
    content: str

# ===============================
# TEMP STORAGE (IN MEMORY)
# ===============================
stored_note = ""

# ===============================
# ROOT (DEBUG / HEALTH CHECK)
# ===============================
@app.get("/")
def root():
    return {"status": "FastAPI is running"}

# ===============================
# GET NOTES
# ===============================
@app.get("/notes")
def get_notes():
    return {"content": stored_note}

# ===============================
# SAVE NOTES
# ===============================
@app.post("/notes")
def save_notes(note: Note):
    global stored_note
    stored_note = note.content
    return {"status": "saved"}
