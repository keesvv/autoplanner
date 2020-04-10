import requests

class API:
    def __init__(self, auth_provider):
        self.auth_provider = auth_provider
        self.session = requests.Session()
        self.session.headers['Authorization'] = f'Bearer {auth_provider.access_token}'

    def __request(self, url):
        result = self.session.get(
            f'https://{self.auth_provider.school_url}/api{url}'
        )
        
        return result

    def get_roster(self):
        appointments = self.__request('/personen/11698/afspraken')
        return appointments.json()['Items']

