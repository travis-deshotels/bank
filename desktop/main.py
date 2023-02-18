import json
import requests

BASE_API_URL = 'http://localhost:8000'


def view_accounts(user):
    response_data = requests.get(f'{BASE_API_URL}/accounts/{user}')
    accounts = json.loads(response_data.text)
    for account in accounts:
        print(account['account_no'])
        print(account['account_type'])
        print(account['account_balance'])


if __name__ == '__main__':
    user_given = input('Input username: ')
    view_accounts(user_given)
