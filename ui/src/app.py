import json
import os
import requests
from flask import Flask

app = Flask(__name__)
BASE_API_URL = f'http://{os.environ["API_URL"]}:8000'
BASE_HTML = '<link rel="shortcut icon" href="static/favicon.ico">'

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

@app.route("/")
def say_hello():
    return BASE_HTML + '<p>Hello there!</p>'
