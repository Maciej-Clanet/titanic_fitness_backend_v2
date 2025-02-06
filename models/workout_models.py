from pydantic import BaseModel
from typing import List, Dict

class AddWorkout(BaseModel):
    exercise_name : str
    date : str
    reps : int
    weight: float
    user_email : str


class GetDay(BaseModel):
    user_email: str
    date: str

class ExerciseEntry(BaseModel):
    reps: int
    weight: float

class WorkoutDay(BaseModel):
    exercises: Dict[str, List[ExerciseEntry] ] 


class Workouts(BaseModel):
    workouts: Dict[str, WorkoutDay]



class AddExercise(BaseModel): 
    user_email: str 
    date: str 
    exercise_name: str 
    reps: int 
    weight: float 