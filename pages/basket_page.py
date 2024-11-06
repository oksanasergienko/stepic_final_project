from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def is_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "Basket is not empty"


    def should_be_empty_basket_text(self):
        empty_basket_text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert "Your basket is empty." in empty_basket_text, "There is no message 'Basket is empty'"

