import re
import time

from playwright.sync_api import Page, expect
from src.pages.play.login_page_play import LoginPagePlay    
from src.pages.play.inventory_page_play import InventoryPagePlay    

class TestLoginPagePlay:

    def test_inventory_page(self, page: Page) -> None:
        """
        Test that Inventory page is fully loaded
        """     
        login_page = LoginPagePlay(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")         
        inventory_page = InventoryPagePlay(page)
                       
        # Assertions
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(inventory_page.inventory_title).to_be_visible()
        expect(inventory_page.inventory_title).to_contain_text("Swag Labs")  
        

    def test_inventory_add_to_cart(self, page: Page) -> None:
        """
        Test that the inventory page is loaded and item is added to cart successfully
        """     
        login_page = LoginPagePlay(page)
        login_page.navigate()
        login_page.login("standard_user", "secret_sauce")         
        inventory_page = InventoryPagePlay(page)

        # Assertions
        expect(inventory_page.add_to_cart_button).to_be_visible()

        inventory_page.add_to_cart()                       
        
        # Assertions
        #expect(page.locator("[data-test=\"remove-sauce-labs-backpack\"]")).to_be_visible() 
        expect(inventory_page.remove_to_cart_button).to_be_visible() 