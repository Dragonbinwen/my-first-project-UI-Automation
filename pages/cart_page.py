import time

from selenium.webdriver.common.by import By
from common.base_page import BasePage


class CartPage(BasePage):
    # 选择全部
    select_all_checkbox = (By.XPATH,'//div[@class="cart-tab"]//input')
    # 结算
    settle_button =  (By.XPATH, '//a[text()="结算"]')
    # 总价
    total_price = (By.XPATH,'//div[@class="total-price"]/span')

    def __init__(self,driver):
        self.driver = driver

    # 全部结算
    def all_settle(self):
        self.click(self.select_all_checkbox)
        time.sleep(1)
        price = self.get_text(self.total_price).replace('¥','')
        self.click(self.settle_button)
        return price

    # 指定的商品结算
    def product_settle(self,product_name):
        # 选择指定的商品
        product_checkbox = (By.XPATH, f'//a[contains(text(),"{product_name}")]/parent::div/preceding-sibling::div[2]/input')
        self.click(product_checkbox)
        time.sleep(1)
        price = self.get_text(self.total_price).replace('¥', '')
        self.click(self.settle_button)
        return price