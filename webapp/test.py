import unittest
from flask import current_app
import main

def setUp(self):
    self.app = main(config=['testing'])
    self.appctx = self.app.app_context()

def tearDown(self):
    self.app = None
    self.client = None

def test_login(self):
    data = {
        "password": "password"
    }
    response = self.client.post('/', data=data)
    print(response.status_code)
    assert response.status_code == 200