import service.userservice as service
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    user: str
    accountType: str


@app.get("/")
def read_root():
    return {
        "/accounts/{userid}": "List accounts for a user."
    }


@app.get("/accounts/{user_id}")
def get_accounts_for_user(user_id):
    return service.get_accounts_for_user(user_id)


@app.post("/accounts")
def add_account_for_user(item: Item):
    service.add_account_for_user(item.user, item.accountType)
    return {"message": "ok"}
