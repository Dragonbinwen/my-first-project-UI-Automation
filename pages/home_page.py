import time

from selenium.webdriver.common.by import By
from common.base_page import BasePage


class HomePage(BasePage):
    # 登录链接
    login_link = (By.LINK_TEXT, '登录')
    # 欢迎提示元素
    welcome_tips = (By.XPATH,'//span[text()="欢迎来到柠檬班"]')
    # 用户名元素
    username_text = (By.XPATH,'//a[@class="link-name"]')
    # 搜索输入框
    search_input = (By.XPATH,'//div[@class="search-input-box"]/input')
    # 搜索按钮
    search_button = (By.XPATH,'//div[@class="search-input-box"]/following-sibling::input')
    # 购物车
    cart_link = (By.XPATH,'//span[@data-route="cart"]')
    # 我的订单
    my_order_link = (By.XPATH,'//span[@data-route="order"]')
    # 个人中心
    my_center_link = (By.XPATH,'//span[@data-route="userCenter"]')

    def __init__(self,driver):
        self.driver = driver

    def search(self,data):
        self.input(self.search_input,data)
        self.click(self.search_button)

    def click_login_link(self):
        self.click(self.login_link)

    def click_cart_link(self):
        self.click(self.cart_link)

    def click_order_link(self):
        time.sleep(2)
        self.click(self.my_order_link)

    def click_my_center_link(self):
        self.click(self.my_center_link)

    def is_display_welcome_tips(self):
        return self.is_display(self.welcome_tips)

    def get_username_text(self):
        return self.get_text(self.username_text)
