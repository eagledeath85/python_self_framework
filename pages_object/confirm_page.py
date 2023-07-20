from selenium.webdriver.common.by import By


class ConfirmPage:

    # Checkout button locator from the confirmation page
    confirm_checkout = (By.XPATH, "//button[@class='btn btn-success']")

    # Choice of country locator
    country = (By.ID, "country")

    # Tap country choice
    selected_country = (By.LINK_TEXT, "India")

    # Agreement locator
    agree_button = (By.XPATH, "//div[@class='checkbox checkbox-primary']")

    # Purchase locator
    purchase_button = (By.XPATH, "//input[@type='submit']")

    # Success Message
    success_message = (By.CSS_SELECTOR, "div[class*='alert-success']")

    def __init__(self, driver):
        self.driver = driver

    def checkout(self):
        return self.driver.find_element(*ConfirmPage.confirm_checkout)

    def country_menu(self):
        return self.driver.find_element(*ConfirmPage.country)

    def select_country(self):
        return self.driver.find_element(*ConfirmPage.selected_country)

    def terms_agreement(self):
        return self.driver.find_element(*ConfirmPage.agree_button)

    def final_purchase(self):
        return self.driver.find_element(*ConfirmPage.purchase_button)

    def find_success_message(self):
        return self.driver.find_element(*ConfirmPage.success_message)