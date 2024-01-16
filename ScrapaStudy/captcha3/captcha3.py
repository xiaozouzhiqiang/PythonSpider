# 主要练习 https://scrape.center/ Python 爬虫练习平台的
# captcha3 图文点选

import time
from io import BytesIO
from PIL import Image
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from chaojiying import Chaojiying_Client
from selenium.common.exceptions import TimeoutException

# 12306账号密码
USERNAME = 'admin'
PASSWORD = 'admin'

# 超级鹰打码平台账号密码
CHAOJIYING_USERNAME = '********'
CHAOJIYING_PASSWORD = '*******'

# 超级鹰打码平台软件ID
CHAOJIYING_SOFT_ID = '*************'
# 验证码类型
CHAOJIYING_KIND = '9004'

class CrackTouClick:

    def __init__(self):
        self.url = 'https://captcha3.scrape.center/'
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)  #不自动关闭浏览器
        self.options.add_argument('--start-maximized')#浏览器窗口最大化
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        # self.options.add_argument('--user-data-dir=F:\PythonSpider\PythonObject\PythonSpider\QiMai\chrome\profile')
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.options.add_argument('window-size=1920x1080')
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        self.wait = WebDriverWait(self.driver, 20)
        self.username = USERNAME
        self.password = PASSWORD
        self.chaojiying = Chaojiying_Client(CHAOJIYING_USERNAME, CHAOJIYING_PASSWORD, CHAOJIYING_SOFT_ID)

    def crack(self):
        # 调用账号密码输入函数
        self.get_input_element()
        # 调用验证码图片剪裁函数
        image = self.get_touclick_image()
        bytes_array = BytesIO()
        image.save(bytes_array, format='PNG')
        # 利用超级鹰打码平台的 API PostPic() 方法把图片发送给超级鹰后台，发送的图像是字节流格式，返回的结果是一个JSON
        result = self.chaojiying.PostPic(bytes_array.getvalue(), CHAOJIYING_KIND)
        # # 调用验证码坐标解析函数
        locations = self.get_points(result)
        # 调用模拟点击验证码函数
        self.touch_click_words(locations)

    # 账号密码输入函数
    def get_input_element(self):
        # 登录页面发送请求
        self.driver.get(self.url)
        # 查找到账号密码输入位置的元素
        time.sleep(0.5)
        username = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="text"]')))
        password = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="password"]')))
        # 输入账号密码
        username.send_keys(self.username)
        password.send_keys(self.password)
        submit = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="el-button el-button--primary"]')))
        submit.click()

    # 验证码图片剪裁函数
    def get_touclick_image(self, name='captcha3.png'):
        # 获取验证码的位置
        element = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.geetest_widget')))
        time.sleep(1)
        location = element.location
        size = element.size
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], location['x'] + size['width']
        # 先对整个页面截图
        screenshot = self.driver.get_screenshot_as_png()
        screenshot = Image.open(BytesIO(screenshot))
        # 根据验证码坐标信息，剪裁出验证码图片
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save(name)
        return captcha

    # 验证码坐标解析函数，分析超级鹰返回的坐标
    def get_points(self, captcha_result):
        # 超级鹰识别结果以字符串形式返回，每个坐标都以|分隔
        groups = captcha_result.get('pic_str').split('|')
        # 将坐标信息变成列表的形式
        locations = [list(map(int, item.split(','))) for item in groups]    
        return locations

    # 模拟点击验证码函数
    def touch_click_words(self, locations):
        parent_element = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.geetest_widget'))
        )
        size = parent_element.size
        captcha_width = size['width']
        captcha_height = size['height']
        # 主要注意此处，selenium 4.10+版本，坐标点选不再从左上角开始，而是从中心位置开始，所以需要将左上角位置的坐标，
        # 转换成以中心点来计算的坐标
        coordinates_list = self.convert_coordinates_list(locations,captcha_width,captcha_height)
        # 循环点击正确验证码的坐标
        for location in coordinates_list:
            time.sleep(0.5)
            ActionChains(self.driver).move_to_element_with_offset(parent_element, location[0], location[1]).click().perform()
        time.sleep(0.5)
        # 最后在点击确定按钮
        submit = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@class="geetest_commit"]')))
        submit.click()

    def convert_coordinates_list(self,coordinates_list, width, height):
        # 计算中心点坐标
        center_x = width // 2
        center_y = height // 2
        # 创建一个新的列表来存储转换后的坐标
        new_coordinates_list = []
        for coordinates in coordinates_list:
            x, y = coordinates
            # 将坐标转换为以中心点为原点的坐标
            new_x = x - center_x
            new_y = y - center_y
            new_coordinates_list.append([new_x, new_y])
        return new_coordinates_list

if __name__ == '__main__':
    crack = CrackTouClick()
    crack.crack()