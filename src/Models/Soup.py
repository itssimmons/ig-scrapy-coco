import os
import urllib.request
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()
BASE_URL = os.getenv('BASE_URL')

class Soup:
    def __init__(self, username: str):
        url = f'{BASE_URL}/{username}'
        xhr = urllib.request.urlopen(url)
        html = xhr.read().decode()
            
        soap = BeautifulSoup(html, 'html.parser')
        self.body = soap.find('body')
        
    def find_many(self, tag: str) -> list:
        return self.body.find_all(tag)

    def destroy_tags(self, tag: str):
        selectors = self.body.select(tag)

        if len(selectors) > 0:
            for tag in selectors:
                tag.extract()

    def echo(self):
        print(self.body)
