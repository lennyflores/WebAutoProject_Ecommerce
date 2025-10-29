import logging
import pytest
from selenium import webdriver
from utils.logger import get_logger
from config.config import Config
from src.pages.saucedemo.selenium.login_page import LoginPage
from config.config import Config
from utils.read_json_data import read_json_file

logger = get_logger(__name__)

# Arrange
@pytest.fixture(scope="session")
def first_entry(request):
    env = request.config.getoption("--env")
    logger.debug("Environment: %s", env)
    browser = request.config.getoption("--browser")
    logger.debug("Browser: %s", browser)
    return "a"


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

    """
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
    """
    grid_url = "http://localhost:4444/wd/hub"  # Replace with your Hub's address if different

    #options = ChromeOptions()
    #options = chrome_options

    driver = webdriver.Remote(
        command_executor=grid_url,
        options=chrome_options
    )

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


"""Provide credentials once per pytest session."""
@pytest.fixture(scope="session")
def env(request):
    # Optional: validate config once
    Config.validate()
    environment = request.config.getoption("--env", default="development")
    return {
        "env": environment,
        "user": Config.USER,
        "pass": Config.PASS
    }



# Fixture: Login (UI login before tests)
@pytest.fixture(scope="function")
def login(driver, env):
    """
    Logs in using credentials and returns InventoryPage object.
    """
    login_page = LoginPage(driver, env["env"])
    inventory_page = login_page.login(env["user"], env["pass"])
    return inventory_page

# Fixture: Read JSON data
@pytest.fixture(params=["credentials_errors"])
def read_data(request):
    """Read JSON data for a specific test case."""
    return read_json_file(f"tests/data/{request.param}.json")