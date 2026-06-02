from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class User(BaseModel):
    name: str
    age: int
  

@app.post("/create_user")
def create_user(name: str, age: int):
    return {"message":f"User {name} created with age {age}"}

#real world example
@app.post("/create_users")
def create_users(User: User):
    return {
        "data":User
        }