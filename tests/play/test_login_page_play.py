import re
import time

from playwright.sync_api import Page, expect
from src.pages.play.login_page_play import LoginPagePlay    

class TestLoginPagePlay:

    def test_login_page(self, page: Page) -> None:
        """
        Test the login functionality
        """     
        login_page = LoginPagePlay(page)
        login_page.navigate()

        #wait_for_page_to_load()
        login_page.login("standard_user", "secret_sauce")
        time.sleep(5)

        # Assertions after login
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        # or check for an element that appears after successful login