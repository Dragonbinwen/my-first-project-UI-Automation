from selenium.webdriver.common.by import By
from common.base_page import BasePage


class ProductListPage(BasePage):
    # 商品名字-不能写死
    #product_name_text = (By.XPATH,'//div[text()="product_name"]')

    def __init__(self,driver):
        self.driver = driver

    def click_product(self,product_name):
        product_name_text = (By.XPATH, f'//div[contains(text(),"{product_name}")]')
        self.click(product_name_text)

