import json
from datetime import datetime, timedelta
from mimesis import Person
from flask import current_app

from project.models.user import User
from project.api.common.utils.constants import Constants
from project.models.user import UserRole
from tests.base import BaseTestCase
from tests.utils import add_user, add_user_password


class TestLoginBlueprint(BaseTestCase):
    """
    Test users api endpoints
    Methods include:
    Login
    """
    # Generate fake data with mimesis
    data_generator = Person('en')
    version = 'v1'
    url = f'/{version}/auth/'
    """
    Test Login
    """
    def test_auth_login(self):
        """Ensure registered user can login"""
        user, password = add_user_password()
        print(user.email)
        with self.client:
            response = self.client.post(
                '/v1/auth/login',
                data=json.dumps(dict(
                    email=user.email,
                    password=password
                )),
                content_type='application/json',
                headers=[('Accept', 'application/json')]
            )
            data = json.loads(response.data.decode())
            self.assertEqual(data['message'], 'Successfully logged in.')
            self.assertTrue(data['auth_token'])
            self.assertEqual(response.content_type, 'application/json')
            self.assertEqual(response.status_code, 200)

   
