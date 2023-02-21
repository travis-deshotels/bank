import dao.account as dao
from fastapi import Request
import rsa


def get_accounts_for_user(user_id: str, key: bytes):
    return_dict = []
    with open('key/private.pem', 'rb') as f:
        private_key = rsa.PrivateKey.load_pkcs1(f.read())
    clear_message = rsa.decrypt(key, private_key).decode()
    creds = clear_message.split(' ')
    accounts = dao.get_accounts_for_user(creds[0], creds[1])
    for account in accounts:
        return_dict.append({
            'account_no': account[0],
            'account_type': account[1],
            'account_balance': account[2]
        })

    return return_dict


async def parse_body(request: Request):
    data: bytes = await request.body()
    return data
