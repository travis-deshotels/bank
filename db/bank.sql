--pragma foreign_keys = ON;

CREATE TABLE bank_account_types(
    ID integer primary key autoincrement,
    ACCOUNT_TYPE_NAME varchar(12) unique
)

CREATE TABLE bank_user(
    ID integer primary key autoincrement,
    USERNAME varchar(12) unique,
    PASSWORD varchar(12)
);


CREATE TABLE bank_account(
    ID integer primary key autoincrement,
    ACCOUNTNO varchar(12) unique not null,
    ACCOUNTTYPE integer not null,
    BALANCE bigint not null,
    ACCOUNTLORD integer not null,
    foreign key (ACCOUNTLORD)
        references bank_user(ID),
    foreign key (ACCOUNTTYPE)
        references bank_account_types(ID)
);

INSERT INTO bank_account_types(ACCOUNT_TYPE_NAME) VALUES('checking');
INSERT INTO bank_account_types(ACCOUNT_TYPE_NAME) VALUES('savings');
COMMIT;
INSERT INTO bank_user(USERNAME, PASSWORD) VALUES('tnd', 'tnd');
COMMIT;
SELECT ID FROM bank_account_types WHERE ACCOUNT_TYPE_NAME = 'checking';
SELECT ID FROM bank_user WHERE USERNAME = 'tnd';
INSERT INTO bank_account(ACCOUNTNO, BALANCE, ACCOUNTLORD, ACCOUNTTYPE) VALUES('1234567890', 0,
    (SELECT ID FROM bank_user WHERE USERNAME = 'tnd'),
    (SELECT ID FROM bank_account_types WHERE ACCOUNT_TYPE_NAME = 'checking')
    );
COMMIT;