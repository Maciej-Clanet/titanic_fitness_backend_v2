from pydantic import BaseModel
from typing import List, Dict


class AddWorkout(BaseModel):
    exercise_name: str
    date: str
    reps: int
    weight: float
    user_email: str


# Data that will be send to the endpoint
class GetDay(BaseModel):
    user_email: str
    date: str


class ExerciseEntry(BaseModel):
    reps: int
    weight: float


# Workout day contains a dictionary of exercises each having a list of exercise entries for logging
class WorkoutDay(BaseModel):
    exercises: Dict[str, List[ExerciseEntry]]


class Workouts(BaseModel):
    workouts: Dict[str, WorkoutDay]


class AddExercise(BaseModel):
    user_email: str
    date: str
    exercise_name: str
    reps: int
    weight: float
