from app.models.task import Task


def create_task(
    db,
    user_id,
    data
):

    task = Task(
        user_id=user_id,
        title=data.title,
        description=data.description,
        status="pending"
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


def get_tasks(
    db,
    user_id
):

    return (
        db.query(Task)
        .filter(
            Task.user_id == user_id
        )
        .all()
    )


def complete_task(
    db,
    task_id
):

    task = (
        db.query(Task)
        .filter(
            Task.id == task_id
        )
        .first()
    )

    if task:

        task.status = "completed"

        db.commit()
        db.refresh(task)

    return task