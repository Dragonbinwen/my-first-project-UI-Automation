import time

from selenium import webdriver
from pages.home_page import HomePage
from pages.login_page import LoginPage


def test_login(open_browser):
    driver = open_browser
    home_page = HomePage(driver)
    home_page.click_login_link()
    login_page = LoginPage(driver)
    login_page.login('lemon_auto', 'lemon123456')
    time.sleep(3)
    # 断言条件
    # 1、首页中的欢迎提示（1、使用欢迎的文本定位该元素，如果元素定位到了断言通过 2、定位欢迎元素之后获取其文本，与预期做对比）
    # assert home_page.get_welcome_tips() == '欢迎来到柠檬班'
    assert home_page.is_display_welcome_tips()
    # 2、显示当前的登录的用户名
    assert home_page.get_username_text() == 'lemon_auto'






    # 使用登录页面-->实例化登录页面类-->得到对应的对象
    # 1、实例化LoginPage类 -->得到对象
    #login_page = LoginPage()
    # 2、对象.方法名 调用对象里面的实例方法
    #login_page.login(driver)
    #（1）每次的操作调用都需要实例化页面对象
    #（2）每次的操作调用都需要传递driver参数
    # 可以通过类的构造方法来对数据进行初始化
    # LoginPage().login(driver,'lemon_auto','lemon123456')
    # LoginPage().check_service_terms(driver)

