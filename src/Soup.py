from bs4 import BeautifulSoup
from Driver import Driver
from Helpers import Helpers
from Helpers.env import BASE_URL
from Helpers.enums import CONSTANTS

class Soup:
    not_found = False

    def __init__(self, username: str):
        url = f'{BASE_URL}/{username}'
        html = Driver.launch(url)

        if (html == CONSTANTS.NotFound):
            self.not_found = True
        else:
            soap = BeautifulSoup(html, 'html.parser')
            self.body = soap.find('body')

    def find_many(self, tag: str, class_name: str):
        classes = Helpers.join_by('.', class_name)
        return self.body.select(f'{tag}.{classes}')
        