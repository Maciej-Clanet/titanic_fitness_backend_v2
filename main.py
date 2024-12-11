from fastapi import FastAPI
from routes.workouts_routes import workouts_router

app = FastAPI()

app.include_router(workouts_router, prefix="/workouts", tags=["Workouts"])


@app.get("/")
def get_test():

    return {"hello": "world"}
