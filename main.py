from fastapi import FastAPI
import uvicorn

from dotenv import load_dotenv
import os

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
    host = os.getenv("APP_HOST", "127.0.0.1")
    reload = os.getenv("APP_RELOAD", "1") == "1"
    uvicorn.run("main:app", host=host, port=8080, reload=reload)
