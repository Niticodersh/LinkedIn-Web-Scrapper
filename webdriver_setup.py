from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver(path=None):

    opts = Options()
    # opts.add_argument("--headless")
    # opts.add_argument("--disable-gpu")
    # opts.add_argument("--no-sandbox")
    # opts.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options = opts)

    driver.get('http://selenium.dev')
    driver.quit()
    # path = "C:/Users/nitis/Downloads/chromedriver-win64/chromedriver.exe"
    driver = webdriver.Chrome(options=opts)
    return driver