from selenium.webdriver.common.by import By

from pages_object.checkout_page import CheckoutPage


class HomePage:

    # Shop locator
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.XPATH, "(//input[@type='text'])[1]")
    email = (By.CSS_SELECTOR, "input[name='email']")
    password = (By.CSS_SELECTOR, "input[type='password']")
    gender = (By.ID, 'exampleFormControlSelect1')
    form = (By.XPATH, "//input[@type='submit']")
    success_message = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver

    def shop_items(self):
        # driver.find_element(By.CSS_SELECTOR, "a[href*='shop']")
        self.driver.find_element(*HomePage.shop).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page

    def define_name(self):
        self.driver.find_element(*HomePage.name)

    def define_email(self):
        self.driver.find_element(*HomePage.email)

    def define_password(self):
        self.driver.find_element(*HomePage.password)

    def get_gender(self):
        self.driver.find_element(*HomePage.gender)

    def submit_form(self):
        self.driver.find_element(*HomePage.form)

    def get_success_message(self):
        self.driver.find_element(*HomePage.success_message)