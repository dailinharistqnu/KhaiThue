from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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
        # input("Please solve the CAPTCHA and log in manually. Press Enter to continue...")

    def select_report(self,reportid):
        self.select_an_option("/html/body/form/div[2]/table/tbody/tr[1]/td[2]/select",reportid)
        input("Press Enter to continue....")
        self.click_element("//input[@type='button' and @value='Tiếp tục']")


    def select_period(self,type,period):
        self.select_an_option("/html/body/form/div[2]/div[2]/table/tbody/tr[6]/td[2]/select",type)
        self.select_an_option("/html/body/form/div[2]/div[2]/table/tbody/tr[12]/td[2]/select",period)
        input("Press enter to continue....")
        self.click_element("//input[@type='button' and @value='Tiếp tục']")

    def select_annex(self,annex):
        input("Press enter to continue....")
        self.click_element(f"//font[@id='{annex}']")
        
    def fill_form(self,index, row):
        # input_element = self.wait.until(EC.visibility_of_element_located((By.NAME, field)))
        # input_element.clear()
        # input_element.send_keys(value)
        self.fillcellinrow(f"plct06_{3+index}",row["Ten HH"])
        self.fillcellinrow(f"plct07_{3+index}",row["DVT"])
        self.fillcellinrow(f"plct08_{3+index}",row["SLTD"],decimal=True)
        self.fillcellinrow(f"plct09_{3+index}",row["TTTD"])
        self.fillcellinrow(f"plct10_{3+index}",row["SLN"],decimal=True)
        self.fillcellinrow(f"plct11_{3+index}",row["TTN"])
        self.fillcellinrow(f"plct12_{3+index}",row["SLB"],decimal=True)
        self.fillcellinrow(f"plct13_{3+index}",row["TTB"])
        # self.fillcellinrow(f"plct14_{3+index}",row["SLTC"])
        # self.fillcellinrow(f"plct15_{3+index}",row["TTTC"])

    def add_new_record(self):
        try:
            print("Tim cach them dong")
            add_button = self.wait.until(EC.element_to_be_clickable((By.ID, 'themDong')))
            print(add_button)
            add_button.click()
        except Exception as e:
            print(e)

    def save_draft(self,xpath):
        self.click_element(xpath)

    def wait(self,time):
        self.wait = WebDriverWait(self.driver, time)

    def fillinput(self,name,value):
        try:
            input_element = self.wait.until(EC.visibility_of_element_located((By.NAME, name)))
            input_element.send_keys(value)
        except Exception as e:
            print(e)            
            input("Element not found. Manually fill it and press Enter to continue...")

    def fillcellinrow(self,id,value,decimal=False):
        try:
            input_element = self.wait.until(EC.presence_of_element_located((By.ID, id)))
            input_element.send_keys(Keys.CONTROL+"a")
            formated_value = ""
            if isinstance(value,(int,float)):
                if decimal:
                    formated_value = f"{value:,.2f}".replace(",","X").replace(".",",").replace("X",".")
                else:
                    formated_value = f"{value:,.0f}"
            else:
                formated_value = value
            print(formated_value)
            input_element.send_keys(formated_value)
        except Exception as e:
            print(e)            
            input("Element not found. Manually fill it and press Enter to continue...")

    def click_button(self,id,outer_element=False):
        try:
            button = self.wait.until(EC.element_to_be_clickable((By.ID, id)))
            if outer_element:
                button = button.find_element(By.XPATH,"..")
            button.click()
        except Exception as e:
            print(e)
            input("Element not found. Manually click it and press Enter to continue...")
    
    def click_element(self,xpath,outer_element=False):
        try:
            button = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            if outer_element:
                button = button.find_element(By.XPATH,"..")
            button.click()
        except Exception as e:
            print(e)
            input("Element not found. Manually click it and press Enter to continue...")
    
    def select_an_option(self,xpath,value):
        try:
            select_box = self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            select = Select(select_box)
            select.select_by_value(value)
        except Exception as e:
            print(e)
            input("Element not found. Manually select it and press Enter to continue...")

    def switch_to_iframe(self,frame_name):
        self.driver.switch_to.frame(frame_name)

    def switch_to_main(self):
        self.driver.switch_to.default_content()


    def close(self):
        self.driver.quit()
    

