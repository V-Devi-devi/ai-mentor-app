from app.models.user import User
from app.models.task import Task
from app.models.roadmap import Roadmap
from app.models.interview import Interview
from app.models.chat import Chat


def get_dashboard(db, user_id):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    total_tasks = db.query(Task).filter(
        Task.user_id == user_id
    ).count()

    completed_tasks = db.query(Task).filter(
        Task.user_id == user_id,
        Task.status == "Completed"
    ).count()

    task_progress = 0

    if total_tasks > 0:
        task_progress = (
            completed_tasks / total_tasks
        ) * 100

    total_roadmaps = db.query(Roadmap).filter(
        Roadmap.user_id == user_id
    ).count()

    completed_roadmaps = db.query(Roadmap).filter(
        Roadmap.user_id == user_id,
        Roadmap.status == "Completed"
    ).count()

    roadmap_progress = 0

    if total_roadmaps > 0:
        roadmap_progress = (
            completed_roadmaps /
            total_roadmaps
        ) * 100

    interviews = db.query(
        Interview
    ).filter(
        Interview.user_id == user_id
    ).all()

    interview_score = 0

    if interviews:
        total_score = sum(
            i.score for i in interviews
        )

        interview_score = (
            total_score /
            len(interviews)
        )

    total_chats = db.query(Chat).filter(
        Chat.user_id == user_id
    ).count()

    overall_performance = (
        task_progress +
        roadmap_progress +
        interview_score
    ) / 3

    if overall_performance >= 80:
        recommendation = (
            "Excellent progress. Start advanced interview preparation."
        )

    elif overall_performance >= 60:
        recommendation = (
            "Good progress. Focus on completing pending tasks."
        )

    else:
        recommendation = (
            "Need improvement. Practice daily and complete roadmap topics."
        )

    return {
        "username": user.username,

        "total_tasks":
            total_tasks,

        "completed_tasks":
            completed_tasks,

        "task_progress":
            round(task_progress, 2),

        "total_roadmaps":
            total_roadmaps,

        "completed_roadmaps":
            completed_roadmaps,

        "roadmap_progress":
            round(roadmap_progress, 2),

        "average_interview_score":
            round(interview_score, 2),

        "total_chats":
            total_chats,

        "overall_performance":
            round(
                overall_performance,
                2
            ),

        "recommendation":
            recommendation
    }