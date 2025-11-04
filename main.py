from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Notes API")

class Note(BaseModel):
    id: int
    text: str

# In-memory storage for the sake of the demo
notes_db = {}

@app.post("/notes", response_model=Note)
def create_note(note: Note):
    if note.id in notes_db:
        raise HTTPException(status_code=400, detail="Note with this ID already exists.")
    notes_db[note.id] = note
    return note

@app.get("/notes", response_model=List[Note])
def get_notes():
    return list(notes_db.values())

@app.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int):
    if note_id not in notes_db:
        raise HTTPException(status_code=404, detail="Note not found.")
    return notes_db[note_id]

@app.delete("/notes/{note_id}", response_model=dict)
def delete_note(note_id: int):
    if note_id not in notes_db:
        raise HTTPException(status_code=404, detail="Note not found.")
    del notes_db[note_id]
    return {"ok": True}
