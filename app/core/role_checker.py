from fastapi import Depends, HTTPException, status
from app.core.dependencies import get_current_user


def role_required(allowed_roles: list):

    def check_role(
        current_user: str = Depends(get_current_user)
    ):

        # Temporary role mapping
        # Later this will come from PostgreSQL

        user_roles = {
            "admin": "admin",
            "mentor": "mentor",
            "devi": "student"
        }

        role = user_roles.get(
            current_user,
            "student"
        )

        if role not in allowed_roles:

            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Access Denied"
            )

        return {
            "username": current_user,
            "role": role
        }

    return check_role