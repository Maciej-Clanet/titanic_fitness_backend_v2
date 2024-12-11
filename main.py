from fastapi import FastAPI
from routes.workouts_routes import workouts_router
from routes.auth_routes import auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(workouts_router, prefix="/workouts", tags=["Workouts"])
app.include_router(auth_router, prefix="/auth", tags=["Auth"])


@app.get("/")
def get_test():

    return {"hello": "world"}
