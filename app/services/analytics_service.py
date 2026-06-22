from app.models.task import Task
from app.models.roadmap import Roadmap
from app.models.interview import Interview
from app.models.chat import Chat


def get_analytics(db, user_id):

    total_tasks = db.query(Task).filter(
        Task.user_id == user_id
    ).count()

    completed_tasks = db.query(Task).filter(
        Task.user_id == user_id,
        Task.status == "Completed"
    ).count()

    task_percentage = 0

    if total_tasks > 0:
        task_percentage = (
            completed_tasks / total_tasks
        ) * 100

    total_roadmaps = db.query(Roadmap).filter(
        Roadmap.user_id == user_id
    ).count()

    completed_roadmaps = db.query(Roadmap).filter(
        Roadmap.user_id == user_id,
        Roadmap.status == "Completed"
    ).count()

    roadmap_percentage = 0

    if total_roadmaps > 0:
        roadmap_percentage = (
            completed_roadmaps / total_roadmaps
        ) * 100

    interviews = db.query(
        Interview
    ).filter(
        Interview.user_id == user_id
    ).all()

    average_score = 0

    if interviews:
        total_score = sum(
            interview.score
            for interview in interviews
        )

        average_score = (
            total_score / len(interviews)
        )

    total_chats = db.query(
        Chat
    ).filter(
        Chat.user_id == user_id
    ).count()

    return {
        "total_tasks": total_tasks,
        "completed_tasks": completed_tasks,
        "task_completion_percentage":
            round(task_percentage, 2),

        "total_roadmaps": total_roadmaps,
        "completed_roadmaps":
            completed_roadmaps,
        "roadmap_completion_percentage":
            round(roadmap_percentage, 2),

        "average_interview_score":
            round(average_score, 2),

        "total_chats":
            total_chats
    }