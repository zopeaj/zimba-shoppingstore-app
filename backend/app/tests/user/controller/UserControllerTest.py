from testtools import TestCase
from fastapi import FastAPI
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import settings
from sqlalchemy import Session
from app.utils import random_email, random_lower_string
from app.models.user.repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate

client = TestClient(app)

class UserControllerTest(TestCase):
    def setUp(self):
        self.client = TestClient()
        self.db = Session()
        self.userRepository = UserRepository()

    def test_get_users_superuser_me(self):
        superuser_token_headers: Dict[str, str]
        r = self.client.get(f"{settings.API_V1_STR}/users/me", headers=superuser_token_headers)
        current_user = r.json()

        self.assertTrue(current_user, True)
        self.assertTrue(current_user["is_active"], True)
        self.assertTrue(current_user["is_superuser"], True)
        self.assertTrue(current_user["email"], True)

    def test_get_users_normal_user_me(self):
        normal_user_token_headers: Dict[str, str]
        r = self.client.get(f"{settings.API_V1_STR}/users/me", headers=norma_user_token_headers)
        current_user = r.json()

        self.assertTrue(current_user, True)
        self.assertTrue(current_user["is_active"], True)
        self.assertTrue(current_user["is_superuser"], False)
        self.assertTrue(current_user["email"], settings.EMAIL_TEST_USER)

    def test_create_user_new_email(self):
        superuser_token_headers: dict
        usrname = random_email()
        password = random_lower_string()
        data = {"email": username, "password": password}
        r = self.client.post(f"{settings.API_V1_STR}/users/", headers=superuser_token_headers)

        self.assertTrue(200 <= r.status_code < 300, True)
        created_user = r.json()
        user = self.userRepository.get_by_email(email=username)
        self.assertTrue(user, True)
        self.assertTrue(user.getEmail(), created_user["email"])

    def test_get_existing_user(self):
        superuser_token_headers: dict
        username = random_email()
        password = radom_lower_string()
        user_in = UserCreate(email=username, password=password)
        user = self.userRepository.create(obj_in=user_in)
        user_id = user.getId()
        r = self.client.get(f"{settings.API_V1_STR}/users/{user_id}", headers=superuser_token_headers)

        self.assertTrue(200 <= r.status_code < 300, True)
        api_user = r.json()
        existing_user = self.userRepository.get_by_email(email=username)
        self.assertTrue(existing_user, True)
        self.assertTrue(existing_user.getEmail(), api_user.get(email))

    def test_create_user_existing_username(self):
        superuser_token_headers: dict
        username = random_email()
        # username = email
        password = random_lower_string()
        user_in = UserCreate(email=username, password=password)
        self.userRepository.create(obj_in=user_in)
        data = {"email": username, "password": password}
        r = self.client.post(f"{settings.API_V1_STR}/users/", headers=superuser_token_headers)
        created_user = r.json()
        self.assertTrue(r.status_code, 400)
        self.assertFalse("_id", created_user) # assert "_id" not in created_user

    def test_create_user_by_normal_user(self):
        normal_user_token_headers: Dict[str, str]
        username = random_email()
        password = random_lower_string()
        data = {"email": username, "password": password}
        r = self.client.post(f"{settings.API_V1_STR}/users/", headers=normal_user_token_headers)

        self.assertTrue(r.status_code, 400)

    def test_retrieve_users(self):
        superuser_token_header: dict
        username = random_email()
        password = random_lower_string()
        user_in = UserCreate(email=username, password=password)
        self.userRepository.create(obj_in=user_in)

        username2 = random_email()
        password2 = random_lower_string()
        user_in2 = UserCreate(email=username2, password=password2)
        self.userRepository.create(obj_in=user_in2)

        r = self.client.get(f"{settings.API_V1_STR}/users/", headers=superuser_token_headers)
        all_users = r.json()

        assert len(all_users) > 1
        for item in all_users:
            assert "email" in item


    def test_create_user(self):
        response = client.post("/users/",json={"email": "deadpool@example.com", "password": "chimichangas4life"},)
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["email"] == "deadpool@example.com"
        assert "id" in data
        user_id = data["id"]

        response = client.get(f"/users/{user_id}")
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["email"] == "deadpool@example.com"
        assert data["id"] == user_id
