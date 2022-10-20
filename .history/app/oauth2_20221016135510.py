from jose import JWTError, jwt
from datetime import datetime, timedelta


SECRET_KEY = "asdfas87f98as7f89a23asdjkfasdf!@#$(ASDfasfa(#@"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({'exp': expire})

    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algo)
