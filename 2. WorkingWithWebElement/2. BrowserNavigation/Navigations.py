from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class navigation():
    def browser_navigate(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.get("https://www.google.com")

        driver.get("https://www.bbc.com")

        # navigate to previous page
        driver.back()

        # navigate to forward page
        driver.forward()

        # refresh the current page
        driver.refresh()

        driver.close()
test_obj = navigation()

test_obj.browser_navigate()