from fastapi import FastAPI
from pydantic import BaseModel


app=FastAPI()


todos=[]

class Todo(BaseModel):
    id:int
    title:str
    completed:bool


#create api
@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {"message":"Todo created successfully","data":todo}


#read api
@app.get("/todos")
def get_todos():
    return {"message":"Todos retrieved successfully","data":todos}

#read api by id
@app.get("/todos/{id}")
def get_todo_by_id(id:int):
    for todo in todos:
        if todo.id==id:
            return {"message":"Todo retrieved successfully","data":todo}
    return {"message":"Todo not found"}


#update api
@app.put("/todos/{id}")
def update_todo(todo_id:int,updated_todo:Todo):
    for index,todo in enumerate(todos):
        if todo.id==todo_id:
            todos[index]=updated_todo
            return {"message":"Todo updated successfully","data":updated_todo}
    return {"message":"Todo not found"}

#delete api
@app.delete("/todos/{id}")
def delete_todo(id:int):
    for index,todo in enumerate(todos):
        if todo.id==id:
            deleted_todo=todos.pop(index)
            return {"message":"Todo deleted successfully","data":deleted_todo}
    return {"message":"Todo not found"}

