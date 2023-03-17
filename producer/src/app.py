from fastapi import FastAPI, Body
from pydantic import BaseModel

from fastapidesc import description, contract

app = FastAPI(
    title='Message',
    description=description,
    contract=contract,
)

class Message(BaseModel):
    name: str
    message: str

@app.post("/message", tags=['producer'])
async def send_message(message: Message = Body(...)):
    return {"notification": f"You, {message.name}, succesfully sended the message: {message.message}"}
