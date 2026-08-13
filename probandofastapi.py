# siempre poner en terminal antes de empezar para levantar server (se detiene con Ctrl + C)
# uvicorn probandofastapi:app --reload

from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()

def crear_base():
    conn = sqlite3.connect("simbolic.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS artifacts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            archive TEXT,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

crear_base()

@app.get("/")
def inicio():
    return {"mensaje": "Archivo online"}

@app.get("/simbolic.exe")
def archivista():
    return {"status": "STANDBY", "archive": "001"}

@app.get("/artifact/{id}")
def get_artifact(id: int):
    return {"artifact_id": id, "status": "PRESERVED", "archive": "001"}

@app.get("/search")
def search(archive: str = "001"):
    return {"searching_in_archive": archive, "status": "ACTIVE"}

class Artifact(BaseModel):
    nombre: str
    archive: str
    status: str

@app.post("/artifact")
def crear_artifact(artifact: Artifact):
    return {"mensaje": "Artifact registrado", "datos": artifact}