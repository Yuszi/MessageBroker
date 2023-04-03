from fastapi import FastAPI
from pydantic import BaseModel
from backend_func import producerKafkaSend

from fastapidesc import description, contract

"""
    Einrichtung von FastAPI als benutzerfreundiches Interface für den Client.
    Ebenfalls ist eine POST-Methode möglich mit dem man eine Notifikation 
    zurückbekommt.
"""

# Einrichtung von FastAPI mit paar Beschreibungen
app = FastAPI(
    title='Producer',
    description=description,
    contract=contract,
)

# Einrichtung von POST-Methode in SwaggerUI
@app.post("/message", tags=['producer'])
async def send_message(message: str):
    # Versenden der Nachricht an die Funktion
    producerKafkaSend(message=message)

    # Benachrichtigung mit dem Inhalt der Nachricht, dass die Nachricht auch versendet wurde.
    return {"notification": f"You succesfully sended the message: {message}"}
