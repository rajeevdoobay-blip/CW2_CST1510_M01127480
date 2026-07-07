import bcrypt

# hash password using bcrypt
def generate_hash(pwd):
    byte_pwd = pwd.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(byte_pwd, salt)
    return hash.decode('utf-8')

# validating the hash vs password 
def is_valid_hash(pwd, hash):
    hash_ =  hash.encode('utf-8')
    byte_pwd = pwd.encode('utf-8')
    is_valid = bcrypt.checkpw(byte_pwd, hash_)
    return is_valid 