# main.py

# ----------------------------
# Part 1: Understanding JSON
# ----------------------------

import json
import requests
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

print("\n--- PART 1: Understanding JSON ---")

# A sample JSON string
json_string = '''
{
    "name": "Alice",
    "age": 28,
    "city": "London"
}
'''

# Parse JSON string into Python dict
data = json.loads(json_string)
print(f"Name: {data['name']}, Age: {data['age']}, City: {data['city']}")

# Convert back to JSON
back_to_json = json.dumps(data, indent=2)
print("Converted back to JSON:\n", back_to_json)


# ----------------------------
# Part 2: Making an API Request
# ----------------------------

print("\n--- PART 2: Making an API Request ---")

# Public placeholder API
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

if response.status_code == 200:
    api_data = response.json()
    print("Fetched Post Title:", api_data['title'])
else:
    print("Failed to fetch data from API.")


# ----------------------------
# Part 3: Creating an API with FastAPI
# ----------------------------

print("\n--- PART 3: FastAPI Server Starting... ---")

# Create FastAPI app
app = FastAPI()

# Pydantic model for a Post
class Post(BaseModel):
    title: str
    content: str
    author: str

# In-memory "database"
posts_db = []

# Create a post
@app.post("/posts/", response_model=Post)
def create_post(post: Post):
    posts_db.append(post)
    return post

# Get all posts
@app.get("/posts/", response_model=List[Post])
def get_all_posts():
    return posts_db

# Get a single post by ID
@app.get("/posts/{post_id}", response_model=Post)
def get_post(post_id: int):
    if 0 <= post_id < len(posts_db):
        return posts_db[post_id]
    return {"error": "Post not found"}
