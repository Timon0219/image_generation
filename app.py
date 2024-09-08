from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from image_generator import image_generator

app = FastAPI()

class Question(BaseModel):
    question: str


@app.post("/image")
async def img_generatiom(prompt: Question):
    response = image_generator(prompt)
    return {"image": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)