import time

from selenium import webdriver

driver = webdriver.Firefox()

driver.get("https://www.baidu.com")

time.sleep(1)
new = 'window.open("https://www.google.com");'
# 打开一个新窗口
driver.execute_script(new)

# 获取当前页面的url
print(driver.current_url)
# 切换窗口,这样写的话，就是固定第一个打开的页面
driver.switch_to.window(driver.window_handles[0])

# 再次获取当前页面的url
print(driver.current_url)