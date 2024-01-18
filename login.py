from selenium.webdriver.common.by import By
from time import sleep

def login_to_linkedIn(driver, name, pwd):

    driver.get('https://www.linkedin.com')
    sleep(0.5)
    username = driver.find_element(By.ID, 'session_key')
    username.send_keys(name)
    sleep(0.5)
    password = driver.find_element(By.ID, 'session_password')
    password.send_keys(pwd)
    sleep(0.5)
    sign_in = driver.find_element(By.XPATH, '//*[@type="submit"]')
    sign_in.click()
    sleep(1)