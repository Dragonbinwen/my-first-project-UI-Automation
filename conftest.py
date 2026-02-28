import pytest
from selenium import webdriver

from pages.home_page import HomePage
from pages.login_page import LoginPage
from loguru import logger
from config import env_dict

# 这是pytest的钩子函数：通过该钩子函数在pytest执行开始的时候获取我们定义的参数
def pytest_addoption(parser):
    # 设置要接收的命令行参数
    parser.addoption("--env", default="test", choices=['dev', 'test', 'pre'],
                     help="命令行参数 '--env' 用来设置环境切换")

@pytest.fixture(scope='session')
def get_env(request):
    # 从命令行参数中获取env参数的值,env_name就是环境名字
    env_name = request.config.getoption("--env")
    yield env_name
    # 拿到对应环境的地址 测试环境：http://test.lemonban.com 开发的环境：http://dev.lemonban.com -->写入配置文件中

# 把登录的操作及打开浏览器操作定义成fixture函数
@pytest.fixture
def open_browser(get_env):
    url = env_dict[get_env]['url']
    logger.info(f"选择的环境地址是:{url}")
    # 在每条用例前面执行的代码
    driver = webdriver.Firefox()
    logger.info('===============================打开Chrome浏览器================================')
    driver.get(url)
    # yield关键字两大作用：1、作为前后置的分割线  2、相当于return返回数据
    yield driver
    logger.info('===============================关闭Chrome浏览器================================')
    driver.close()
    #return driver

@pytest.fixture
def init_login(open_browser):
    driver = open_browser
    home_page = HomePage(driver)
    home_page.click_login_link()
    login_page = LoginPage(driver)
    login_page.login('lemon_auto', 'lemon123456')

if __name__ == '__main__':
    pytest