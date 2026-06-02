from fastapi import FastAPI,status,HTTPException


app = FastAPI()


@app.get("/create_user",status_code=status.HTTP_201_CREATED)
def create_user():
    return {"message": "User created successfully"}


#custom response status code
@app.get("/user")
def get_user():
    return {
        "message": "Success",
        "message": "User fetched successfully",
        "data": {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com" 

        }
        }   


#error handling with custom status code
@app.get("/user/{user_id}") 
def get_user_by_id(user_id: int):
    if user_id != 1:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return {
        "message": "Success",
        "message": "User fetched successfully",
        "data": {
            "id": 1,
            "name": "John Doe",
            "email": "john.doe@example.com" 
        }
    }