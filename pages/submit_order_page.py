from selenium.webdriver.common.by import By
from common.base_page import BasePage


class SubmitOrderPage(BasePage):
    # 提交订单按钮
    submit_button = (By.XPATH, '//a[text()="提交订单"]')

    def __init__(self,driver):
        self.driver = driver

    def click_submit(self):
        self.click(self.submit_button)