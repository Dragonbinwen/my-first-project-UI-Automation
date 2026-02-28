import time

import allure
import pyautogui
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from loguru import logger


# 所有页面类的父类
# BasePage这个类是所有你要去做web自动化的项目通用的
class BasePage:
    def wait_element_clickable(self, locator):
        try:
            return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        except Exception as e:
            # 这里处理异常，异常不会向外抛出
            logger.error(f'{locator}等待元素可被点击发生了异常')
            # 向外抛出代码异常
            raise e

    def wait_element_visible(self, locator):
        try:
            return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        except Exception as e:
            logger.error(f'{locator}等待元素可见发生了异常')
            raise e

    def wait_element_presence(self, locator):
        try:
            return WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(locator))
        except Exception as e:
            logger.error(f'{locator}等待元素存在发生了异常')
            raise e

    # 点击操作
    def click(self, locator):
        try:
            logger.info(f'{locator}执行点击操作')  # 想要知道哪个元素执行了点击操作 locator保存了元素的定位信息
            self.wait_element_clickable(locator).click()
        except Exception as e:
            # 处理异常 - 记录日志+截图
            logger.error(f'{locator}执行点击操作报错')
            # self.driver.get_screenshot_as_file("111.png")
            # 将截图附在allure报告中 self.driver.get_screenshot_as_png() --》 获取截图的二进制数据
            allure.attach(self.driver.get_screenshot_as_png(),name='失败用例截图',attachment_type=allure.attachment_type.PNG)
            raise e


    # 输入操作
    def input(self, locator, input_data):
        try:
            logger.info(f'{locator}执行输入操作，输入:{input_data}')
            self.wait_element_visible(locator).send_keys(input_data)
        except Exception as e:
            # 处理异常
            logger.error(f'{locator}执行输入操作报错')
            allure.attach(self.driver.get_screenshot_as_png(), name='失败用例截图',
                          attachment_type=allure.attachment_type.PNG)
            raise e

    # 获取元素的文本操作
    def get_text(self, locator):
        try:
            ele_text = self.wait_element_visible(locator).text
            logger.info(f'获取该元素{locator}的文本值:{ele_text}')
            return ele_text
        except Exception as e:
            logger.error(f'获取元素{locator}的文本值报错')
            allure.attach(self.driver.get_screenshot_as_png(), name='失败用例截图',
                          attachment_type=allure.attachment_type.PNG)
            raise e

    def is_display(self, locator):
        try:
            ele_display = self.wait_element_visible(locator).is_displayed()
            logger.info(f'获取元素{locator}的显示状态:{ele_display}')
            return ele_display
        except Exception as e:
            logger.error(f'获取元素{locator}的显示状态报错')
            allure.attach(self.driver.get_screenshot_as_png(), name='失败用例截图',
                          attachment_type=allure.attachment_type.PNG)
            raise e

    # 切换iframe的操作
    def switch_iframe(self, locator):
        try:
            logger.info(f'切换iframe:{locator}')
            iframe = self.wait_element_visible(locator)
            self.driver.switch_to.frame(iframe)
        except Exception as e:
            logger.error(f'切换iframe{locator}报错')
            allure.attach(self.driver.get_screenshot_as_png(), name='失败用例截图',
                          attachment_type=allure.attachment_type.PNG)
            raise e

    # 切换弹窗的操作
    def switch_alert(self):
        try:
            logger.info('切换弹窗')
            return self.driver.switch_to.alert
        except Exception as e:
            logger.error(f'切换弹窗报错')
            allure.attach(self.driver.get_screenshot_as_png(), name='失败用例截图',
                          attachment_type=allure.attachment_type.PNG)
            raise e

    # 通过JavaScript进行窗口上下滚动
    def scroll_window_up_down(self, distance):
        try:
            logger.info(f'窗口上下滚动到指定的距离:{distance}')
            self.driver.execute_script(f'document.documentElement.scrollTop={distance}')
        except Exception as e:
            logger.error(f'执行窗口上下滚动报错')
            allure.attach(self.driver.get_screenshot_as_png(), name='失败用例截图',
                          attachment_type=allure.attachment_type.PNG)
            raise e

    # 通过鼠标移动到指定元素上
    def mouse_move_to(self, locator):
        try:
            logger.info(f'鼠标移动到指定元素上:{locator}')
            ele = self.wait_element_presence(locator)
            ActionChains(self.driver).move_to_element(ele).perform()
        except Exception as e:
            logger.error(f'鼠标移动到指定元素上报错:{locator}')
            allure.attach(self.driver.get_screenshot_as_png(), name='失败用例截图',
                          attachment_type=allure.attachment_type.PNG)
            raise e

    # windows文件上传窗口的操作
    def win_upload_select(self,file_path):
        try:
            logger.info(f'windows文件上传窗口选择，输入文件路径:{file_path}')
            # 输入文件上传路径
            time.sleep(0.5)
            pyautogui.write(file_path)
            time.sleep(0.5)
            pyautogui.press('enter',presses = 1)
        except Exception as e:
            logger.error(f'windows文件上传窗口选择报错:{file_path}')
            allure.attach(self.driver.get_screenshot_as_png(), name='失败用例截图',
                          attachment_type=allure.attachment_type.PNG)
            raise e

