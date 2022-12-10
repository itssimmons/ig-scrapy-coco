from selenium import webdriver as web
from selenium.webdriver.support.ui import WebDriverWait as BrowserWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from env import BINARY

class Driver:
    @staticmethod
    def launch(url: str):
        ms = 5
        browser = web.Chrome(BINARY)
        browser.get(url)

        try:
            BrowserWait(browser, ms).until(EC.presence_of_element_located((By.XPATH, '//main[@role="main"]')))
            print('Page finally loaded!')
        except TimeoutException:
            print('Loading took to much time!')

        return browser.page_source
