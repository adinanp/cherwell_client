from urllib.parse import urlparse


def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.status_code = status_code

        def json(self):
            return self.json_data

    if urlparse(args[0]).path == '/token' and kwargs['data']:
        v = list(kwargs['data'].values())
        c = [
            'password',
            'f9610046-adf6-46a4-8951-19279705f5e8',
            'user',
            'pwd',
        ]

        if set(v) == set(c):
            return MockResponse({'access_token': 'token_maneiro'}, 200)
        else:
            return MockResponse(
                {'error': 'invalid_grant', 'error_description': 'BADREQUEST'},
                400
            )

    elif urlparse(args[0]).path == '/api/v1/savebusinessobject/':
        h = kwargs['headers']
        if h['Authorization'] == 'Bearer token_maneiro':
            return MockResponse({'busObPublicId': 'patututum'}, 200)

    return MockResponse('Error', 404)
