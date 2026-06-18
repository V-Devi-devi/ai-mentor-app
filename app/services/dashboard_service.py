def get_dashboard(
    user,
    onboarding,
    roadmap,
    tasks,
    interviews,
    chats
):

    # Roadmap Progress
    total_topics = len(roadmap)
    completed_topics = sum(
        1 for r in roadmap
        if r.status == "completed"
    )

    roadmap_percentage = 0

    if total_topics > 0:
        roadmap_percentage = round(
            (completed_topics / total_topics) * 100,
            2
        )

    # Tasks Progress
    total_tasks = len(tasks)

    completed_tasks = sum(
        1 for t in tasks
        if t.status == "completed"
    )

    pending_tasks = (
        total_tasks -
        completed_tasks
    )

    # Interview Performance
    total_interviews = len(interviews)

    average_score = 0

    if total_interviews > 0:

        total_score = sum(
            i.score
            for i in interviews
        )

        average_score = round(
            total_score /
            total_interviews,
            2
        )

    # Chat Statistics
    questions_asked = len(chats)

    return {
        "profile": {
            "username":
            user.username,

            "target_role":
            onboarding.target_role,

            "skills":
            onboarding.skills
        },

        "roadmap_progress": {
            "completed":
            completed_topics,

            "total":
            total_topics,

            "percentage":
            roadmap_percentage
        },

        "tasks": {
            "completed":
            completed_tasks,

            "pending":
            pending_tasks,

            "total":
            total_tasks
        },

        "interviews": {
            "total":
            total_interviews,

            "average_score":
            average_score
        },

        "learning_activity": {
            "questions_asked":
            questions_asked
        }
    }