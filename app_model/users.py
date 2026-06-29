

def add_user(connection, name, hash, role):
    cursor = connection.cursor()
    sql = '''INSERT INTO users (username, password_hash, role)  VALUES (?, ?, ?)'''
    param = (name, hash, role)
    cursor.execute(sql, param)
    connection.commit()


def migrate_users(connection):
    with open('DATA/users.txt', 'r') as f:
        users = f.readlines()

        for user in users:
            name, hash, role = user.strip().split(',')
            add_user(connection, name, hash, role)


def get_all_users(connection):
    cursor = connection.cursor()
    sql = '''SELECT * FROM users'''
    cursor.execute(sql)
    users = cursor.fetchall()
    connection.close()
    return users


def get_user(connection, name):
    cursor = connection.cursor()
    sql = '''SELECT * FROM users WHERE username = ?'''
    param = (name,)
    cursor.execute(sql, param)
    user = cursor.fetchone()
    connection.close()
    return user 


def update_user(connection, old_name, new_name):
    cursor = connection.cursor()
    sql   = '''UPDATE users SET username = ? WHERE username = ?'''
    param = (new_name, old_name)   
    cursor.execute(sql, param)
    connection.commit()


def delete_user(connection, user_name):
    cursor = connection.cursor()
    sql   = '''DELETE FROM users WHERE username = ?'''
    param = (user_name,)   
    cursor.execute(sql, param)   
    connection.commit()