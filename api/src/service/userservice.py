import uuid
import dao.account as dao


def get_accounts_for_user(user_id):
    return_dict = []
    accounts = dao.get_accounts_for_user(user_id)
    for account in accounts:
        return_dict.append({
            'account_no': account[0],
            'account_type': account[1],
            'account_balance': account[2]
        })

    return return_dict


def add_account_for_user(user, account_type):
    row_id = dao.add_account_for_user(user, str(uuid.uuid4())[:8], account_type)
    if not row_id:
        print('Error saving user')
    else:
        print(f'Account saved as record {row_id}')
