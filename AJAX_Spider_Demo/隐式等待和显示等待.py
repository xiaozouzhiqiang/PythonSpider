from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 隐式等待：调用driver.implicitly_wait,那么在获取不可用的元素之前，会先等待10秒的时间，
# 显示等待是表明某个条件成立后才执行获取元素的操作，也可以是等待的时候指定一个最大的时间，
driver = webdriver.Firefox()
# 隐式等待
driver.implicitly_wait(10)
driver.get("https://www.buyiju.com/")
# 显示等待
try:
    # 10：超时时间，在10秒内判断是否加载了Class_name属性为zbbtn的
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CLASS_NAME,"zbbtn")))
finally:
    print("按钮加载完成")
    driver.quit()
