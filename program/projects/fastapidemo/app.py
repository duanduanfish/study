from fastapi import FastAPI, HTTPException
from fastapi import Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel

app = FastAPI()

basic : HTTPBasicCredentials = HTTPBasic()


secret_username = "duanduan"
secret_password = "ds"

class Item(BaseModel):
	name: str
	path: str
	price: float

@app.get("/")
def read_root():
	return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
	return {"item_id": item_id, "q": q}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
	return {"item_name": item.name, "item_id": item_id}

# if you want to use path parameter, you need to add a path:path parameter to the decorator
@app.get("/items/path/{path:path}")
def read_path(path: str):
	return {"path": path}

@app.get("/who")
def get_user(creds : HTTPBasicCredentials = Depends(basic)):
	if creds.username == secret_username and creds.password == secret_password:
		return {'username': creds.username, 'password': creds.password}
	raise HTTPException(status_code=401, detail="invalid user")
