from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class WebAutomation:
    def __init__(self, driver_path):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service = webdriver.ChromeService(executable_path=os.path.abspath(driver_path))
        # options.binary_location = driver_path
        self.driver = webdriver.Chrome(options=options,service=service)
        self.wait = WebDriverWait(self.driver, 10)

    def login(self,login_url,target_url):
        self.driver.get(login_url)
        input("Please solve the CAPTCHA and log in manually. Press Enter to continue...")
        self.driver.get(target_url)


    def fill_form(self, data):
        for field, value in data.items():
            input_element = self.wait.until(EC.visibility_of_element_located((By.NAME, field)))
            input_element.clear()
            input_element.send_keys(value)

    def add_new_record(self):
        add_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'add_record_button_id')))
        add_button.click()

    def save_draft(self):
        save_draft_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'save_draft_button_id')))
        save_draft_button.click()

    def wait(self,time):
        self.wait = WebDriverWait(self.driver, time)

    def close(self):
        self.driver.quit()
    

