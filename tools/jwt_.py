import jwt
from django.conf import settings
def get_jwt(payload):
    headers = {
        'typ': 'jwt',
        'alg': 'HS256'
    }
    payload = payload
    token = jwt.encode(payload=payload, key=settings.SECRET_KEY, algorithm="HS256", headers=headers)
    return token
