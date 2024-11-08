from os import getenv

from dotenv import load_dotenv

from fastapi import FastAPI
from uvicorn import run as server_run

# Load environment variables from `.env` file
load_dotenv()

# Create FastAPI app
app = FastAPI()

# Define a route for the root endpoint
@app.get("/")
def read_root():
    return {
        "message": "Welcome to the application."
    }

# Run the app with Uvicorn
if __name__ == "__main__":
    host = getenv("APP_HOST", "127.0.0.1")
    reload = getenv("APP_RELOAD", "1") == "1"
    server_run("main:app", host=host, port=8080, reload=reload)
