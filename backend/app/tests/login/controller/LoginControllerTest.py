import os, sys
from dotenv import load_dotenv
load_dotenv()
path = os.environ['FILE_PATH']
sys.path.append(path)

from typing import Dict
from testtools import TestCase
from fastapi.testclient import TestClient
from app.main import app as testingApp
from app.core.config import settings

class LoginControllerTest(TestCase):
    def setUp(self):
        self.client = TestClient(testingApp)
        self.superuser_token_headers: Dict[str, str]

    def test_get_access_token(self):
        login_data = {
            "username": settings.FRIST_SUPERUSER,
            "password": settings.FRIST_SUPERUSER_PASSWORD
        }
        r = self.client.post(f"{settings.API_V1_STR}/login/access-token", data=login_data)
        tokens = r.json()
        self.assertTrue(r.status_code, 200)
        self.assertTrue("access_token", tokens) # assert "access_token" in tokens
        self.assertTrue(tokens["access_token"], True)

    def test_use_access_token(self):
        r = self.client.post(f"{settings.API_V1_STR}/login/test-token", headers=self.superuser_token_headers)
        result = r.json()
        self.assertTrue(r.status_code, 200)
        self.assertTrue("email", result) # assert "email" in result

    def test_read_user_bad_token():
        pass

    def test_read_inexistent_user():
        pass

    def test_create_user():
        pass

    def test_create_user_bad_token():
        pass

    def test_create_existing_user():
        pass


