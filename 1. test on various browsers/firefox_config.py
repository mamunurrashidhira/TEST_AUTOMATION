import time

from selenium import webdriver

def firefox_browser():
    driver = webdriver.Firefox(executable_path="F:\\HIRA_DOC\\TRAINING_COURSES\\SOFTWARE_TESTING_AND_QA"
                                               "\\TEST_AUTOMATION\\Drivers\\geckodriver.exe")
    # Open webpage
    driver.get("https://www.google.com/")

    # close webpage
    driver.close()

    firefox_browser()
