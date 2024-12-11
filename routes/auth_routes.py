import json
from fastapi import APIRouter, HTTPException

from models.auth_models import LoginForm, SignInForm

auth_router = APIRouter()


# this will be used to get the "users database" so we can modify it
def get_all_users():
    with open("./fake_db/users.json", "r") as file:
        return json.load(file)


# This will be used to save the "users database" once we modified it
def save_users(new_users):
    with open("./fake_db/users.json", "w") as file:
        file.write(json.dumps(new_users, indent=4))


@auth_router.post("/register")
def register(register_data: SignInForm):

    all_users = get_all_users()  # get users db
    email = register_data.email

    if email in all_users:
        raise HTTPException(409, "User already exists")

    # extract new user info from the form
    new_user = {
        "email": register_data.email,
        "username": register_data.display_name,
        "password": register_data.password,
    }

    # make a new entry in the user db
    all_users[email] = new_user
    save_users(all_users)
    return new_user


@auth_router.post("/login")
def login(login_data: LoginForm):

    all_users = get_all_users()
    email = login_data.email

    if email not in all_users:
        raise HTTPException(401, "Invalid Credentials")

    if all_users[email]["password"] != login_data.password:
        raise HTTPException(401, "Invalid Credentials")

    return all_users[email]
