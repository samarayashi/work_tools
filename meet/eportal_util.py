import requests
import logging
import os

def get_login_session(username, password):
    # keep login session https://stackoverflow.com/questions/12737740/python-requests-and-persistent-sessions
    url = 'https://eportal.104.com.tw/doLogin.jsp'

    s = requests.Session()
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    }

    data = {
        'username': username,
        'password': password
    }

    response = s.post(url, headers=headers, data=data)
    logging.info(f' login status code: {response.status_code}')
    return s

if __name__ == '__main__':
    from dotenv import load_dotenv, dotenv_values
    # logger output https://stackoverflow.com/questions/13733552/logger-configuration-to-log-to-file-and-print-to-stdout
    logging.basicConfig(encoding='utf-8', level=logging.DEBUG,
    handlers=[
        # logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ])
    # username, password= dotenv_values(".env")
    # dotenv docs: https://pypi.org/project/python-dotenv/
    load_dotenv()
    username, password = os.environ.get('eportal_username'),os.environ.get('eportal_password')
    logging.debug('test login')
    get_login_session(username, password)
