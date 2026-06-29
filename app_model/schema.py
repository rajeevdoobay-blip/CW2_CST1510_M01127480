def create_user_table(connection):
    cursor = connection.cursor()
    sql = '''CREATE TABLE users (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    username      TEXT    NOT NULL UNIQUE,
    password_hash TEXT    NOT NULL,
    role          TEXT    DEFAULT 'user'
    );
    '''
    cursor.execute(sql)
    connection.commit()