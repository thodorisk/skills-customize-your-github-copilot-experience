from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    price: float
    description: Optional[str] = None

class ItemCreate(BaseModel):
    name: str
    price: float
    description: Optional[str] = None

items = [
    Item(id=1, name="Laptop", price=999.99, description="Portable computer"),
    Item(id=2, name="Headphones", price=59.99, description="Noise-canceling headphones"),
    Item(id=3, name="Notebook", price=4.99, description="Spiral notebook for notes"),
]

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI item store!"}

@app.get("/items", response_model=List[Item])
def list_items(search: Optional[str] = None, max_price: Optional[float] = None):
    results = items
    if search:
        results = [item for item in results if search.lower() in item.name.lower()]
    if max_price is not None:
        results = [item for item in results if item.price <= max_price]
    return results

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/items", response_model=Item, status_code=201)
def create_item(item_data: ItemCreate):
    next_id = max(item.id for item in items) + 1 if items else 1
    new_item = Item(id=next_id, **item_data.dict())
    items.append(new_item)
    return new_item

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item_data: ItemCreate):
    for index, item in enumerate(items):
        if item.id == item_id:
            updated_item = Item(id=item_id, **item_data.dict())
            items[index] = updated_item
            return updated_item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, item in enumerate(items):
        if item.id == item_id:
            items.pop(index)
            return {"message": "Item deleted successfully"}
    raise HTTPException(status_code=404, detail="Item not found")
