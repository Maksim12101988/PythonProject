import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Указываем путь к chrome.exe
def test_skillbox_title():
    # Set up the Chrome options
    chrome_options = Options()
    chrome_options.binary_location = r'C:\Users\ezhov\AppData\Local\Google\Chrome\Application\chrome.exe'

    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to the website
        driver.get("https://skillbox.ru/")
        print("Page loaded")

        # Check the title of the page
        assert "Skillbox" in driver.title
        print("Page title contains 'Skillbox – образовательная платформа с онлайн-курсами.'")
    finally:
        # Close the browser
        driver.quit()