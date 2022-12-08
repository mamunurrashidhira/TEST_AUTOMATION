import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

class Locator():
    def locator_findings(self):

        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(5)

        # username = driver.find_element(By.NAME, 'username')
        # username = driver.find_element(By.CSS_SELECTOR, "input[name='username']")

        username = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='orangehrm-login-layout']/div["
                                                 "@class='orangehrm-login-layout-blob']//form["
                                                 "@action='/web/index.php/auth/validate']/div[1]/div//input["
                                                 "@name='username']")
        
        if username is not None:
            print('Username found Successfully')
        else:
            print('Username not found')

        driver.close()


test_obj = Locator()
test_obj.locator_findings()
