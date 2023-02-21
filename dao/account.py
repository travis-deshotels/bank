import sqlite3

SQLITE_DB = 'D:/pythonprojects/bank/sqlite'


def get_accounts_for_user(user, password):
    conn = None
    cur = None
    try:
        query = "SELECT a.ACCOUNTNO, t.ACCOUNT_TYPE_NAME, a.BALANCE FROM bank_account a INNER JOIN bank_account_types " \
                "t ON a.ACCOUNTTYPE = t.ID INNER JOIN bank_user u ON a.ACCOUNTLORD = u.ID WHERE u.USERNAME = ? " \
                "AND u.PASSWORD = ?;"
        conn = sqlite3.connect(SQLITE_DB)
        cur = conn.cursor()
        cur.execute(query, (user, password))
        return cur.fetchall()
    except Exception as e:
        print(e)
        return []
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
