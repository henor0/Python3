from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()



def get_fullname(first_name: str, last_name: str) -> str:
    full_name = first_name.title() + " " + last_name.title()
    return full_name



class Person(BaseModel):
    first_name: str
    last_name: str
    age: Optional[int] = None


people_db: List[Person] = []



# GET all people
@app.get("/people/", response_model=List[Person])
def get_all_people():
    return people_db


@app.get("/people/{person_id}")
def get_person(person_id: int):
    if 0 <= person_id < len(people_db):
        person = people_db[person_id]
        return {
            "full_name": get_fullname(person.first_name, person.last_name),
            "age": person.age
        }
    raise HTTPException(status_code=404, detail="Person not found")


@app.post("/people/")
def create_person(person: Person):
    people_db.append(person)
    return {
        "message": "Person added!",
        "full_name": get_fullname(person.first_name, person.last_name)
    }


@app.put("/people/{person_id}")
def update_person(person_id: int, updated_person: Person):
    if 0 <= person_id < len(people_db):
        people_db[person_id] = updated_person
        return {
            "message": "Person updated!",
            "full_name": get_fullname(updated_person.first_name, updated_person.last_name)
        }
    raise HTTPException(status_code=404, detail="Person not found")


@app.delete("/people/{person_id}")
def delete_person(person_id: int):
    if 0 <= person_id < len(people_db):
        removed = people_db.pop(person_id)
        return {
            "message": f"{get_fullname(removed.first_name, removed.last_name)} deleted"
        }
    raise HTTPException(status_code=404, detail="Person not found")
