from django.test import TestCase
import json


class TestUserLogin(TestCase):
    """Class tests user login"""

    def setUp(self):
        user_data = {
            "user": {
                "username": "Jacob390",
                "email": "jake@jake39.jake",
                "password": "jakejake"
            }
        }
        self.client.post(
            '/api/users/',
            data=json.dumps(user_data),
            content_type='application/json'
        )

    def tearDown(self):
        pass

    def test_user_login(self):
        """Test a user can successfully login"""

        login_data = {
            "user": {
                "email": "jake@jake39.jake",
                "password": "jakejake"
            }
        }

        response = self.client.post(
            '/api/users/login/',
            data=json.dumps(login_data),
            content_type='application/json'
        )
        data = response.data
        self.assertEqual(response.status_code, 200)
        self.assertIn("jake@jake39.jake", data['email'])

    def test_user_login_wrong_credentials(self):
        """Test login with wrong credentials"""

        login_data = {
            "user": {
                "email": "jake@jake39.jake",
                "password": "jakejake1"
            }
        }

        response = self.client.post(
            '/api/users/login/',
            data=json.dumps(login_data),
            content_type='application/json'
        )
        data = response.data
        self.assertEqual(response.status_code, 400)
        self.assertIn('A user with this email and password was not found.',
                      data['errors']['error'])

    def test_user_login_missing_password(self):
        """Test user cannot login without a password"""

        login_data = {
            "user": {
                "email": "jake@jake39.jake"
            }
        }

        response = self.client.post(
            '/api/users/login/',
            data=json.dumps(login_data),
            content_type='application/json'
        )
        data = response.data
        self.assertEqual(response.status_code, 400)
        self.assertIn('password', data['errors'])

    def test_user_login_wrong_content_type(self):
        """Test signing in with a wrong content type"""

        login_data = {
            "user": {
                "email": "jake@jake39.jake",
                "password": "jakejake"
            }
        }
        response = self.client.post(
            '/api/users/login/',
            data=login_data,
            content_type='text'
        )
        data = response.data
        self.assertEqual(response.status_code, 415)



