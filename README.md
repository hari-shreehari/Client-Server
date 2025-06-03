
A minimal “server” (FastAPI + SQLite) and “client” (plain HTML + JavaScript) setup.  
Users can submit their Name + DOB to the backend (which writes into a SQLite DB), and can also add two numbers purely in the browser.

# Structure
- **client/**  
  - `index.html` – HTML form + “add two numbers” widget  
  - `script.js` – JavaScript logic (handles form submission and client-side addition)

- **server/**  
  - `main.py` – FastAPI app (exposes `/submit-data`)  
  - `database.db` – SQLite database (created automatically on startup)  
  - `__pycache__/` – ignore these byte-compiled files

---

## ⚙️ Prerequisites

1. **Python 3.10+** (any recent 3.x will work)
2. **pip** (comes with Python)
3. VS Code (or any code editor) is recommended but not required
4. A modern web browser (Chrome, Firefox, Edge, etc.)

---

# 🛠️ Setup & Run (Windows/macOS/Linux)

> These steps assume you’re using VS Code, but they also work in any terminal.

1. **Clone or download the repo**.  
    ```bash
    git clone https://github.com/hari-shreehari/Client-Server
    ```

2. **Open the project in VS Code** (or your editor).  
- In VS Code:  
  - **File → Open Folder…** → select `Client-Server/`.

3. **Create (and activate) a Python virtual environment** (optional).

- **Windows (PowerShell)**:
  ```powershell
  cd server
  python -m venv venv
  .\venv\Scripts\Activate.ps1
  ```
- **macOS/Linux (bash/zsh)**:
  ```bash
  cd server
  python3 -m venv venv
  source venv/bin/activate
  ```

After activation, you should see `(venv)` at the start of your prompt.

4. **Install Python dependencies**.  
In VS Code’s integrated terminal (make sure you’re inside `server/` and your venv is active), run:

```bash
pip install fastapi uvicorn aiosqlite pydantic
```

# What this does:

1. fastapi: Web framework
2. uvicorn: ASGI server to run FastAPI
3. aiosqlite: Async interface to SQLite
4. pydantic: Data validation (used by FastAPI)

Start the FastAPI server.  
From within Client-Server/server/ (and with your venv active), run:

```bash
uvicorn main:app --reload
```

You should see something like:

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [XXXX] using statreload

On first run, database.db is created automatically in server/, and a users table is set up.


## Open the client (HTML + JS).  
You have two options:

### Directly via browser (file://)

 In your file manager, double-click index.html, which opens it in your browser (URL will start with file://).

### In VS Code’s Explorer
 Right-click on client/index.html → Open with Live Server (if you have the Live Server extension), or


# Use the web app.

## Submit Name + DOB

1. Type a name (e.g. “Alice”)

2. Pick a date (e.g. “1990-05-15”)

3. Click Submit to Server

4. You should see “User data saved.” displayed below the button.

5. Behind the scenes, FastAPI inserted that row into server/database.db (table: users).

## Add 2 Numbers (Client-Side)

1. Enter a number in Number A (e.g. “5”)

2. Enter a number in Number B (e.g. “7”)

3. Click Compute Sum

4. You’ll immediately see “Sum = 12” appear—computed entirely in your browser (no server call).  
