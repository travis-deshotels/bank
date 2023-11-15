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


def add_account_for_user(user, account_no, account_type):
    conn = None
    cur = None
    try:
        query = "INSERT INTO bank_account(ACCOUNTNO, BALANCE, ACCOUNTLORD, ACCOUNTTYPE) VALUES(?, 0," \
                "(SELECT ID FROM bank_user WHERE USERNAME = ?)," \
                "(SELECT ID FROM bank_account_types WHERE ACCOUNT_TYPE_NAME = ?));"
        conn = sqlite3.connect(SQLITE_DB)
        cur = conn.cursor()
        cur.execute(query, (account_no, user, account_type))
        conn.commit()
        return cur.lastrowid
    except Exception as e:
        print(e)
        return 0
    finally:
        if cur is not None:
            cur.close()
        if conn is not None:
            conn.close()
