import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv('BASE_URL')
CHROME_DRIVER = os.getenv('CHROME_DRIVER')
BINARY = f'{CHROME_DRIVER}\chromedriver.exe'
IG_USER = os.getenv('IG_USER')
IG_PASS = os.getenv('IG_PASS')
