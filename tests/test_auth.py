# tests/test_auth.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from auth import login 

# Before Refactor
def test_login():
    assert login("user", "password") == True
    assert login("user", "wrong_password") == False



# After Refactor
def test_login():
    users = {"user": "password"}
    

    assert login("user", "password", users) == True
    

    assert login("user", "wrong_password", users) == False
    

    assert login("non_user", "password", users) == False

