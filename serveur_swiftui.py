from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class CanData(BaseModel):
    can_id: str
    valeur: str
    timestamp: Optional[float] = None

@app.get("/")
def read_root():
    return {"status": "Online", "message": "En attente de données CAN"}

@app.post("/debug-can")
def receive_data(data: CanData):
    # Ce print s'affichera dans les "Logs" sur Render
    print(f"--- NOUVELLE DONNÉE CAN ---")
    print(f"ID: {data.can_id} | Valeur: {data.valeur}")
    return {"status": "success", "received": data.can_id}
