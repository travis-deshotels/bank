# API

## Docker
* Setup `bank.db`

* `docker build -t bank-api-img .`

* `docker run --name bankapi -p 8000:8000 -v "<local path>/bank.db:/app/data/bank.db" bank-api-img`
