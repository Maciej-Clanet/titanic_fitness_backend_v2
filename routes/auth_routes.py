import json
from fastapi import APIRouter, HTTPException

from models.auth_models import LoginForm, RegisterForm

auth_router = APIRouter()

def get_all_users():
    with open("./fake_db/users.json", "r") as file:
        return json.load(file)

def save_users(new_users):
    with open("./fake_db/users.json", "w") as file:
        file.write(json.dumps(new_users, indent=4))
        # this is a comment


@auth_router.post("/register")
def register(register_data: RegisterForm):

    all_users = get_all_users()
    email = register_data.email

    if email in all_users:
        raise HTTPException(409, "User already exists")
    
    new_user = {
        "email": register_data.email,
        "username": register_data.username,
        "password": register_data.password,
    }

    all_users[email] = new_user

    save_users(all_users)
    return new_user


@auth_router.post("/login")
def login(login_data: LoginForm):
    all_users = get_all_users()
    email = login_data.email

    if email not in all_users:
        raise HTTPException(401,"Invalid Credentials")
    
    if all_users[email]["password"] != login_data.password:
        raise HTTPException(401,"Invalid Credentials")
    
    return all_users[email]

