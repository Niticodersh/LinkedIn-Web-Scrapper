from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def get_driver(path=None):

    opts = Options()
    driver = webdriver.Chrome(options=opts)
    driver.get('http://selenium.dev')
    driver.quit()
    # path = "C:/Users/nitis/Downloads/chromedriver-win64/chromedriver.exe"
    driver = webdriver.Chrome(options=opts)
    return driver