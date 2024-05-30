# from selenium.webdriver.common.by import By
# from time import sleep
#
# def login_to_linkedIn(driver, name, pwd):
#
#     driver.get('https://www.linkedin.com')
#     sleep(0.5)
#     username = driver.find_element(By.ID, 'session_key')
#     username.send_keys(name)
#     sleep(0.5)
#     password = driver.find_element(By.ID, 'session_password')
#     password.send_keys(pwd)
#     sleep(0.5)
#     sign_in = driver.find_element(By.XPATH, '//*[@type="submit"]')
#     sign_in.click()
#     sleep(1)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def login_to_linkedIn(driver, name, pwd):
    driver.get('https://www.linkedin.com')

    # Wait for the login form to be present
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'session_key')))

    username = driver.find_element(By.ID, 'session_key')
    username.send_keys(name)

    password = driver.find_element(By.ID, 'session_password')
    password.send_keys(pwd)

    # Click the "Sign In" button
    sign_in_button = driver.find_element(By.XPATH, '//*[@type="submit"]')
    sign_in_button.click()

    # Wait for the login to be successful with a maximum timeout of 30 seconds
    for _ in range(3):  # Try up to 3 times
        try:
            WebDriverWait(driver, 30).until(EC.url_contains('linkedin.com/feed'))
            break  # Break the loop if the URL contains 'linkedin.com/feed'
        except:
            print("Login unsuccessful. Retrying after 30 seconds...")
            sleep(30)

    # You might want to add additional checks for successful login if needed

    # Add a delay to ensure the page fully loads (customize the sleep duration as needed)
    sleep(5)
