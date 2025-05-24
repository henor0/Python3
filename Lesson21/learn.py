from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/items")
def read_items():
    return {"items": ["item1", "item2", "item3"]}