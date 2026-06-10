def generate_response(message: str):

    message = message.lower()

    responses = {

        "python":
        "Python is a high-level programming language widely used in AI, web development, and automation.",

        "sql":
        "SQL is used to store, retrieve, and manage data in relational databases.",

        "fastapi":
        "FastAPI is a modern Python framework used to build high-performance APIs.",

        "interview":
        "A technical interview evaluates your programming, problem-solving, and communication skills.",

        "resume":
        "A good resume should contain education, skills, projects, internships, and achievements.",

        "hr":
        "HR interviews focus on communication skills, teamwork, strengths, weaknesses, and career goals.",

        "strength":
        "One example answer: My strength is problem-solving and my ability to learn new technologies quickly.",

        "weakness":
        "One example answer: I sometimes spend extra time perfecting details, but I am learning to balance quality and deadlines.",

        "oops":
        "OOPs stands for Object-Oriented Programming. The four pillars are Encapsulation, Inheritance, Polymorphism, and Abstraction.",

        "dbms":
        "DBMS is software used to create and manage databases. Examples include MySQL and PostgreSQL.",

        "normalization":
        "Normalization is the process of organizing data to reduce redundancy and improve consistency.",

        "api":
        "API stands for Application Programming Interface. It allows different software systems to communicate.",

        "backend":
        "Backend development focuses on server-side logic, databases, APIs, and application security.",

        "frontend":
        "Frontend development focuses on building user interfaces using HTML, CSS, JavaScript, and frameworks like React.",

        "react":
        "React is a JavaScript library used for building interactive user interfaces.",

        "project":
        "When explaining a project, discuss the problem, technologies used, your role, challenges faced, and outcomes.",

        "tell me about yourself":
        "I am a Computer Science student passionate about software development and problem-solving. I have worked on projects using Python, FastAPI, SQL, and React.",

        "why should we hire you":
        "You should hire me because I have strong technical skills, a willingness to learn, and the ability to work effectively in a team.",

        "ai":
        "Artificial Intelligence enables machines to perform tasks that normally require human intelligence, such as learning and decision-making.",

        "machine learning":
        "Machine Learning is a subset of AI where systems learn patterns from data and improve automatically.",

        "placement":
        "To prepare for placements, focus on DSA, DBMS, OOPs, Operating Systems, Aptitude, and Mock Interviews."
    }

    for key, value in responses.items():
        if key in message:
            return value

    return """
I am your AI Placement Mentor.

You can ask me about:
• Python
• SQL
• DBMS
• OOPs
• React
• FastAPI
• Backend Development
• HR Interview Questions
• Resume Building
• Placement Preparation
• AI & Machine Learning
• Project Explanations
"""