import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# 新版selenium 和旧版的有些变化，具体变化的参考下面
def run():
    driver_path = r"M:\chromedriver\chromedriver.exe"
    server = Service(executable_path=driver_path)
    option = webdriver.ChromeOptions()
    # 这句语句实现不自动关闭浏览器
    option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=server,options=option)
    driver.get("http://www.baidu.com")
    # 通过id定位输入框
    # inputbyid = driver.find_element(by=By.ID,value='kw')

    #通过name 属性定位输入框
    # inputByName = driver.find_element(by=By.NAME,value='wd')

    # 通过class 属性定位输入框
    # inputClass = driver.find_element(by=By.CLASS_NAME,value='s_ipt')

    # 通过xpath 标签去查找输入框
    # inputXpath = driver.find_element(by=By.XPATH,value="//input[@id='kw']")

    # 通过css 标签选择输入框
    inputcss = driver.find_elements(by=By.CSS_SELECTOR,value=".quickdelete-wrap > input")[0]
    inputcss.send_keys("python")

    # 如果只是解析网页中的数据，那么推荐 将网页源代码扔给lxml来解析，因为lxml底层使用的是c代码，解析会更快，
    # 如果只是想要对元素进行一些操作，比如输入框什么的，或者点击某个按钮，那么就必须使用selenium给我们提供查找元素的方法
if __name__ == '__main__':
    run()