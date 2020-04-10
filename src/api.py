import requests

class API:
    def __init__(self, auth_provider):
        self.auth_provider = auth_provider
        self.session = requests.Session()
        self.session.headers['Authorization'] = f'Bearer {auth_provider.access_token}'

    def request(self, url):
        result = self.session.get(
                'https://' + self.auth_provider.school_url + url
        )
        
        return result

    def get_roster(self):
        appointments = self.request('/api/personen/11698/afspraken')
        return appointments.json()['Items']

