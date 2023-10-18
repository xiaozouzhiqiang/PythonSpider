from selenium import webdriver

drive = webdriver.Firefox()
drive.get("https://www.buyiju.com/")

for cookie in drive.get_cookies():
    # 打印所有cookie
    # print(cookie)
    pass

# 打印指定key的cookie值
name = drive.get_cookie("value")

# 删除cookie
drive.delete_cookie("name")

# 删除所有cookie
drive.delete_all_cookies()

print(name)