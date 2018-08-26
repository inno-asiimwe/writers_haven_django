from django.test import TestCase
import json


class TestUserRegistration(TestCase):
    """
    Test user Registration.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_user_registration(self):
        """ Test successful registration """
        user_data = {
            "user": {
                "username": "Jacob390",
                "email": "jake@jake39.jake",
                "password": "jakejake"
            }
        }

        response = self.client.post(
            '/api/users/',
            data=json.dumps(user_data),
            content_type='application/json'
        )
        data = response.data
        self.assertEqual(response.status_code, 201)
        self.assertIn('Jacob390', data['username'])
        self.assertIn('jake@jake39.jake', data['email'])
        self.assertIn('token', data)

    def test_duplicate_user_registration(self):
        """Test failure to register a duplicate user."""
        user_data = user_data = {
            "user": {
                "username": "Jacob390",
                "email": "jake@jake39.jake",
                "password": "jakejake"
            }
        }

        response = self.client.post(
            '/api/users/',
            data=json.dumps(user_data),
            content_type='application/json'
        )
        response1 = self.client.post(
            '/api/users/',
            data=json.dumps(user_data),
            content_type='application/json'
        )
        data = response1.data
        self.assertIn('email',
                      data['errors'])
        self.assertIn('username',
                      data['errors'])
        self.assertEqual(response1.status_code, 400)

    def test_user_registration_non_json_input(self):
        """Test use of wrong content type in request"""
        user_data = {
            "user": {
                "username": "Jacob390",
                "email": "jake@jake39.jake",
                "password": "jakejake"
            }
        }

        response = self.client.post(
            '/api/users/',
            data=user_data,
            content_type='text'
        )
        self.assertEqual(response.status_code, 415)
    
    def test_user_registration_short_password(self):
        """Test user registration using a short password"""
        user_data = {
            "user": {
                "username": "Jacob390",
                "email": "jake@jake39.jake",
                "password": "jake"
            }
        }
        
        response = self.client.post(
            '/api/users/',
            data=json.dumps(user_data),
            content_type='application/json'
        )

        data = response.data
        self.assertEqual(response.status_code, 400)
        self.assertIn("password", data['errors'])
