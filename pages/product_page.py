from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    
    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text.strip()

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text.strip()

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_button.click()

    def should_be_correct_book(self, product_name):
        actual_book_name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text.strip()
        assert product_name in actual_book_name, f"Expected book name '{product_name}', but got '{actual_book_name}'"

    def should_be_correct_basket_total(self, product_price):
        basket_total = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text.strip()
        price_value = basket_total.split(" ")[-1]
        assert product_price.strip() == price_value, f"Expected basket total '{product_price}', but got '{basket_total}'"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        
    def success_message_disappered(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"
        

