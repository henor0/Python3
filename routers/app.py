import streamlit as st
import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")

# ----- API client functions -----

def get_categories():
    try:
        response = requests.get(f"{API_BASE_URL}/categories/")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Failed to fetch categories: {e}")
        return []

def get_recipes(cuisine=None, difficulty=None):
    params = {}
    if cuisine:
        params['cuisine'] = cuisine
    if difficulty:
        params['difficulty'] = difficulty

    try:
        response = requests.get(f"{API_BASE_URL}/recipes/", params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Failed to fetch recipes: {e}")
        return []

def create_category(category_name):
    try:
        response = requests.post(f"{API_BASE_URL}/categories/", json={"name": category_name})
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Failed to create category: {e}")
        return None

def create_recipe(recipe_data: dict):
    try:
        response = requests.post(f"{API_BASE_URL}/recipes/", json=recipe_data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        st.error(f"Failed to create recipe: {e}")
        return None

# ----- Streamlit UI -----
st.title("Recipe Manager")

menu = st.sidebar.selectbox("Menu", ["View Categories", "View Recipes", "Add Category", "Add Recipe"])

if menu == "View Categories":
    categories = get_categories()
    if categories:
        df = pd.DataFrame(categories)
        st.dataframe(df)
    else:
        st.write("No categories found.")

elif menu == "View Recipes":
    cuisine_filter = st.text_input("Filter by cuisine (optional):")
    difficulty_filter = st.text_input("Filter by difficulty (optional):")
    recipes = get_recipes(cuisine=cuisine_filter or None, difficulty=difficulty_filter or None)
    if recipes:
        df = pd.DataFrame(recipes)
        st.dataframe(df)
    else:
        st.write("No recipes found.")

elif menu == "Add Category":
    new_cat = st.text_input("New category name:")
    if st.button("Create Category"):
        if new_cat.strip():
            result = create_category(new_cat.strip())
            if result:
                st.success(f"Category '{new_cat}' created successfully!")
        else:
            st.warning("Please enter a category name.")

elif menu == "Add Recipe":
    # Fetch categories for dropdown
    categories = get_categories()
    category_options = {cat['name']: cat['id'] for cat in categories} if categories else {}

    with st.form("recipe_form"):
        name = st.text_input("Recipe name:")
        description = st.text_area("Description:")
        ingredients = st.text_area("Ingredients (comma-separated):")
        instruction = st.text_area("Instruction:")
        cuisine = st.text_input("Cuisine:")
        difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])
        category_name = st.selectbox("Category", list(category_options.keys()) or ["No categories found"])

        submitted = st.form_submit_button("Create Recipe")

        if submitted:
            if not name or not description or not ingredients or not instruction or not cuisine:
                st.warning("Please fill in all required fields.")
            elif category_name == "No categories found":
                st.error("No categories available. Please add a category first.")
            else:
                recipe_data = {
                    "name": name,
                    "description": description,
                    "ingredients": ingredients,
                    "instruction": instruction,
                    "cuisine": cuisine,
                    "difficulty": difficulty,
                    "category_id": category_options[category_name]
                }
                result = create_recipe(recipe_data)
                if result:
                    st.success(f"Recipe '{name}' created successfully!")

