import service.userservice as service
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "/accounts/{userid}": "List accounts for a user."
    }


@app.get("/accounts/{user_id}")
def get_accounts_for_user(user_id):
    return service.get_accounts_for_user(user_id)
