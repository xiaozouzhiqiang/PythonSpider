import requests

url = 'https://www.baidu.com/s'

params = {
    'wd': '中国'
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
}

respone = requests.get(url, params=params, headers=headers)

# print(respone.text) #打印这个可能会出现乱码
# print(respone.content.decode('utf-8'))
print(type(respone.status_code))
print(respone.encoding)
print(respone.url)
if respone.status_code == 200:
    with open('baidu.html', 'w', encoding='utf-8') as fp:
        fp.write(respone.content.decode('utf-8'))
    print('成功')
