from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def say_hello():
    return{"greetings":"Hello Wolrd"}

@app.get("/items/{item_id}")
async def get_items(item_id: int, count: int = 1):
    return {"fetch": f"Fetched {count} of {item_id}"}