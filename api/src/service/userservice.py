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
