import urllib.request

import requests

hao_url = "http://www.hao123.com/"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

# response = urllib.request.urlopen(hao_url)
# print(response.read().decode('utf-8'))

html = requests.get(hao_url, headers=headers)
html.encoding = 'utf-8'
# print(html.text)

with open('reren.html', 'w', encoding='utf-8') as fp:
    fp.write(html.text)
    print('写入成功')

