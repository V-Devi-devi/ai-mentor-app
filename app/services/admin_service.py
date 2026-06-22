from app.models.user import User
from app.models.task import Task
from app.models.roadmap import Roadmap
from app.models.interview import Interview
from app.models.chat import Chat


def get_system_stats(db):

    return {
        "total_users":
            db.query(User).count(),

        "total_tasks":
            db.query(Task).count(),

        "total_roadmaps":
            db.query(Roadmap).count(),

        "total_interviews":
            db.query(Interview).count(),

        "total_chats":
            db.query(Chat).count()
    }


def get_all_users(db):
    return db.query(User).all()


def delete_user(db, user_id):

    user = db.query(User).filter(
        User.id == user_id
    ).first()

    if user:
        db.delete(user)
        db.commit()

    return user