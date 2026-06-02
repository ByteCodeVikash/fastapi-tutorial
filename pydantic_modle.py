from fastapi import FastAPI
from pydantic import BaseModel


app=FastAPI()

class User(BaseModel):
    name:str
    age:int
    email:str


@app.post("/create_user")
def create_user(User: User):
    return {"message":f"User {User.name} created with age {User.age} and email {User.email}"}   



#nested_model
class Address(BaseModel):
    street:str
    city:str
    state:str
    zip_code:str        

class UserWithAddress(BaseModel):
    name:str
    age:int
    email:str
    address:Address     

@app.post("/create_user_with_address")
def create_user_with_address(user:UserWithAddress):
    return {"message":f"User {user.name} created with age {user.age}, email {user.email} and address {user.address.street}, {user.address.city}, {user.address.state} {user.address.zip_code}"} 