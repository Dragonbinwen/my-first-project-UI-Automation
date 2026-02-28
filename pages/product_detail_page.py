from selenium.webdriver.common.by import By
from common.base_page import BasePage


class ProductDetailPage(BasePage):
    # 属性
    # 添加购物车按钮
    add_cart_button = (By.XPATH,'//a[@class="add-cart"]')
    # 商品的名称
    product_title = (By.XPATH,'//div[@class="name-box"]/div[@class="name"]')

    def __init__(self,driver):
        self.driver = driver

    # 方法
    def add_cart(self):
        self.click(self.add_cart_button)

    def get_product_title(self):
        return self.get_text(self.product_title)