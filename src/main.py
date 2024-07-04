from drivers.webInteraction import WebAutomation
from pandas_tools import file_processing
from datetime import datetime
from helpers import datehandler
def main():
    # driver = WebAutomation("C:/Users/taoda/tools/khaithue/src/drivers/chromedriver/chromedriver.exe")
    # Doc file excel
    df = file_processing.load_excel_data("src/input/data.xlsx")
    for index, row in df.iterrows():
        # print(index)
        print(row["Cot 1"])
        df.at[index,"Status"]="Done"
    
    file_processing.save_excel_data(df,f"src/output/data_{datehandler.current_toString()}.xlsx")

    #Khoi chay trinh duyet, dang nhap
    # driver = WebAutomation("src/drivers/chromedriver/chromedriver.exe")
    # driver.login("https://google.com","https://facebook.com")

    # Nhap thong tin khai bao ban dau

    # Chuyen den trang co phu luc

    # Vong lap cho den khi het file
        # Dien du lieu vao dong file
        # Danh dau vao trong file moi
        # Them dong moi

    # Luu nhap

    


if __name__ == "__main__":
    main()