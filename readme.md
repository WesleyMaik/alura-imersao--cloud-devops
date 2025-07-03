# Imersão DevOps - Alura Google Cloud

This project is an API developed with FastAPI to manage students, courses, and enrollments in an educational institution.

## Prerequisites

- [Python 3.10 or higher installed](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/get-started/)

## Steps to run the project

1. **Download the repository:**
   [Click here to download](https://github.com/guilhermeonrails/imersao-devops/archive/refs/heads/main.zip)

2. **Create a virtual environment:**
   ```sh
   python3 -m venv ./venv
   ```

3. **Activate the virtual environment:**
   - On Linux/Mac:
     ```sh
     source venv/bin/activate
     ```
   - On Windows, open a terminal in administrator mode and run the command:
   ```sh
   Set-ExecutionPolicy RemoteSigned
   ```

     ```sh
     venv\Scripts/activate
     ```

4. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```sh
   uvicorn app:app --reload
   ```

6. **Access the interactive documentation:**

   Open your browser and go to:  
   [http://127.0.0.1:8000/docs](http://127.00.1:8000/docs)

   Here you can test all API endpoints interactively.

---

## Project Structure

- `app.py`: Main FastAPI application file.
- `models.py`: Database models (SQLAlchemy).
- `schemas.py`: Validation schemas (Pydantic).
- `database.py`: SQLite database configuration.
- `routers/`: Directory with route files (students, courses, enrollments).
- `requirements.txt`: Project dependencies list.

---

- The SQLite database will be automatically created as `escola.db` on the first run.
- To reset the database, simply delete the `escola.db` file (this will erase all data).

---
