# app/services/auth_service.py

users = []

def register_user(user):

    users.append(user)

    return True