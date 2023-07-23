from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages_object.checkout_page import CheckoutPage
from pages_object.confirm_page import ConfirmPage
from pages_object.home_page import HomePage
from utils.fixture_scope import FixtureScope


# Instead of declaring fixture on every class, we declare a class in utils that knows what's the scope of the fixture
class TestOne(FixtureScope):
    def test_e2e(self):

        # Create logger
        logger = self.get_logger()

        # Create an instance of home_page
        home_page = HomePage(self.driver)

        # Find the Shop button using css regex and click on it
        checkout_page = home_page.shop_items()

        # Retrieving all the elements (phones) of the webpage
        # checkout_page = CheckoutPage(self.driver)
        logger.info("Getting phones cards from webpage")
        phone_cards = checkout_page.get_phones_cards()

        assert len(phone_cards) > 0, f"ERROR, list of checkboxes is empty."

        logger.info(f'Looking for phone name Blackberry')
        # Asserting phone_name is Blackberry. If yes, add it to the cart
        for phone_card in phone_cards:
            phone_name = phone_card.text
            if phone_name == "Blackberry":
                logger.info(f'Phone name found with name {phone_name}')
                checkout_page.add_button.click()
                break

        # Go to the checkout confirm page
        confirm_page = checkout_page.checkout_items()

        # Click on Checkout button in the Confirm Page
        # self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        confirm_page.checkout().click()

        logger.info(f'Looking for India in the auto-suggest menu')
        # Writing in the auto-suggest menu
        # self.driver.find_element(By.ID, "country").send_keys("ind")
        confirm_page.country_menu().send_keys("ind")

        # Adding an explicit wait, and wait until the class suggestions is present in the webpage code
        self.verify_link_presence("India")

        # Click on the desired country
        confirm_page.select_country().click()

        # Click on agree with terms and conditions
        #self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        confirm_page.terms_agreement().click()

        # Click on Purchase button
        # self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        confirm_page.final_purchase().click()

        # Retrieving final message
        # final_message = self.driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text
        final_message = confirm_page.find_success_message().text

        # Validating message
        assert 'Success' in final_message, f"ERROR, purchase is not complete"
