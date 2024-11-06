# tests/test_mock.py
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


from mock import login 

from unittest.mock import Mock

def test_login_with_mock():
    mock_database = Mock()
    mock_database.find_user.return_value = {"username": "user", "password": "password"}
    assert login("user", "password", mock_database) == True
    assert login("user", "wrong_password", mock_database) == False
