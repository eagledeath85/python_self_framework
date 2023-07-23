import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select


# Declaring a class that has a fixture decorator allow to simplify the code
# This class will run the code in the fixture
# All classes that inherit from it will also have knowledge of the scope through the fixture
@pytest.mark.usefixtures("setup")
class FixtureScope:

    def get_logger(self):

        logger_name = inspect.stack()[1][3]
        # Capture the filename in the __name__ parameter. Mandatory to give this
        logger = logging.getLogger(logger_name)

        # Log file creation
        fileHandler = logging.FileHandler("logfile.log")

        # Log format - How to print logs
        # YYYY-MM-DD HH:MM:SS,MMS :LOG_LEVEL : TEST_NAME :LOG_MESSAGE
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

        # Tell the fileHandler object how to format the log file
        fileHandler.setFormatter(formatter)

        # Giving the logger in which file it has to print the logs - Where to print logs
        logger.addHandler(fileHandler)

        # Setting level of logging to DEBUG
        # At INFO level, debu logs won't be printed
        logger.setLevel(logging.DEBUG)

        return logger

    def verify_link_presence(self, text):
        # Adding an explicit wait, and wait until the class suggestions is present in the webpage code
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

    def select_options_by(self, locator, text: str):
        """Declaring this method here allows us to reuse it on every test in which we have to search in a dropdown menu.
        We'll only need to pass a locator, and a string to look for"""
        # locator = home_page.get_gender()
        sel = Select(locator)
        sel.select_by_visible_text(text)