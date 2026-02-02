from fastapi import FastAPI, HTTPException, Depends, Query
from pydantic import BaseModel, Field
from typing import Optional
from database import engine, Base, SessionLocal
from models import Task
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI()

# database session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class TaskCreate(BaseModel):
    title : str = Field(..., min_length = 1)
    description : Optional[str] = None
    priority : int = Field(..., ge=1, le=5)

class TaskUpdate(BaseModel):
    title : Optional[str] = Field(None, min_length=1)
    description : Optional[str] = None
    completed : Optional[bool] =  None
    priority : Optional[int] = Field(None, ge=1, le=5)

class TaskResponse(BaseModel):
    id : int
    title : str
    description : Optional[str]
    completed : bool
    priority : int

    model_config = {
        "from_attributes" : True
    }


@app.get("/")
def home():
    return {
        "message" : "task api is running"
    }


@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(
        completed: Optional[bool] = Query(None),
        priority: Optional[int] = Query(None, ge=1, le=5),
        limit: int = Query(10, ge=1, le=100),
        offset: int = Query(0, ge=0),
        db: Session = Depends(get_db)
    ):

    query = db.query(Task)

    if completed is not None:
        query = query.filter(Task.completed == completed)

    if priority is not None:
        query = query.filter(Task.priority == priority)

    tasks = query.offset(offset).limit(limit).all()
    return tasks


@app.post("/tasks",status_code=201, response_model=TaskResponse)
def add_task(task : TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(
        title=task.title,
        description=task.description,
        completed=False,
        priority=task.priority
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


@app.get("/tasks/{id}", response_model=TaskResponse)
def get_task(id : int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="task not found"
        )
    
    return task


@app.patch("/tasks/{id}", response_model=TaskResponse)
def update_task(id : int, updates : TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()

    if not task:
        raise HTTPException(
        status_code=404,
        detail="task not found"
    )

    if updates.title is not None:
        task.title= updates.title
    if updates.description is not None:
        task.description = updates.description
    if updates.completed is not None:
        task.completed = updates.completed
    if updates.priority is not None:
        task.priority = updates.priority      

    db.commit()
    db.refresh(task)

    return task


@app.delete("/tasks/{id}")
def delete_task(id : int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == id).first()
    
    if not task:    
        raise HTTPException(
            status_code=404,
            detail="task not found"
        )
    
    db.delete(task)
    db.commit()

    return {
        "message" : "task deleted succesfully"
    }