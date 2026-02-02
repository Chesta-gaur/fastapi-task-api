# Task Management API (FastAPI)

A backend REST API built with **FastAPI** and **SQLAlchemy** to practice clean REST design,database integration, and scalable API patterns.
- RESTful API design
- PATCH vs PUT
- Database integration
- Request/response validation

## Features
- CRUD operations for tasks
- Partial updates using **PATCH**
- Filtering by completion status and priority
- Pagination using limit & offset
- SQLite database integration using SQLAlchemy ORM
- Dependency-based database session handling
- Request and response validation with Pydantic

## Tech Stack
- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- Uvicorn

## 📌 API Capabilities

### Endpoints
- `POST /tasks` – Create a task  
- `GET /tasks` – List tasks (supports filtering & pagination)  
- `GET /tasks/{id}` – Get task by ID  
- `PATCH /tasks/{id}` – Partially update a task  
- `DELETE /tasks/{id}` – Delete a task  

### Query Parameters (GET /tasks)
- `completed` → true / false  
- `priority` → 1 to 5  
- `limit` → number of records  
- `offset` → pagination offset  

This project is for learning backend development fundamentals.

## ▶️ Run Locally
1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:

```bash
pip install -r requirements.txt


🎯 Purpose of This Project :

This project was built as a learning-focused backend application to strengthen:

1. REST API fundamentals
2. Backend data flow and validation
3. SQL database interaction via ORM
4. Clean API design and scalability concepts

It is not production-ready, but reflects real-world backend development practices.


📚 What I Learned

1. Designing RESTful APIs with FastAPI
2. Using SQLAlchemy ORM for database operations
3. Managing database sessions safely
4. Implementing filtering and pagination
5. Handling partial updates correctly with PATCH