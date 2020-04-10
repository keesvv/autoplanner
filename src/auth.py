import config
import json
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()

class AuthProvider:
    def __init__(self, school_url):
        self.school_url = school_url

    def authenticate(self):
        driver.get('https://' + self.school_url)
        wait = WebDriverWait(driver, 120)
        wait.until(lambda driver: driver.current_url.startswith(
            'https://' + config.SCHOOL_URL + '/magister')
        )

        item = f'oidc.user:https://accounts.magister.net:M6-{self.school_url}'
        raw_session = driver.execute_script(f"return window.sessionStorage.getItem('{item}')")

        session = json.loads(raw_session)

        self.access_token = session['access_token']
        driver.quit()

