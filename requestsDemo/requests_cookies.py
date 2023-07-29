import requests

login_url = "https://login2.scrape.center/login?next=/"
login_after = "https://login2.scrape.center/"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

data = {
    'username': 'admin',
    'password': 'admin'
}

session_login = requests.session()
session_login.post(login_url, data=data, headers=headers)
resp = session_login.get(login_after)
print(session_login.cookies.get_dict())
