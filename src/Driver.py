from time import sleep
from selenium import webdriver as web
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from Helpers import Helpers
from Helpers.env import BINARY, BASE_URL, IG_USER, IG_PASS
from Helpers.enums import CONSTANTS

class Driver:
    @staticmethod
    def launch(url: str):
        browser = web.Chrome(BINARY)

        try:
            browser.get(BASE_URL)
            Helpers.await_page(browser)

            browser.find_element(By.XPATH, '//input[@name="username"]').send_keys(IG_USER)
            browser.find_element(By.XPATH, '//input[@name="password"]').send_keys(IG_PASS)
            browser.find_element(By.XPATH, '//button[@type="submit"]').click()
            sleep(2)

            browser.get(url)
            Helpers.await_page(browser)

            # not found page
            browser.find_element(By.XPATH, '//h2[@class="_aacl _aacr _aacw _aacx _aad6 _aadb"]')
            return CONSTANTS.NotFound
        except TimeoutException:
            raise TimeoutException('Loading took to much time!')
        except NoSuchElementException:
            return browser.page_source

