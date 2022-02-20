#Time module is responsible for setting an expiry of tokens
import time 
from typing import Dict

#JWT Module is responsible for encoding and decoding generated token strings
import jwt

#Helps to secure the app using a .env file
from decouple import config

#secret key is used for encoding and decoding JWT strings and algorithm value is the type of algorithm used in the encoding process
JWT_SECRET = config("SECRET")
JWT_ALGORITHIM = config("ALGORITHM")

#Helper function to return generated tokens
def token_response(token: str):
    return{
        "access_token": token
    }

def signJWT(user_id: str)-> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHIM)
    return token_response(token)


def decodeJWT(token: str)-> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHIM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}