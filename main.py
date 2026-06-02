from fastapi import FastAPI


app=FastAPI( )

#home route
@app.get("/")
def home():
    return {"message":"Welcome to FastAPI"}


#about route
@app.get("/about")
def about():
    return {"message":"This is the about page of FastAPI"}

# user route

@app.get("/user/{user_id}")
def get_user(user_id):
    return {user_id:user_id}

#user route datatype
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"message":f"user id is {user_id}"}

#query parameter
@app.get("/query")
def query_params(name):
    return {"message":f"Hello {name}"}


#optional query parameter
@app.get("/optional_query")
def optional_query_params(name=None):  
    if name:
        return {"message":f"Hello {name}"}
    else:
        return {"message":"Hello World"}
    
#default query parameter
@app.get("/default_query")
def default_query_params(name="World"):
    return {"message":f"Hello {name}"}

#multiple query parameters
@app.get("/multiple_query")
def multiple_query_params(name="World", age=None):
    return {"message":f"Hello {name}, you are {age} years old"} 






