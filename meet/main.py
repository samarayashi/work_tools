import imp
import os
import eportal_util
import meet_crawler
import logging
from dotenv import load_dotenv

logging.basicConfig(encoding='utf-8', level=logging.DEBUG,
    handlers=[
        logging.StreamHandler()
    ])

load_dotenv()
username, password = os.environ.get('eportal_username'),os.environ.get('eportal_password')

session = eportal_util.get_login_session(username, password)
data = meet_crawler.get_meets_reserve(session, '張志宏', 4, output_csv=True)
print(data)