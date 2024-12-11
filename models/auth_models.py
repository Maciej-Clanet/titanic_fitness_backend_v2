from pydantic import BaseModel


class LoginForm(BaseModel):
    email: str
    password: str


class SignInForm(BaseModel):
    email: str
    password: str
    display_name: str
