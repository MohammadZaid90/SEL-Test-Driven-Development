# src/auth.py

# Before Refactor
def login(username, password):
    return username == "user" and password == "password"
 
 
 
# After Refactor
def login(username, password, users):
    return users.get(username) == password

