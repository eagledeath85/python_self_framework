import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pages_object.home_page import HomePage
from utils.fixture_scope import FixtureScope


class TestHomePage(FixtureScope):

    # Load the login_credentials fixture to be able to use it during the test
    def test_form_submission(self, login_credentials):
        # Create log file
        log = self.get_logger()
        home_page = HomePage(self.driver)

        log.info(f'Putting name {login_credentials["name"]} in name field')
        home_page.get_name().send_keys(login_credentials["name"])
        log.info(f'Putting email {login_credentials["email"]} in email field')
        home_page.get_email().send_keys(login_credentials["email"])
        log.info(f'Putting password {login_credentials["password"]} in password field')
        home_page.get_password().send_keys(login_credentials["password"])

        log.info(f'Selecting gender {login_credentials["gender"]} in gender dropdown menu')
        # Inheritance from FixtureScope parent class
        self.select_options_by(home_page.get_gender(), login_credentials["gender"])
        time.sleep(5)
        log.info("Submitting form")
        home_page.submit_form().click()

        message = home_page.get_success_message().text
        log.info(f"Message received is: {message}")
        assert message != "The Form has been submitted successfully!.", f"ERROR, message is incorrect"

        # Refreshing the browser so the next set of credentials is not concatenated to the first one (ie. rahul shettyshandra kalapurna)
        self.driver.refresh()

    # This fixture accepts params. This way, we can loop through all the tuples and use all of them
    # when running test_form_submission
    @pytest.fixture(params=[{"name": "rahul shetty", "email": "shetty@shetty.com", "password": "123456789", "gender": "Male"},
                            {"name": "shandra kalapurna", "email": "shandra.k@shandra.com", "password": "P@ssword", "gender": "Female"},
                            {"name": "John Doe", "email": "john@doe.com", "password": "nononononono", "gender": "Male"}])
    def login_credentials(self, request):
        return request.param
