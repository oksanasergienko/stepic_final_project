from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.LINK_TEXT, "View basket")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_ITEM = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_TEXT = (By.XPATH, "//*[contains(text(), 'Your basket is empty.')]")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL = (By.ID, 'id_registration-email')
    PASSWORD = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.XPATH, "//button[@value='Register']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BOOK_NAME = (By.CSS_SELECTOR, ".alert-success strong")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".alertinner p")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#message .alert:nth-child(1) .alertinner')

