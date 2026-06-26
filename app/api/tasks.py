from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.task import TaskCreate

from app.services.task_service import (
    create_task,
    get_tasks,
    complete_task
)

from app.core.dependencies import (
    get_current_user
)

from app.models.user import User

router = APIRouter()


# ==========================
# Create Task
# ==========================
@router.post("/create")
def add_task(
    data: TaskCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):

    return create_task(
        db,
        user_id=user.id,
        data=data
    )


# ==========================
# Get User Tasks
# ==========================
@router.get("/")
def all_tasks(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):

    return get_tasks(
        db,
        user_id=user.id
    )


# ==========================
# Complete Task
# ==========================
@router.put("/{task_id}/complete")
def finish_task(
    task_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user)
):

    task = complete_task(
        db,
        task_id
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return {
        "message": "Task completed successfully",
        "task": task
    }