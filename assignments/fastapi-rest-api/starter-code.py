from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="FastAPI REST API - Starter")


class Item(BaseModel):
    id: int | None = None
    name: str
    description: str | None = None


# in-memory storage
items: Dict[int, Item] = {}
next_id = 1


@app.post("/items", response_model=Item)
def create_item(item: Item):
    global next_id
    item.id = next_id
    items[next_id] = item
    next_id += 1
    return item


@app.get("/items", response_model=list[Item])
def list_items():
    return list(items.values())


@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[item_id]


@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    item.id = item_id
    items[item_id] = item
    return item


@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    del items[item_id]
    return {"detail": "deleted"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)
