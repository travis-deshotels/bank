import json
import requests
import rsa


BASE_API_URL = 'http://localhost:8000'


def view_accounts(user, password):
    message = f"{user} {password}"
    with open("../key/public.pem") as f:
        public_key = rsa.PublicKey.load_pkcs1(f.read())
    encrypted_message = rsa.encrypt(message.encode(), public_key)
    response_data = requests.post(url=f'{BASE_API_URL}/accounts/{user}', data=encrypted_message)
    accounts = json.loads(response_data.text)
    for account in accounts:
        print(account['account_no'])
        print(account['account_type'])
        print(account['account_balance'])


if __name__ == '__main__':
    user_given = input('Input username: ')
    password_given = input('Input password: ')
    view_accounts(user_given, password_given)
