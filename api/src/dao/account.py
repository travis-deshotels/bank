import sqlite3

SQLITE_DB = '/app/data/bank.db'


def get_accounts_for_user(user):
    conn = None
    cur = None
    try:
        query = "SELECT a.ACCOUNTNO, t.ACCOUNT_TYPE_NAME, a.BALANCE FROM bank_account a INNER JOIN bank_account_types " \
                "t ON a.ACCOUNTTYPE = t.ID INNER JOIN bank_user u ON a.ACCOUNTLORD = u.ID WHERE u.USERNAME = ?;"
        conn = sqlite3.connect(SQLITE_DB)
        cur = conn.cursor()
        cur.execute(query, (user,))
        return cur.fetchall()
    except Exception as e:
        print(e)
        return []
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
