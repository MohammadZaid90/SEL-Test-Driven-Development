def login(username, password, database):
    user = database.find_user(username)
    return user and user["password"] == password
