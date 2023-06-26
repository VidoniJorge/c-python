# Python
from typing import Optional
from enum import Enum
# Pydantic
from pydantic import BaseModel, Field, EmailStr
# FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path, Form, Cookie, Header, File, UploadFile
from fastapi import HTTPException 
from fastapi.responses import HTMLResponse
from fastapi import status

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
                "is_married" : False,
                "password" : "string12" 
            }
        } 

class PersonRequest(Person):
    password: str = Field(..., min_length=8)

class PersonResponse(Person):
    pass

class LoginResponse(BaseModel):
    username: str = Field(..., max_length=20, example="miguelk2020")

@app.get(path='/', status_code=status.HTTP_200_OK)
def home():
    return {
        "hello" : "world"
    }

@app.post(
        path="/person",
        status_code=status.HTTP_201_CREATED, 
        response_model=PersonResponse, 
        tags=["person"], 
        summary="Create person in the app"
        )
def create_person(person: PersonRequest = Body(...)):
    # ... el body es obligatorio
    # Docstring
    """
        Create Person

        This path operation creates a person in the app and save the information in the database

        Parameters:
        - Request body parameter:
            - **person: Person** -> A person model with first name, last name, age hair color and marital status
        
        Returns a person model with first name, last name, age hair color and marital status
    """
    return person

# Validaciones : query parameters
@app.get(path="/person/details", status_code=status.HTTP_200_OK, tags=["person"], deprecated=True)
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
persons = [1,2,3,4]
@app.get("/person/{person_id}", tags=["person"])
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person id",
        description="This is the person id. It's requiered"
        )
    ):
    if person_id not in persons:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="This person doesn't exist")
    
    return { person_id : "It exists!" }

# Validaciones : Request Body

@app.put("/person/{person_id}", tags=["person"])
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

@app.get("/contact", response_class=HTMLResponse, tags=["contact"])
def contacts():
    return """
        <h1>Vidoni Jorge</h1>
    """

# formulario
@app.post(path="/login", response_model=LoginResponse, status_code=status.HTTP_200_OK, tags=["person"])
def login(username: str = Form(...), password: str = Form(...)):
    return LoginResponse(username=username)

@app.post(path="/contact", status_code=status.HTTP_200_OK, tags=["contact"])
def contact(
    firstname: str = Form(..., max_length=20, min_length=1),
    lastname: str = Form(..., max_length=20, min_length=1),
    email: EmailStr = Form(...),
    message: str = Form(..., min_length=20),
    user_agent: Optional[str] = Header(default=None),
    ads: Optional[str] = Cookie(default=None)
):
    return user_agent


@app.post(path="/post-image")
def post_image(image: UploadFile = File(...)):
    return {
        "filename": image.filename,
        "format" : image.content_type,
        "size": len(image.file.read())
    }

def run():
    pass

if __name__ == '__main__' :
    run()