from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    quantity: str

class Order(BaseModel):
    name: str
    quantity: str
    price: float

data = {
    1: {
        "name": "a",
        "price": 100,
        "quantity": "normal"
    },
    2: {
        "name": "b",
        "price": 200,
        "quantity": "good"
    },
    3: {
        "name": "c",
        "price": 50,
        "quantity": "bad"
    },
    4: {
        "name": "d",
        "price": 300,
        "quantity": "good"
    }
}

cus = {}

@app.get('/')
def getItems():
    return data

@app.get('/{id}')
def getItems(id: int):
    return data[id]

@app.post('/{id}')
def addItems(id: int, item : Item):
    data[id] = item
    return data[id]

@app.put('/{id}')
def updateItem(id: int, item : Item):
    data[id].update(item)
    return data[id]

@app.delete('/{id}')
def deleteItem(id: int):
    del data[id]

@app.get('/12')
def getOrder():
    return cus


@app.get('/{order_id}')
def getOrder(order_id: int):
    return cus[order_id]

@app.post('/{order_id}')
def createOrder(order_id: int, order: Order):
    cus[order_id] = order
    return cus[order_id]