import time

from selenium.webdriver.common.by import By
from common.base_page import BasePage

class MyCenterPage(BasePage):
    # 编辑资料区域
    edit_profile_area = (By.XPATH,'//div[@class="portrait"]')
    # 编辑资料按钮
    edit_profile_button = (By.XPATH,'//div[@class="edit"]')
    # 用户头像
    user_avatar = (By.CLASS_NAME, 'el-upload--text')
    # 保存账号信息
    save_account_button = (By.LINK_TEXT,'保存账户信息')
    # 修改成功的提示
    success_tips  = (By.XPATH,'//p[@class="el-message__content"]')

    def __init__(self,driver):
        self.driver = driver

    def get_success_tips(self):
        return self.get_text(self.success_tips)

    def modify_avatar(self,pic_path):
        # 1、将鼠标移动到编辑资料上面
        self.mouse_move_to(self.edit_profile_area)
        time.sleep(0.5)
        # 2、点击编辑资料
        self.click(self.edit_profile_button)
        # 3、点击用户头像
        self.click(self.user_avatar)
        # 4、选择本地的图片 - windows窗口选择框
        self.win_upload_select(pic_path)
        # 等到按钮变为红色才可以
        time.sleep(5)
        # 5、点击保存账号信息按钮
        self.click(self.save_account_button)
