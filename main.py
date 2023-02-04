from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/signin")
async def say_hello():
    return {""}

@app.post("/signup")
async def say_hello(name: str):
    return {""}

@app.get("/users")
async def say_hello(name: str):
    return {""}

@app.delete("/user/{user_id}")
async def say_hello(name: str):
    return {""}


#Forums

@app.get("/forums")
async def say_hello(name: str):
    return {""}

@app.get("/general_discussion")
async def say_hello(name: str):
    return {""}

@app.get("/lore")
async def say_hello(name: str):
    return {""}

@app.get("/co-op")
async def say_hello(name: str):
    return {""}


#Threads
@app.post("/thread")
async def say_hello(name: str):
    return {""}

@app.get("/thread")
async def say_hello(name: str):
    return {""}

@app.get("/threads")
async def say_hello(name: str):
    return {""}

#Comments
@app.post("/thread")
async def say_hello(name: str):
    return {""}

@app.get("/thread")
async def say_hello(name: str):
    return {""}

@app.get("/threads")
async def say_hello(name: str):
    return {""}