from astapi import FastAPI
from models import Developer, Project

app = FastAPI()
# Creating developer API with POST method
@app.post("/developers/")
def create_developer(developer: Developer):
    return {"message": "Developer created successfully", "developer": developer}

#Creating Projects API with POST method
@app.post("/projects/")
def create_project(project: Project):
    return{"message": "Project create successfully","Project": project}