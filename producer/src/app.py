from fastapi import FastAPI, Body
from pydantic import BaseModel

from fastapidesc import description, contract

app = FastAPI(
    title='Message',
    description=description,
    contract=contract,
)


@app.post("/message", tags=['producer'])
async def send_message(name: str = Body(...), message: str = Body(...)):
    return {"notification": f"You, {name}, succesfully sended the message: {message}"}
