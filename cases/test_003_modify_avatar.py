import time

from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.my_center_page import MyCenterPage


def test_modify_user_avatar(open_browser,init_login):
    driver = open_browser
    time.sleep(2)
    # 进入到个人中心
    HomePage(driver).click_my_center_link()
    # 在个人中心进行头像修改
    my_center_page = MyCenterPage(driver)
    my_center_page.modify_avatar('C:\\Users\\86180\\Desktop\\test.png')
    # 断言 - 通过页面中的提示信息——修改成功
    # 缺陷：检查不了图片是否显示正常 - 图像匹配技术
    assert my_center_page.get_success_tips() == '修改成功!'
    driver.close()