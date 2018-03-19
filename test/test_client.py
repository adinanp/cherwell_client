import unittest
import client

from unittest.mock import patch

from .utils import mocked_requests_post
from models import BusinessObject, BusinessObjectFields


class CherwellClientTestCase(unittest.TestCase):
    def setUp(self):
        self.cherwell_client = client.CherwellClient('http://cherwell.com.br')

    def test_client(self):
        '''
        Should be created
        '''
        self.assertIsInstance(self.cherwell_client, client.CherwellClient)

    @patch('requests.post', side_effect=mocked_requests_post)
    def test_client_authentication_with_valid_credentials(self, mock_post):
        '''
        Should return 200 OK
        Should return a token for this user
        '''
        token = response = self.cherwell_client.authenticate(
            cid='f9610046-adf6-46a4-8951-19279705f5e8',
            user='user',
            pwd='pwd',
        )

        self.assertEqual(token, 'token_maneiro')

    @patch('requests.post', side_effect=mocked_requests_post)
    def test_client_authentication_with_invalid_credentials(self, mock_post):
        '''
        Should return 400 BADREQUEST
        Should return error description in response
        '''
        token = self.cherwell_client.authenticate(
            cid='f9610046-adf6-46a4-8951-19279705f5e',
            gt='passwor',
            user='use',
            pwd='pw',
        )

        self.assertFalse(token)

    @patch('requests.post', side_effect=mocked_requests_post)
    def test_client_save_busines_object_with_valid_data(self, mock_post):
        '''
        Should return 201 Created
        Should return a BusObId for created object
        '''
        data = BusinessObject('FakeBusObjectId')
        data.fields = [
            BusinessObjectFields(
                fieldId='FakeFieldid',
                name='FakeFieldName',
                value='FakeFieldValue',
                dirty=True,
            ),
            BusinessObjectFields(
                fieldId='FakeFieldid2',
                name='FakeFieldName2',
                value='FakeFieldValue2',
                dirty=True,
            ),
        ]

        bo = self.cherwell_client.save_business_object(
            token='token_maneiro', data=data
        )
        self.assertEqual(bo, 'patututum')

    @patch('requests.post', side_effect=mocked_requests_post)
    def test_client_save_business_object_with_invalid_data(self, mock_post):
        '''
        Should return 500 INTERNAL SERVER ERROR
        Should return hasError (true) attribute in json body
        '''
        data = BusinessObject()
        data.fields = []

        bo = self.cherwell_client.save_business_object(
            token='token', data=data
        )

        self.assertFalse(bo)


if __name__ == '__main__':
    unittest.main()
