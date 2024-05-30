from datetime import datetime, timedelta, timezone
import os
import jwt

SECRET_KEY = os.environ.get('SECRET_KEY') or 'privatepassword'

def encode_token(user_id):
    payload = {
        'exp': datetime.now(timezone.utc) + timedelta(hours=1),
        'sub': user_id
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

