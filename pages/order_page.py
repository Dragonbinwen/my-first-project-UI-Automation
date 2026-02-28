from selenium.webdriver.common.by import By
from common.base_page import BasePage


class OrderPage(BasePage):
    # 商品数量
    product_nums_text = (By.XPATH, '//div[@class="goods-number"]')
    # 商品价格
    product_price_text = (By.XPATH,'//td[@class="bl"]/div[@class="amount"]//span')
    # 订单状态
    order_status_text = (By.XPATH,'//div[@class="status"]/div')
    # 商品名字
    product_name_text = (By.XPATH, '//a[@class="name"]')

    def __init__(self,driver):
        self.driver = driver

    def get_product_nums(self):
        nums_text = self.get_text(self.product_nums_text)
        # 去掉前面的x字符
        return nums_text.replace('×','')

    def get_product_price(self):
        # 去掉前面的￥字符串
        return self.get_text(self.product_price_text).replace('￥','')

    def get_order_status(self):
        # 去掉字符串前后的空白字符
        return self.get_text(self.order_status_text).strip()

    def get_product_name(self):
        return self.get_text(self.product_name_text)

