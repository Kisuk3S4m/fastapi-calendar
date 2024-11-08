# FastAPI Calendar

A calendar app developed with FastAPI for learning purposes.

## Prerequisites
- Python: 3.10 or above
- PostgreSQL: 13 or above

## Setup and Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/fastapi-calendar.git
    cd fastapi-calendar
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate    # On Linux and macOS
    venv\Scripts\activate   # On Windows
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Create `.env` file and put this content on it:**
    ```env
    # Application environment
    APP_HOST=127.0.0.1
    APP_RELOAD=1    # You can disable reload by set on 0

    # Database connection environment
    # Replace placeholders {} with your actual database credentials
    DATABASE_URL=postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}
    ```

5. **Start the FastAPI server:**
    ```bash
    python main.py
    ```

7. **Access the application:**
    Open your browser and go to `http://127.0.0.1:8000`.
