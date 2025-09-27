from fastapi import FastAPI, HTTPException
from typing import List
from pydantic import BaseModel
import database  # Placeholder for your actual DB logic
import models    # Placeholder for your actual ORM models

from models import Movie, MovieCreate

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Movies CRUD API"}

# Create a new movie
@app.post("/movies/", response_model=Movie)
def create_movie(movie: MovieCreate):
    new_movie = database.create_movie(movie)  # Assuming this saves to DB and returns the new movie
    return new_movie

# Read all movies
@app.get("/movies", response_model=List[Movie])
def read_movies():
    return database.read_movies()

# Read a specific movie by ID
@app.get("/movies/{movie_id}", response_model=Movie)
def read_movie(movie_id: int):
    movie = database.read_movie(movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

# Update a movie
@app.put("/movies/{movie_id}", response_model=Movie)
def update_movie(movie_id: int, movie_data: MovieCreate):
    updated_movie = database.update_movie(movie_id, movie_data)
    if updated_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return updated_movie

# Delete a movie
@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    success = database.delete_movie(movie_id)
    if not success:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": f"Movie with ID {movie_id} deleted successfully"}

from fastapi import FastAPI, HTTPException, Query, Depends, Header
from typing import List
from enum import Enum
from pydantic import BaseModel
import database

app = FastAPI(title="Movies CRUD API", version="1.0")

# --- Security ---
API_KEY = "mysecretapikey"

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")


# --- Genre Enum ---
class Genre(str, Enum):
    action = "Action"
    comedy = "Comedy"
    drama = "Drama"
    horror = "Horror"
    sci_fi = "Sci-Fi"
    thriller = "Thriller"

# --- Nested Models ---
class Review(BaseModel):
    reviewer: str
    comment: str
    rating: float  # 0.0 - 5.0

# --- Movie Models ---
class MovieBase(BaseModel):
    title: str
    director: str
    year: int
    genre: Genre
    reviews: List[Review] = []

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int

    class Config:
        orm_mode = True

# --- Root Route ---
@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Welcome to the Movies CRUD API"}

# --- Create Movie ---
@app.post("/movies/", response_model=Movie, tags=["Movies"], dependencies=[Depends(verify_api_key)])
def create_movie(movie: MovieCreate):
    return database.create_movie(movie)

# --- Read All Movies with Pagination ---
@app.get("/movies", response_model=List[Movie], tags=["Movies"])
def read_movies(skip: int = 0, limit: int = 10):
    return database.read_movies(skip=skip, limit=limit)

# --- Read Single Movie ---
@app.get("/movies/{movie_id}", response_model=Movie, tags=["Movies"])
def read_movie(movie_id: int):
    movie = database.read_movie(movie_id)
    if movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie

# --- Update Movie ---
@app.put("/movies/{movie_id}", response_model=Movie, tags=["Movies"], dependencies=[Depends(verify_api_key)])
def update_movie(movie_id: int, movie_data: MovieCreate):
    updated_movie = database.update_movie(movie_id, movie_data)
    if updated_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return updated_movie

# --- Delete Movie ---
@app.delete("/movies/{movie_id}", tags=["Movies"], dependencies=[Depends(verify_api_key)])
def delete_movie(movie_id: int):
    success = database.delete_movie(movie_id)
    if not success:
        raise HTTPException(status_code=404, detail="Movie not found")
    return {"message": f"Movie with ID {movie_id} deleted successfully"}

# --- Search Movies ---
@app.get("/movies/search", response_model=List[Movie], tags=["Search"])
def search_movies(query: str = Query(..., min_length=1)):
    return database.search_movies(query)

# --- List All Genres ---
@app.get("/genres", tags=["Genres"])
def list_genres():
    return [genre.value for genre in Genre]
