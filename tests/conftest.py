import logging
import pytest
from selenium import webdriver
from utils.logger import get_logger
#from selenium.webdriver.chrome.options import Options

logger = get_logger(__name__)

# Arrange
@pytest.fixture(scope="session")
def first_entry(request):
    env = request.config.getoption("--env")
    logger.debug("Environment: %s", env)
    browser = request.config.getoption("--browser")
    logger.debug("Browser: %s", browser)
    return "a"

# Arrange
#@pytest.fixture(scope="class")
#fixture that will be executed once for each test function
@pytest.fixture(scope="function")
def driver():

    # Configure Chrome options to disable password management features
    chrome_options = webdriver.ChromeOptions()
    prefs = {
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False,
    "profile.password_manager_leak_detection": False, # Specifically for data breach warnings
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-infobars")
    #end of configuration

    if pytest.browser_type == "chrome":
        driver = webdriver.Chrome(options=chrome_options)
    elif pytest.browser_type == "firefox":
        driver = webdriver.Firefox()
    elif pytest.browser_type == "edge":
        driver = webdriver.Edge()
    elif pytest.browser_type == "safari":
        driver = webdriver.Safari()
    else:
        raise ValueError(f"Browser {pytest.browser_type} is not supported")
    
    driver.maximize_window()
    driver.implicitly_wait(10)
    
    # Clear cookies and cache before each test
    driver.delete_all_cookies()
    
    # clean up
    yield driver
    
    driver.quit()

@pytest.fixture()
def env(request):
    return request.config.getoption("--env")

def pytest_addoption(parser):
    parser.addoption(
        '--env', action='store', default='development', help="Environment where the tests are executed"        
    )
    parser.addoption(
        '--browser_type', action='store', default='chrome', help="Browser to run the web automation tests"
    )

def pytest_configure(config):
    pytest.env = config.getoption("env")
    pytest.browser_type = config.getoption("browser_type")

@pytest.fixture
def log_test_name(request):
    logger.info("Test name: '%s' started", request.node.name)
    def fin():
        logger.info("Test name: '%s' finished", request.node.name)
    
    request.addfinalizer(fin)