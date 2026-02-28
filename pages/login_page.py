from selenium.webdriver.common.by import By
from common.base_page import BasePage

# 登录页面
# 页面类，属性：元素定位相关的信息（元素定位方法+定位表达式值）方法：页面的操作（登录/注册/搜索商品）
class LoginPage(BasePage):
    # 手机号码输入框
    mobile_phone_input = (By.XPATH,'//input[@placeholder="请输入手机号/用户名"]')
    # 密码输入框
    password_input = (By.XPATH,'//input[@placeholder="请输入密码"]')
    # 登录按钮
    login_button = (By.XPATH,'//a[@class="login-button"]')
    # 服务条款
    service_terms_text = (By.XPATH,'//a[text()="《服务条款》"]')

    def __init__(self,driver):
        self.driver = driver

    def login(self,account,password):
        self.input(self.mobile_phone_input, account)
        self.input(self.password_input,password)
        self.click(self.login_button)

    def check_service_terms(self):
        self.click(self.service_terms_text)

