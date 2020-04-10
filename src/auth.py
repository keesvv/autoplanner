import config
import json
import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class AuthProvider:
    def __init__(self, school_url):
        self.driver = webdriver.Chrome()
        self.school_url = school_url

    """
    Authenticate the user
    """
    def authenticate(self):
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

        item = f'oidc.user:https://accounts.magister.net:M6-{self.school_url}'
        raw_session = self.driver.execute_script(f"return window.sessionStorage.getItem('{item}')")

        # Parse the raw session
        session = json.loads(raw_session)

        self.access_token = session['access_token']
        self.driver.quit()
        return self.access_token

