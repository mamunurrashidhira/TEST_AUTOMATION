from selenium import webdriver

def chrome_browser():
    driver = webdriver.Chrome(executable_path="F:\\HIRA_DOC\\TRAINING_COURSES\\SOFTWARE_TESTING_AND_QA\\TEST_AUTOMATION"
                                              "\\Drivers\\chromedriver.exe")
    # Open browser
    driver.get("https://www.google.com/")

    chrome_browser()