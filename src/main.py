from drivers.webInteraction import WebAutomation
from pandas_tools import file_processing
from datetime import datetime
from helpers import datehandler
import time
def main():
    # driver = WebAutomation("C:/Users/taoda/tools/khaithue/src/drivers/chromedriver/chromedriver.exe")
    # Doc file excel
    df = file_processing.load_excel_data("src/input/data.xlsx",sheet_name="Sheet5")
    # file_processing.save_excel_data(df,f"src/output/data_{datehandler.current_toString()}.xlsx")

    #Khoi chay trinh duyet, dang nhap
    driver = WebAutomation("src/drivers/chromedriver/chromedriver.exe")
    driver.login("https://thuedientu.gdt.gov.vn")
    driver.switch_to_iframe("mainframe")
    driver.select_report("retailCnkd01TT40Proc")
    driver.select_period("Q","2")
    driver.select_annex("div_label_pluc_01_02cnkd")
    for index, row in df.iterrows():
        # print(index)
        print(row)
        df.at[index,"Status"]="Done"
        driver.fill_form(index,row)
        time.sleep(1)
        driver.click_element("/html/body/div[2]/form/div/div[2]/div[4]/input[1]")
        # driver.switch_to_main()
        # driver.click_button("themDong")
    # driver.save_draft("/html/body/div[3]/input[4]")
    driver.switch_to_main()
    # driver.get("https://canhan.gdt.gov.vn/ICanhan/Request#")

    # Nhap thong tin khai bao ban dau

    # Chuyen den trang co phu luc

    # Vong lap cho den khi het file
        # Dien du lieu vao dong file
        # Danh dau vao trong file moi
        # Them dong moi

    # Luu nhap

    


if __name__ == "__main__":
    main()