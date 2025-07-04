# Imersão DevOps - Alura Google Cloud

This project is an API developed with FastAPI to manage students, courses, and enrollments in an educational institution.

## Prerequisites

- [Python 3.10 or higher installed](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/get-started/)

## Steps to run the project

1. **Clone or Download respository:**

- Clone

```sh
git clone https://github.com/WesleyMaik/alura-imersao--cloud-devops.git
```

- Download
  [Click here to download](https://github.com/WesleyMaik/alura-imersao--cloud-devops/archive/refs/heads/main.zip);

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

### Run with Docker:

1. **Build the Docker image:**

```sh
docker build -t api .
```

2. **Run the Docker container:**

```sh
docker run -d -p 8000:80 api
```

3. **Access the API documentation:**

Open your browser and go to:  
[http://localhost:8000/docs](http://localhost:8000/docs)

---

## Project Structure

- `app.py`: Main FastAPI application file.
- `models.py`: Database models (SQLAlchemy).
- `schemas.py`: Validation schemas (Pydantic).
- `database.py`: SQLite database configuration.
- `routers/`: Directory with route files (students, courses, enrollments).
- `requirements.txt`: Project dependencies list.

---

- The SQLite database will be automatically created as `school.db` on the first run.
- To reset the database, simply delete the `school.db` file (this will erase all data).

---
