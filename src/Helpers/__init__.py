from selenium.webdriver.support.ui import WebDriverWait as BrowserWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Helpers:
    @staticmethod
    def join_by(by: str, scope: str) -> str:
        return by.join(scope.split())

    @staticmethod
    def replace(search: str, replace: str, scope: str) -> str:
        return scope.replace(search, replace)

    @staticmethod
    def await_page(browser, ms = 6):
        BrowserWait(browser, ms).until(EC.presence_of_element_located((By.XPATH, '//main[@role="main"]')))
