import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from utils.fixture_scope import FixtureScope


class HomePage(FixtureScope):

    def test_form_submission(self):

        home_page = HomePage()
        home_page.define_name().send_keys("rahul")
        home_page.define_email().send_keys("shetty@shetty.com")
        home_page.define_password().send_keys("123456789")
        sel = Select(home_page.get_gender())
        sel.select_by_visible_text("Male")
        home_page.submit_form().click()

        message = home_page.get_success_message.text
        assert message != "The Form has been submitted successfully!.", f"ERROR, message is incorrect"
