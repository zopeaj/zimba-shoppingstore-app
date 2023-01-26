from testtools import TestCase
from app.schemas.user import UserCreate, UserUpdate
from app.utils import random_email, random_lower_string
from app.core.security import verify_password
from app.models.user.userRepository import UserRepository
from fastapi import jsonable_encoder

class UserRepositoryTest(TestCase):
    def setUp(self):
        self.db = Session()
        self.userRepository = UserRepository()
        Base.metadata.create_all(engine)

    def test_create_user(self):
        email = random_email()
        password = random_lower_string()
        user_in = UserCreate(email=email, password=password)
        user = self.userRepository.create(obj_in=user_in)
        self.assertTrue(user.getEmail(), email)
        self.assertTrue(user.getPassword(), "hashed_password")

    def test_authenticate_user(self):
        email = random_email()
        password = random_lower_string()
        user_in = UserCreate(email=email, password=password)
        authenticated_user = self.userRepository.authenticate(password=password, email=email)
        self.assertTrue(authenticated_user, True)
        self.assertTrue(user.getEmail(), authenticated_user.getEmail())

    def test_not_authenticate_user(self):
        email = random_email()
        password = random_lower_string()
        user = self.userRepository.authenticate(email=email, password=password)
        self.assertFalse(user, None)

    def test_check_if_user_is_active(self):
        email = random_email()
        password = random_lower_string()
        user_in = UserCreate(email=email, password=password)
        user = self.userRepository.create(db, obj_in=user_in)
        is_active = self.userRepository.is_active(user)
        self.assertTrue(is_active, True)

    def test_check_if_user_is_active_inactive(self):
        email = random_email()
        password = random_lower_string()
        user_in = UserCreate(email=email, password=password, disabled=True)
        user = self.userRepository.create(obj_in=user_in)
        is_active = self.userRepository.is_active(user)
        self.assertTrue(is_active, True)

    def test_check_if_user_is_superuser(self):
        email = random_email()
        password = random_lower_string()
        user_in = UserCreate(email=email, password=password, is_superuser=True)
        user = self.userRepository.create(obj_in=user_in)
        is_superuser = self.userRepository.is_superuser(user)
        self.assertTrue(is_superuser, True)

    def test_check_if_user_is_superuser_normal_user(self):
        username = random_email()
        password = random_lower_string()
        user_in = UserCreate(email=username, password=password)
        user = self.userRepository.create(obj_in=user_in)
        is_superuser = self.userRepository.is_superuser(user)
        self.assertFalse(is_superuser, False)

    def test_get_user(self):
        password = random_lower_string()
        username = random_email()
        user_in = UserCreate(email=username, password=password, is_superuser=True)
        user = self.userRepository.create(obj_in=user_in)
        user_2 = self.userRepository.get(id=user.getId())
        self.assertTrue(user_2, True)
        self.assertTrue(user.getEmail(), user_2.getEmail())
        self.assertTrue(jsonable_encoder(user), jsonable_encoder(user_2))

    def test_update_user(self):
        password = random_lower_string()
        email = random_email()
        user_in = UserCreate(email=email, password=password, is_superuser=True)
        user = self.userRepository.create(obj_in=user_in)
        new_password = random_lower_string()
        user_in_update = UserUpdate(password=new_password, is_superuser=True)
        self.userRepository.update(db_obj=user, obj_in=user_in_update)
        user_2 = self.userRepository.get(id=user.getId())
        self.assertTrue(user_2, True)
        self.assertTrue(user.getEmail(), user_2.getEmail())
        self.assertTrue(verify_password(new_password), user_2.getPassword())

    def tearDownn(self):
        Base.metadata.drop_all(engine)
