from playwright.sync_api import Page, Locator
from src.pages.play.base_page_play import BasePagePlay
from src.pages.play.inventory_page_play import InventoryPagePlay

class LoginPagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page
        # locators

        self.username_input : Locator = page.get_by_role("textbox", name="Username")
        self.password_input : Locator = page.get_by_role("textbox", name="Password")
        self.login_button : Locator = page.get_by_role("button", name="Login")

    def navigate(self):
        self.navigate_url(url="https://www.saucedemo.com/")
 
    def enter_username(self, username):
        self.enter_text(self.username_input, username)
    
    def enter_password(self, password):
        self.enter_text(self.password_input, password)
       
    def click_submit_button(self):
        self.click_element(self.login_button)
        return InventoryPagePlay(self.driver)

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_submit_button()