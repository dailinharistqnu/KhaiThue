from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import os

class WebAutomation:
    def __init__(self, driver_path):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        service = webdriver.ChromeService(executable_path=os.path.abspath(driver_path))
        # options.binary_location = driver_path
        self.driver = webdriver.Chrome(options=options,service=service)
        self.wait = WebDriverWait(self.driver, 30)

    def get(self,url):
        self.driver.get(url)

    def login(self,login_url):
        self.driver.get(login_url)
        span_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[4]/div/div[2]/div/div[3]/a/span')))
        login_button = span_element.find_element(By.XPATH,"..")
        login_button.click()
        span_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[3]/span[2]/strong/a')))
        span_element.click()
        span_element = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[5]/div[2]/div[1]/div')))
        span_element.click()

        self.fillinput("_userName","4101367812")
        input("Please solve the CAPTCHA and log in manually. Press Enter to continue...")
        self.click_button("dangnhap")
        self.fillinput("_password","Diem@050574")
        self.click_button("dangnhap")
        self.click_element("//span[text()='Khai thuế  ']")
        self.click_element("//*[contains(text(), 'Khai thuế CNKD')]")
        input("Please solve the CAPTCHA and log in manually. Press Enter to continue...")
        # self.select_an_option("/html/body/form/div[2]/table/tbody/tr[1]/td[2]/select","retailCnkd01Proc")
        # self.click_element("//input[@type='button' and @value='Tiếp tục']")

        
    def fill_form(self,index, row):
        # input_element = self.wait.until(EC.visibility_of_element_located((By.NAME, field)))
        # input_element.clear()
        # input_element.send_keys(value)
        self.fillcellinrow(f"plct06_{3+index}",row["Ten HH"])
        self.fillcellinrow(f"plct07_{3+index}",row["DVT"])
        # self.fillcellinrow(f"plct08_{3+index}",row["DVT"])

    def add_new_record(self):
        try:
            print("Tim cach them dong")
            add_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'themDong')))
            print(add_button)
            add_button.click()
        except Exception as e:
            print(e)

    def save_draft(self):
        save_draft_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'save_draft_button_id')))
        save_draft_button.click()

    def wait(self,time):
        self.wait = WebDriverWait(self.driver, time)

    def fillinput(self,name,value):
        input_element = self.wait.until(EC.visibility_of_element_located((By.NAME, name)))
        input_element.send_keys(value)

    def fillcellinrow(self,id,value):
        try:
            input_element = self.wait.until(EC.presence_of_element_located((By.ID, id)))
            input_element.clear()
            input_element.send_keys(value)
        except Exception as e:
            print(e)            



    def click_button(self,id,outer_element=False):
        button = self.wait.until(EC.element_to_be_clickable((By.ID, id)))
        if outer_element:
            button = button.find_element(By.XPATH,"..")
        button.click()
    
    def click_element(self,xpath,outer_element=False):
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        if outer_element:
            button = button.find_element(By.XPATH,"..")
        button.click()
    
    def select_an_option(self,xpath,value):
        select_box = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        select_box.click()
        # select = Select(select_box)
        # select.select_by_value(value)

    def switch_to_iframe(self,frame_name):
        self.driver.switch_to.frame(frame_name)

    def switch_to_main(self):
        self.driver.switch_to.default_content()


    def close(self):
        self.driver.quit()
    

