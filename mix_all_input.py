from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

user=[]

class User(BaseModel):
    name:str
    age=int


@app.post("/user")
def create_user(user:User):
    user.append(user)
    return user


#put method
@app.put("/user/{user_id}")
def update_user(user_id:int,user:User,notify:bool=False):
    for i in range(len(user)):
        if user[i].id==user_id:
            user[i]=user
            return user[i]
    return {"message":"User not found"}