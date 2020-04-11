import requests
from errors import TokenExpiredError, RequestError

class API:
    def __init__(self, auth_provider):
        self.auth_provider = auth_provider
        self.session = requests.Session()
        self.session.headers['Authorization'] = f'Bearer {auth_provider.access_token}'

    @property
    def __person_prefix(self):
        return f"/personen/{self.user['Id']}"

    def __request(self, url):
        result = self.session.get(
            f'https://{self.auth_provider.school_url}/api{url}'
        )

        # User needs to re-login
        if result.status_code == 401:
            raise TokenExpiredError

        # A non-200 code was returned
        if result.status_code != 200:
            raise RequestError
        
        return result.json()

    def initialize(self):
        self.user = self.__request('/account')['Persoon']

    def get_roster(self):
        return self.__request(f'{self.__person_prefix}/afspraken')['Items']

