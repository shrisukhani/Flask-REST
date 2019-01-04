from user import User

users = [
    User(1, 'bob', 'asdf'),
    User(2, 'dylan', 'ghjk'),
    User(3, 'shri', 'sukhani')
]

username_to_user = {u.username: u for u in users}
userid_to_user = {u.id: u for u in users}


def authorize(username, password):
    user = username_to_user[username]
    if user and user.password == password:
        return user
    return None


def identity(payload):
    user_id = payload['identity']
    return userid_to_user.get(user_id, None)
