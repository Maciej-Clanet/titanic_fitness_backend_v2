import json
from typing import List
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from models.workout_models import GetDay
from .auth_routes import get_all_users

workouts_router = APIRouter()


def get_all_workouts():
    with open("./fake_db/workouts.json", "r") as file:
        return json.load(file)


@workouts_router.get("/")
def get_workouts():
    return get_all_workouts()


class Workout(BaseModel):
    name: str
    exercises: List[str]


@workouts_router.post("/")
def add_workout(new_workout: Workout):
    all_workouts = get_all_workouts()

    all_workouts.append(new_workout.model_dump())

    with open("./fake_db/workouts.json", "w") as file:
        file.write(json.dumps(all_workouts, indent=4))

    return all_workouts



@workouts_router.post("/workout_day")
def get_workout_day(data: GetDay):

    all_users = get_all_users()
    
    if data.user_email not in all_users:
        raise HTTPException(404, "no user found")
    
    user = all_users[data.user_email]

    # get workout day
    workouts = user["workouts"]

    day = workouts.get(data.date, {})
    # get allows us to specify a default if it doesnt exist

    return day