# Bank

Not a real bank app. Python based.

## Stack is
* SQLITE
* sqlite3 (DAO)
* fastapi (API)
* front
  * flask (web UI)
  * Python script

---

## Docker
* Setup database by running `db/bank.sql`
* Run `docker network create py-net` to create a user-defined bridge network

### API
* Build `docker build -t bank-api-img .` (in API directory)
* Run `docker run --net py-net --name bankapi -p 8000:8000 -v "<local path>/bank.db:/app/data/bank.db" bank-api-img`

### UI
* Build `docker build -t pythonui .` (in UI directory)
* Run `docker run --net py-net --name myui -p 5000:5000 --env API_URL=bankapi pythonui`

Visit `localhost:5000` and verify the UI is working.
