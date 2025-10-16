from playwright.sync_api import Page, Locator
from src.pages.play.base_page_play import BasePagePlay

class InventoryPagePlay(BasePagePlay):
    def __init__(self, page: Page):
        self.page = page

        # locators
        self.inventory_title : Locator = page.get_by_text("Swag Labs")  
        self.add_to_cart_button = page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]")
        self.remove_to_cart_button = page.locator("[data-test=\"remove-sauce-labs-backpack\"]")

    def navigate(self):
        self.navigate_url(url="https://www.saucedemo.com/inventory.html")
        
    def get_inventory_title(self,inventory_title):
        self.get_tag_and_text(self.inventory_title, inventory_title)
    
    def add_to_cart(self):
        self.click_element(self.add_to_cart_button)