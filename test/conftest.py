import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# This function allows us to run pytest with arguments in command line
# See docs.pytest.org for more details
def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):

    # Retrieving browser_name from the pytest command from command line
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
            # -- Chrome web browser
            service_object = Service("C:/Users/aallouche/Documents/Automation/chromedriver_win32/chromedriver.exe")
            driver = webdriver.Chrome(service=service_object)
    elif browser_name == "firefox":
            # -- Firefox web browser
            service_object = Service("C:/Users/aallouche/Documents/Automation/geckodriver-v0.33.0-win-aarch64/geckodriver.exe")
            driver = webdriver.Firefox(service=service_object)
    elif browser_name == "IE" or browser_name == "edge":
            # -- IE web browser
            service_object = Service(
                "C:/Users/aallouche/Documents/Automation/edgedriver_win64/msedgedriver.exe")
            driver = webdriver.Edge(service=service_object)


    # Adding implicit wait to the script
    driver.implicitly_wait(4)

    URL = 'https://rahulshettyacademy.com/angularpractice/'
    driver.get(URL)
    driver.maximize_window()

    # Pass the driver parameter as an attribute of the request instance
    request.cls.driver = driver

    yield

    driver.close()
