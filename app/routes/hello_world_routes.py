from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.get("/")
def say_hello_world():
    return "Hello World!"

@hello_world_bp.get("/hello/JSON")
def camille_info():
    return {
        "name": "Camille",
        "message": "House down BOOTS!",
        "hobbies": ["Horseback riding", "DJing", "Hiking"]
    }

@hello_world_bp.get("/broken-endpoint-with-broken-server-code")
def broken_endpoint():
    response_body = {
        "name": "Ada Lovelace",
        "message": "Hello!",
        "hobbies": ["Fishing", "Swimming", "Watching Reality Shows"]
    }
    new_hobby = "Surfing"
    response_body["hobbies"].append(new_hobby)
    return response_body