import json
import requests
from flask import Flask

app = Flask(__name__)
BASE_API_URL = 'http://localhost:8000'


@app.route("/<user>")
def view_accounts(user):
    response = ""
    response_data = requests.get(f'{BASE_API_URL}/accounts/{user}')
    accounts = json.loads(response_data.text)
    for account in accounts:
        response += f"<p>{account['account_no']}</p> \
                      <p>{account['account_type']}</p> \
                      <p>{account['account_balance']}</p>"

    return response
