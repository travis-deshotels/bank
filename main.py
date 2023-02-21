import service.userservice as service
from fastapi import FastAPI, Depends

app = FastAPI()


@app.get("/")
def read_root():
    return {
        "/accounts/{userid}": "List accounts for a user."
    }


@app.post("/accounts/{user_id}")
async def get_accounts_for_user(user_id: str, encrypted_key: bytes = Depends(service.parse_body)):
    return service.get_accounts_for_user(user_id, encrypted_key)
