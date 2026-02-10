from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sqlite3

app = FastAPI()

# Allow Netlify frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database setup
conn = sqlite3.connect("notes.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
  id INTEGER PRIMARY KEY,
  content TEXT
)
""")
conn.commit()

class Note(BaseModel):
    content: str

@app.get("/notes")
def get_notes():
    cursor.execute("SELECT content FROM notes WHERE id = 1")
    row = cursor.fetchone()
    return {"content": row[0] if row else ""}

@app.post("/notes")
def save_notes(note: Note):
    cursor.execute("DELETE FROM notes")
    cursor.execute("INSERT INTO notes (id, content) VALUES (1, ?)", (note.content,))
    conn.commit()
    return {"status": "saved"}
