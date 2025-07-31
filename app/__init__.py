from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def get_root():
    return "it's work! even after auto deploy"