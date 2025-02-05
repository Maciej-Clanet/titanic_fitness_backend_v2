import json
from typing import List
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from models.workout_models import AddExercise, GetDay, WorkoutDay
from .auth_routes import get_all_users, save_users

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


@workouts_router.post("/workout_day", response_model=WorkoutDay)
def get_workout_day(data: GetDay):

    all_users = get_all_users()

    # error if user doesn't exist
    if data.user_email not in all_users:
        raise HTTPException(404, "no user found")

    user = all_users[data.user_email]

    workouts = user["workouts"]
    day = workouts.get(data.date, {"exercises": {}})
    # get allows us to specify a default if it doesnt exist

    return day


@workouts_router.post("/add_exercise")
def add_exercise(data: AddExercise):
    all_users = get_all_users()

    # error if user doesn't exist
    if data.user_email not in all_users:
        raise HTTPException(404, "no user found")

    user = all_users[data.user_email]

    workouts = user["workouts"]

    if data.date not in workouts:
        print("didnt find exercise for this date")
        workouts[data.date] = {"exercises": {}}

    exercises = workouts[data.date]["exercises"]

    if data.exercise_name not in exercises:
        print("no existing entry for exercise, initialising with empty list")
        exercises[data.exercise_name] = []

    # we create an exercise entry object to save
    new_entry = {"reps": data.reps, "weight": data.weight}
    # append it to the exercise
    exercises[data.exercise_name].append(new_entry)

    save_users(all_users)

    # 201 code stands for "created"
    return JSONResponse(
        status_code=201, content={"message": "Exercise added successfully"}
    )
