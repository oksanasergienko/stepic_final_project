from .pages.main_page import MainPage
from .pages.base_page import BasePage
from .pages.login_page import LoginPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = LoginPage(browser, link)
        page.open()
        login_page = page.go_to_login_page()
        login_page.should_be_login_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)
    page.open()
    basket_page = page.go_to_basket()
    basket_page.is_basket_empty()
    basket_page.should_be_empty_basket_text()

