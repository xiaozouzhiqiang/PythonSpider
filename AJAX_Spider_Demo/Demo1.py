import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# 新版selenium 和旧版的有些变化，具体变化的参考下面
def run():
    driver_path = r"M:\chromedriver\chromedriver.exe"
    server = Service(executable_path=driver_path)
    option = webdriver.ChromeOptions()
    # 这句语句实现不自动关闭浏览器
    option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=server,options=option)
    driver.get("https://www.baidu.com")
    # print(driver.page_source)
    # 实现关闭当前页面和关闭浏览器的操作
    time.sleep(5)
    driver.close()
    # driver.quit()

if __name__ == '__main__':
    run()