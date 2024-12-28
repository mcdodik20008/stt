from random import Random as r
from fastapi import FastAPI

app = FastAPI()
rnd = r()
value = rnd.randint(0, 100)

@app.get("/")
async def speech_to_text():
    print("база отработала")
    return f"Хорошо работаем братья {value}"

@app.get("/speech-to-text")
async def speech_to_text():
    print("база отработала2")
    return f"Я умный робот спич ту текст {value}"

@app.post("/speech-to-text")
async def speech_to_text():
    print("база отработала3")
    return f"Я умный робот спич ту текст {value}"


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
