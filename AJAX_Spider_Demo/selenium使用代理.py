from selenium import webdriver

options = webdriver.ChromeOptions() # 创建一个配置对象
options.add_argument('--proxy-server=http://113.121.40.162:9999')
driver = webdriver.Chrome(options=options)
driver.get("http://httpbin.org/ip")

print(driver.page_source)