import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

# 本Dmeo中没有用类来实现（复用的地方很多），而是直接用函数来操作，实现操作html中的表单元素

def run_Write_input():
    ## 下面这些都是操作输入框的操作
    driver_path = r"M:\chromedriver\chromedriver.exe"
    server = Service(executable_path=driver_path)
    option = webdriver.ChromeOptions()
    # 这句语句实现不自动关闭浏览器
    option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=server,options=option)
    driver.get("http://www.baidu.com")
    # 按照类名来获取输入框
    inputTag = driver.find_element(By.CLASS_NAME,"s_ipt")
    print(inputTag)
    inputTag.send_keys("selenium")
    time.sleep(2)
    # 清除输入框中的内容
    inputTag.clear()

def run_Check_rememberBtn():
    driver_path = r"M:\chromedriver\chromedriver.exe"
    server = Service(executable_path=driver_path)
    option = webdriver.ChromeOptions()
    # 这句语句实现不自动关闭浏览器
    option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=server,options=option)
    driver.get("https://www.ktanx.com/user/login")
    # 按照类名来获取输入框
    rememberBtn = driver.find_element(By.CLASS_NAME,"form-check-input")
    # 勾选记住密码
    time.sleep(2)
    rememberBtn.click()
    time.sleep(2)
    rememberBtn.click()

def run_check_select():
    driver_path = r"M:\chromedriver\chromedriver.exe"
    server = Service(executable_path=driver_path)
    option = webdriver.ChromeOptions()
    # 这句语句实现不自动关闭浏览器
    option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=server,options=option)
    driver.get("https://www.buyiju.com/")
    # 按照组件名称来获取控件·
    selectBtn = Select(driver.find_element(By.NAME,"sex"))
    time.sleep(2)

    # 按照select的索引来选择select 组件对应的值,从0开始
    # selectBtn.select_by_index(1)
    # time.sleep(2)
    # selectBtn.select_by_index(0)

    # 按照 select 属性的value值来进行匹配
    # selectBtn.select_by_value("女")
    # time.sleep(2)
    # selectBtn.select_by_value("男")
    # time.sleep(2)

    # 根据文本值来进行匹配
    selectBtn.select_by_visible_text("女性")
    time.sleep(2)
    selectBtn.select_by_visible_text("男性")
    time.sleep(2)

def run_click_btn():
    # 实现单击按钮查询生辰八字
    driver_path = r"M:\chromedriver\chromedriver.exe"
    server = Service(executable_path=driver_path)
    option = webdriver.ChromeOptions()
    # 这句语句实现不自动关闭浏览器
    option.add_experimental_option('detach', True)
    driver = webdriver.Chrome(service=server, options=option)
    driver.get("https://www.buyiju.com/")
    clickBtn = driver.find_element(By.CLASS_NAME,"zbbtn")
    time.sleep(2)
    clickBtn.click()

if __name__ == "__main__":
    run_click_btn()
