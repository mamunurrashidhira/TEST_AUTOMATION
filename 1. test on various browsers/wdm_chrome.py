import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
def chrome_wdm():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    driver.get("https://www.google.com/")

    #driver.close()

    chrome_wdm()



