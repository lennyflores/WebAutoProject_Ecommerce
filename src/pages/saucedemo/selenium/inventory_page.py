from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import logging
from utils.logger import get_logger
from src.pages.saucedemo.selenium.base_page import BasePage
from src.pages.saucedemo.selenium.cart_page import CartPage

logger = get_logger(__name__)

class InventoryPage(BasePage):

    # inventory page locators
    inventory_title = (By.CLASS_NAME, "title")
    inventory_list = (By.XPATH, "//*[@id='inventory_container']/div/div[@class='inventory_item']")
    add_to_cart_button = (By.XPATH, "//*[@id='inventory_container']/div/div[@class='inventory_item']/div[@class='inventory_item_description']/div[@class='pricebar']/button[text()='Add to cart']")    
    shopping_cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    remove_to_cart_button = (By.XPATH, "//*[@id='inventory_container']/div/div[@class='inventory_item']/div[@class='inventory_item_description']/div[@class='pricebar']/button[text()='Remove']")


    def __init__(self, driver):
        super().__init__(driver)        
       
    # inventory page actions  
    def get_inventory_title(self):
        return self.find_element(self.inventory_title)
    
    # get the remove to cart button   
    def get_remove_to_cart_button(self):
        return self.find_element(self.remove_to_cart_button)
    
    # get the add to cart button
    def get_add_to_cart_button(self):
        return self.find_element(self.add_to_cart_button)
    
    # get the inventory items
    def get_inventory_items(self):
        """Return a list of WebElements representing inventory items."""
        return self.driver.find_elements(*self.inventory_list)
    
    # click the add to cart button
    def click_add_to_cart_button(self):
        self.click_element(self.add_to_cart_button)

    # click the remove to cart button
    def click_remove_to_cart_button(self):
        self.click_element(self.remove_to_cart_button)

    # click the add to cart button for all inventory items
    def click_add_to_cart_for_all_inventory_items(self):        
        inventory_items = self.get_inventory_items()
        for item in inventory_items:
            try:
                self.click_add_to_cart_button()                
                logger.info("Clicked Add to Cart for a product.")                
            except Exception as e:                
                logger.error(f"Failed to click Add to Cart for a product: {e}")

    # get the shopping cart badge count
    def get_shopping_cart_badge_count(self):
        return self.get_element_text(self.shopping_cart_badge)

    # get the shopping cart badge
    def get_shopping_cart_badge(self):
        return self.find_element(self.shopping_cart_badge)
        
    # click the shopping cart badge
    def click_shopping_cart_badge(self):
        self.click_element(self.shopping_cart_badge)
        return CartPage(self.driver)

    # inventory page validations for page loading
    def is_page_loaded(self):
        return "inventory" in self.driver.current_url.lower()
    