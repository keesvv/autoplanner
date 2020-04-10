from selenium import webdriver

driver = webdriver.Chrome()

class AuthProvider:
    def __init__(self, school_url):
        self.school_url = school_url

    def authenticate(self):
        driver.get('https://' + self.school_url)
        return None

