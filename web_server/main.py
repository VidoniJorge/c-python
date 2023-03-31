# Python
from typing import Optional
from enum import Enum
# Pydantic
from pydantic import BaseModel, Field
# FastAPI
from fastapi import FastAPI, Body, Query, Path
from fastapi.responses import HTMLResponse

# Variable va a contener toda nuestra aplicación
app = FastAPI()


# Models
class HairColor(Enum):
    white = "White"
    brown = "Brown"
    black = "Black"
    blonde = "Blonde"
    red = "Red"

class Location(BaseModel):
    city: str = Field(..., min_length=1, max_length=50, example="Tigre")
    state: str = Field(..., min_length=1, max_length=50, example="Buenos aires")
    country: str = Field(..., min_length=1, max_length=50, example="Argentina")

class Person(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=50)
    last_name: str = Field(..., min_length=1, max_length=50)
    age: int = Field(..., gt=0, le=150)
    hair_color: Optional[HairColor] = Field(default=None) # definimos el valor por defecto por ser optional
    is_married: Optional[bool] = Field(default=None)

    class Config():
        schema_extra = {
            "example": {
                "first_name" : "facundo",
                "last_name" : "Martines",
                "age": 21,
                "haid_color" : "White",
                "is_married" : False 
            }
        } 

@app.get('/')
def home():
    return {
        "hello" : "world"
    }

@app.post("/person")
def create_person(person: Person = Body(...)):
    # ... el body es obligatorio
    return person

# Validaciones : query parameters
@app.get("/person/details")
def show_person_details(
    name: Optional[str] = Query(
        default=None,
        min_length=1, 
        max_length=50,
        title="Person Name",
        description="This is the person name. It's between 1 and 50 characters"
        ),
    age: Optional[str] = Query(
        ...,
        title="Person age",
        description="This is the person age. It's requiered"
        )
    ):
    return { name : age }

# Validaciones : path parameters
@app.get("/person/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person id",
        description="This is the person id. It's requiered"
        )
    ):
    return { person_id : "It exists!" }

# Validaciones : Request Body
@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person id",
        description="This is the person id. It's requiered"
        ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    result = person.dict()
    result.update(location.dict())
    return result

@app.get("/contact", response_class=HTMLResponse)
def contacts():
    return """
        <h1>Vidoni Jorge</h1>
    """

def run():
    pass

if __name__ == '__main__' :
    run()