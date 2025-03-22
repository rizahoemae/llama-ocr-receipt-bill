import ollama 
from pydantic import BaseModel
from typing import List
from datetime import date, datetime

class Item(BaseModel):
  name: str
  qty: int
  price: float
  
class Store(BaseModel):
  name: str
  address: str
  
class Bills(BaseModel):
  items: list[Item]
  store: Store
  date: date
  subtotal: float
  tax: float
  service_charge: float
  total: float


res = ollama.chat(model="llama3.2-vision", messages=[
        {
            "role": "user", 
            "content": "I want you to perform an ocr scan of this image i attach. Its a receipt bill. i want you to scan detail of items, service amount, tax etc and also the total i should pay. turn that into a json ", 
            "images": ["./receipt/bill.jpeg"],
        },
        ], 
                  format=Bills.model_json_schema()
                  )
content = Bills.model_validate_json(res.message.content)
print(content)