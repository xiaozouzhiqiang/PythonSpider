import requests

url = 'http://httpbin.org/ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

proxy = {
    'http': '222.74.73.202:42055'
}

resp = requests.get(url, headers=headers,proxies=proxy)

with open('../xpathDemo/proxy.html', 'w', encoding='utf*8') as fp:
    fp.write(resp.text)

