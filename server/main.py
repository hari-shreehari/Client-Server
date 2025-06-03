from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
import aiosqlite
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = "database.db"


class UserData(BaseModel):
    name: str
    dob: str  

class AddData(BaseModel):
    a: float
    b: float


async def init_db():
    """Create tables if they do not exist."""
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id   INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                dob  TEXT NOT NULL
            )
            """
        )
        await db.execute(
            """
            CREATE TABLE IF NOT EXISTS additions (
                id   INTEGER PRIMARY KEY AUTOINCREMENT,
                a    REAL NOT NULL,
                b    REAL NOT NULL,
                sum  REAL NOT NULL
            )
            """
        )
        await db.commit()


@app.on_event("startup")
async def on_startup():
    if not os.path.exists(DB_PATH):
        open(DB_PATH, "w").close()
    await init_db()


@app.get("/", summary="Serve the HTML frontend")
async def serve_frontend():
    """
    Serve the HTML file (index.html) that contains the forms + JS.
    (Make sure index.html sits next to main.py in the same directory.)
    """
    return FileResponse("index.html", media_type="text/html")


@app.post("/submit-data", summary="Receive name + dob and store in SQLite")
async def submit_data(payload: UserData = Body(...)):
    """
    Expects JSON:
      {
        "name": "Alice",
        "dob": "2000-05-15"
      }
    """
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO users (name, dob) VALUES (?, ?)",
            (payload.name, payload.dob),
        )
        await db.commit()
    return JSONResponse({"message": "User data saved."})


@app.post("/add", summary="Receive two numbers, store in SQLite, return their sum")
async def do_add(payload: AddData = Body(...)):
    """
    Expects JSON:
      {
        "a": 3,
        "b": 4
      }
    Returns JSON:
      {
        "sum": 7
      }
    """
    result = payload.a + payload.b
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute(
            "INSERT INTO additions (a, b, sum) VALUES (?, ?, ?)",
            (payload.a, payload.b, result),
        )
        await db.commit()
    return JSONResponse({"sum": result})

