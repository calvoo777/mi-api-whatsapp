from fastapi import FastAPI
from pydantic import BaseModel
from twilio.rest import Client
import os

app = FastAPI()

# ❌ Nada de datos escritos a mano
# ✅ Los leemos de variables de entorno (Render)

TWILIO_SID = os.environ.get("TWILIO_SID")
TWILIO_TOKEN = os.environ.get("TWILIO_TOKEN")
TWILIO_NUMBER = os.environ.get("TWILIO_NUMBER")   # tu número sandbox de Twilio: whatsapp:+1415...
DESTINO = os.environ.get("DESTINO")               # tu número personal: whatsapp:+34...

client = Client(TWILIO_SID, TWILIO_TOKEN)

class Notificacion(BaseModel):
    mensaje: str

@app.post("/enviar")
def enviar_mensaje(data: Notificacion):
    msg = client.messages.create(
        body=data.mensaje,
        from_=TWILIO_NUMBER,
        to=DESTINO
    )
    return {"status": "ok", "sid": msg.sid}
