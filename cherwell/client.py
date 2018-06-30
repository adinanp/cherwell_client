import json
import requests
import logging

from .models import BusinessObjectFields

logger = logging.getLogger(__name__)


class CherwellClient:
    def __init__(self, url):
        self.cherwell_server = url

    def __build_url(self, endpoint):
        return '%s%s'  % (self.cherwell_server, endpoint)

    def __headers(self, **kwargs):
        return {
            'Authorization': 'Bearer %s' % kwargs['token'],
            'Content-Type': 'application/json'
        }

    def __format_response(self, response, key):
        if response.status_code != 200:
            try:
                logger.warning('Request failed with: %s' % response.json())
            except:
                pass

            response.raise_for_status()
        return response.json().get(key, None)

    def authenticate(self, gt='password', cid=None, user=None, pwd=None):
        url = self.__build_url('/token')

        response = requests.post(url, data={
            'grant_type': gt,
            'client_id': cid,
            'username': user,
            'password': pwd,
        })

        return self.__format_response(response, 'access_token')

    def save_business_object(self, token, data):
        url = self.__build_url('/api/v1/savebusinessobject/')

        data.fields = [
            f.__dict__ for f in data.fields if isinstance(f, BusinessObjectFields)
        ]

        response = requests.post(
            url,
            data=json.dumps(data.__dict__),
            headers=self.__headers(token=token)
        )

        return self.__format_response(response, 'busObPublicId')

    def get_business_object(self, token, BO, public_id):
        url = self.__build_url(
            '/api/v1/getbusinessobject/busobid/%s/publicid/%s' % (BO, public_id)
        )

        response = requests.get(url, headers=self.__headers(token=token))

        response.raise_for_status()

        return response.json()
