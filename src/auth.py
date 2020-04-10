import config
import json
import sys
import pickle
from os import path
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class AuthProvider:
    def __init__(self, school_url):
        self.school_url = school_url

    def __load_session(self):
        session_file = open('.session', 'rb')
        content = session_file.read()
        session_file.close()
        self.session = pickle.loads(content)

    def __write_session(self):
        session_file = open('.session', 'wb')
        pickle.dump(self.session, session_file)
        session_file.close()

    def __login(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://' + self.school_url)
        wait = WebDriverWait(self.driver, config.TIMEOUT)

        try:
            # Wait for Magister to redirect to homepage
            wait.until(lambda driver: driver.current_url.startswith(
                'https://' + config.SCHOOL_URL + '/magister'
            ))
        except TimeoutException:
            print('Authentication timed out. Try increasing '
                + 'the TIMEOUT value in the configuration file.')
            self.driver.quit()
            sys.exit(1)

        # Quit the driver when authenticated
        self.driver.quit()

        item = f'oidc.user:https://accounts.magister.net:M6-{self.school_url}'
        result = self.driver.execute_script(f"return window.sessionStorage.getItem('{item}')")
        self.session = json.loads(result)

    """
    Authenticate the user
    """
    def authenticate(self):
        if not path.isfile('.session'):
            self.__login()
        else:
            self.__load_session()

        self.access_token = self.session['access_token']
        self.__write_session()
        return self.access_token

