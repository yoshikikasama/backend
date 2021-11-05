import hashlib
import os
import base64


print(hashlib.sha256(b'password').hexdigest())

user_name = 'user1'
user_pass = 'password'
db = {}

salt = base64.b64encode(os.urandom(32))
print(salt)


# def get_digest(password):
#     password = bytes(user_pass, 'utf-8')
#     digest = hashlib.sha256(salt + password).hexdigest()
#     for _ in range(10000):
#         digest = hashlib.sha256(bytes(digest, 'utf-8')).hexdigest()
#     print('check:', digest)
#     return digest

digest = hashlib.pbkdf2_hmac(
    'sha256', bytes(user_pass, 'utf-8'), salt, 100000
)

db[user_name] = digest

# db[user_name] = get_digest(user_pass)


def is_login(user_name, password):
    digest = hashlib.pbkdf2_hmac(
        'sha256', bytes(password, 'utf-8'), salt, 100000
    )
    return digest == db[user_name]
    # return get_digest(password) == db[user_name]


print(is_login(user_name, user_pass))  
print(db)
