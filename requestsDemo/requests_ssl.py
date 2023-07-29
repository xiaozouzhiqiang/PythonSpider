import requests
import urllib3
urllib3.disable_warnings()

url = 'https://ssr2.scrape.center/'

resp = requests.get(url, verify=False)

print(resp.text)

