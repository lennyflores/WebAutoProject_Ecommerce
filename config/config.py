import os

from dotenv import load_dotenv

load_dotenv()

user_name = os.getenv("USERNAME")
password = os.getenv("PASSWORD")


BASE_URL = {
    "development": "https://www.saucedemo.com/",
    "staging": "http://staging.demoqa.com",
    "production": "https://www.saucedemo.com/"
}