from selenium.webdriver.common.by import By

from pages_object.confirm_page import ConfirmPage


class CheckoutPage:
    # Phones cards locator
    phones_cards = (By.XPATH, "//div[@class='card h-100']")

    # Phone Name locator
    phone_name = (By.XPATH, "div/h4/a")

    # Add button locator
    add_button = (By.XPATH, "div/button")

    # Checkout locator
    checkout = (By.CSS_SELECTOR, "a[class*='btn-primary']")

    def __init__(self, driver):
        self.driver = driver

    def get_phones_cards(self):
        # driver.find_elements(By.XPATH, "//div[@class='card h-100']")
        return self.driver.find_elements(*CheckoutPage.phones_cards)

    def get_phone_name(self):
        return self.driver.find_element(*CheckoutPage.phone_name)

    def add(self):
        return self.driver.find_element(*CheckoutPage.add_button)

    def checkout_items(self):
        # driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']")
        self.driver.find_element(*CheckoutPage.checkout).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
