from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = "mysecretkey"

ALGORITHM = "HS256"

def create_access_token(data: dict):

    expire = datetime.utcnow() + timedelta(hours=1)

    payload = {
        **data,
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )