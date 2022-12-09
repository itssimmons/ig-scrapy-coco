from bs4 import BeautifulSoup
from selenium import webdriver as web
from selenium.webdriver.support.ui import WebDriverWait as BrowserWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from ...env import BASE_URL, BINARY
from ..Helpers import Helpers

class Soup:
    def __init__(self, username: str):
        url = f'{BASE_URL}/{username}'
        html = self.launch_chrome(url)
            
        soap = BeautifulSoup(html, 'html.parser')
        self.body = soap.find('body')

    def launch_chrome(self, url: str):
        browser = web.Chrome(BINARY)
        browser.get(url)

        try:
            myElem = BrowserWait(browser, 3).until(EC.presence_of_element_located(By.XPATH, '//main[@role="main"]'))
            print('Page finally loaded!')
        except TimeoutException:
            print('Loading took to much time!')

        return browser.page_source
        
    def find_many(self, tag: str) -> list:
        return self.body.find_all(tag)

    def find(self, tag: str, class_name: str):
        classes = Helpers.join_by('.', class_name)
        return self.body.select(f'{tag}.{classes}')

    def destroy_tags(self, tag: str):
        selectors = self.body.select(tag)

        if len(selectors) > 0:
            for tag in selectors:
                tag.extract()
