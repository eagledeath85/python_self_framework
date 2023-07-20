import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# Declaring a class that has a fixture decorator allow to simplify the code
# This class will run the code in the fixture
# All classes that inherit from it will also have knowledge of the scope through the fixture
@pytest.mark.usefixtures("setup")
class FixtureScope:

    def verify_link_presence(self, text):
        # Adding an explicit wait, and wait until the class suggestions is present in the webpage code
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))