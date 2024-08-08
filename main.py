from fastapi import FastAPI

app = FastAPI()


@app.get("/path/{item_id}")
async def root(item_id: int):
    
    return {'id': 0 if item_id == 1 else item_id}