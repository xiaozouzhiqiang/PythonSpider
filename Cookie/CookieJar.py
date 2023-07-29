from urllib import request
from http.cookiejar import MozillaCookieJar

# 创建一个cookiejar 对象
cookiejar = MozillaCookieJar('login2_cookie.txt')
handler = request.HTTPCookieProcessor(cookiejar)
opener = request.build_opener(handler)

# resp = opener.open('https://www.baidu.com')
# cookiejar.save()

# 如果cookie是会话结束后就消失的那种，记得添加属性
# cookiejar.save(ignore_discard=True)

# 下面进行举例，测试网站为 http://httpbin.org/

resp = opener.open('http://httpbin.org/cookies/set?coure=zouzhiqiang')
cookiejar.save(ignore_discard=True)

# 保存到本地的cookie怎么加载呢？？
cookiejar.load()
for cookie in cookiejar:
    print(cookie)
