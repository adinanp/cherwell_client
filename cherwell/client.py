import json
import requests
import logging

from .models import BusinessObjectFields

logger = logging.getLogger(__name__)


class CherwellClient:
    def __init__(self, url):
        self.cherwell_server = url

    def __build_url(self, endpoint):
        return '{0}{1}'.format(self.cherwell_server, endpoint)

    def __format_response(self, response, key):
        if response.status_code != 200:
            try:
                logger.warning('Request failed with: %s' % response.json())
            except:
                pass

            response.raise_for_status()
        return response.json().get(key, None)

    def authenticate(self, gt='password', cid=None, user=None, pwd=None):
        endpoint = self.__build_url('/token')

        response = requests.post(endpoint, data={
            'grant_type': gt,
            'client_id': cid,
            'username': user,
            'password': pwd,
        })

        return self.__format_response(response, 'access_token')

    def save_business_object(self, token, data):
        endpoint = self.__build_url('/api/v1/savebusinessobject/')

        data.fields = [
            f.__dict__ for f in data.fields if isinstance(f, BusinessObjectFields)
        ]

        response = requests.post(
            endpoint,
            data=json.dumps(data.__dict__),
            headers={
                'Authorization': 'Bearer {0}'.format(token),
                'Content-Type': 'application/json'
            }
        )

        return self.__format_response(response, 'busObPublicId')
