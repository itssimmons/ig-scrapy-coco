from bs4 import BeautifulSoup
from env import BASE_URL
from Helpers import Helpers
from Driver import Driver

class Soup:
    def __init__(self, username: str):
        url = f'{BASE_URL}/{username}'
        html = Driver.launch(url)
            
        soap = BeautifulSoup(html, 'html.parser')
        self.body = soap.find('body')

    def find_many(self, tag: str, class_name: str):
        classes = Helpers.join_by('.', class_name)
        return self.body.select(f'{tag}.{classes}')
        