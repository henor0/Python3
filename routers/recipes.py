from fastapi import FastAPI, APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List, Optional
import sqlite3

app = FastAPI()
router = APIRouter()

# ---------- Database helpers ----------
def get_db_connection():
    conn = sqlite3.connect("recipes.db")  # Make sure this DB exists or create one
    conn.row_factory = sqlite3.Row
    return conn

def category_exists(category_id: int) -> bool:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM categories WHERE id = ?", (category_id,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

def recipe_exists(recipe_id: int) -> bool:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM recipes WHERE id = ?", (recipe_id,))
    exists = cursor.fetchone() is not None
    conn.close()
    return exists

# ---------- Pydantic models ----------
class RecipeBase(BaseModel):
    name: str
    description: str
    ingredients: str
    instruction: str
    cuisine: str
    difficulty: str
    category_id: int

class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int

    class Config:
        orm_mode = True

# ---------- Route helpers ----------
def map_row_to_recipe(row) -> Recipe:
    return Recipe(
        id=row["id"],
        name=row["name"],
        description=row["description"],
        ingredients=row["ingredients"],
        instruction=row["instruction"],
        cuisine=row["cuisine"],
        difficulty=row["difficulty"],
        category_id=row["category_id"]
    )

# ---------- Routes ----------
@router.get("/recipes", response_model=List[Recipe])
def get_recipes(
    cuisine: Optional[str] = Query(None, description="Filter by cuisine"),
    difficulty: Optional[str] = Query(None, description="Filter by difficulty")
):
    conn = get_db_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM reci*
