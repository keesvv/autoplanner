import requests

class API:
    def __init__(self, auth_provider):
        self.auth_provider = auth_provider
        self.session = requests.Session()
        self.session.headers['Authorization'] = f'Bearer {auth_provider.access_token}'

    @property
    def person_prefix(self):
        return f"/personen/{self.user['Id']}"

    def __request(self, url):
        result = self.session.get(
            f'https://{self.auth_provider.school_url}/api{url}'
        )
        
        return result.json()

    def initialize(self):
        self.user = self.__request('/account')['Persoon']

    def get_roster(self):
        return self.__request(f'{self.person_prefix}/afspraken')['Items']

