import time
import pytest
from selenium import webdriver

from pages.cart_page import CartPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.order_page import OrderPage
from pages.product_detail_page import ProductDetailPage
from pages.product_list_page import ProductListPage
from pages.submit_order_page import SubmitOrderPage


def test_submit_order_success(open_browser,init_login):
    driver = open_browser
    time.sleep(2)     # 不能去掉
    # 搜索商品关键字
    product_name = '香水'
    home_page = HomePage(driver)
    home_page.search(product_name)
    # 商品列表页面
    prodcut_list_page = ProductListPage(driver)
    prodcut_list_page.click_product(product_name)
    # 商品详情页面
    product_detail_page = ProductDetailPage(driver)
    product_detail_page.add_cart()
    # 点击购物车链接
    home_page.click_cart_link()
    # 购物车页面
    cart_page = CartPage(driver)
    total_price = cart_page.product_settle(product_name)
    # 提交订单页面
    submit_order_page = SubmitOrderPage(driver)
    submit_order_page.click_submit()
    # 断言？？检查页面的URL地址、标题、页面的元素信息变化
    # 进入到我的订单页面，检查订单的信息（订单数量、价格、状态、名字）
    home_page.click_order_link()
    order_page = OrderPage(driver)
    assert order_page.get_product_nums() == '1'
    assert order_page.get_order_status() == '待支付'
    assert product_name in order_page.get_product_name()
    # 价格的预期值???
    assert order_page.get_product_price() == total_price


