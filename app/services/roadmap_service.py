def generate_roadmap(
    target_role,
    current_skills,
    experience_level
):

    role = target_role.lower()

    if role == "backend developer":

        return {
            "Month 1": [
                "Python",
                "OOP",
                "SQL",
                "Git"
            ],

            "Month 2": [
                "FastAPI",
                "PostgreSQL",
                "JWT Authentication",
                "REST APIs"
            ],

            "Month 3": [
                "Docker",
                "Redis",
                "Projects",
                "Deployment"
            ],

            "Projects": [
                "Employee Management System",
                "AI Mentor Backend"
            ]
        }

    elif role == "frontend developer":

        return {
            "Month 1": [
                "HTML",
                "CSS",
                "JavaScript"
            ],

            "Month 2": [
                "React",
                "React Router",
                "Axios"
            ],

            "Month 3": [
                "Redux",
                "Projects",
                "Deployment"
            ],

            "Projects": [
                "Portfolio Website",
                "Employee Dashboard"
            ]
        }

    elif role == "data scientist":

        return {
            "Month 1": [
                "Python",
                "NumPy",
                "Pandas"
            ],

            "Month 2": [
                "Statistics",
                "Machine Learning",
                "Scikit Learn"
            ],

            "Month 3": [
                "Deep Learning",
                "Projects",
                "Deployment"
            ],

            "Projects": [
                "House Price Prediction",
                "Resume Analyzer"
            ]
        }

    else:

        return {
            "message":
            "Roadmap not available for this role"
        }