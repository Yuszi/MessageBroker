from fastapi import FastAPI, Body
from pydantic import BaseModel
from backend_func import producerKafkaSend
from enum import Enum

from fastapidesc import description, contract

app = FastAPI(
    title='Producer',
    description=description,
    contract=contract,
)

class Topic(str, Enum):
    hw = 'hw'
    sw = 'sw'

@app.post("/message", tags=['producer'])
async def send_message(message: str, topic: Topic):
    producerKafkaSend(topic=topic, message=message)
    return {"notification": f"You succesfully sended the message: {message} for the topic {topic}"}
