import time
from selenium import webdriver
from selenium.webdriver.common.by import By

my_data = {
'Data1':{'Firstname': 'Dion', 'Lastname': 'James', 'Age': 28, 'Email': 'dionj@gmail.com', 'Salary': 2000000, 'Departement': 'Store'},
'Data2':{'Firstname': 'Loli', 'Lastname': 'Taxi', 'Age': 23, 'Email': 'lolita@gmail.com', 'Salary': 3000000, 'Departement': 'Logistic'},
'Data3':{'Firstname': 'John', 'Lastname': 'Son', 'Age': 38, 'Email': 'Johnson@gmail.com', 'Salary': 5000000, 'Departement': 'Head'}
}
url = 'https://demoqa.com/webtables'

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

for x in my_data:
    driver.find_element(By.XPATH, "//button[@id= 'addNewRecordButton']").click()
    driver.find_element(By.XPATH, "//input[@id= 'firstName']").send_keys(my_data[x]["Firstname"])
    driver.find_element(By.XPATH, "//input[@id= 'lastName']").send_keys(my_data[x]["Lastname"])
    driver.find_element(By.XPATH, "//input[@id= 'userEmail']").send_keys(my_data[x]["Email"])
    driver.find_element(By.XPATH, "//input[@id= 'age']").send_keys(my_data[x]["Age"])
    driver.find_element(By.XPATH, "//input[@id= 'salary']").send_keys(my_data[x]["Salary"])
    driver.find_element(By.XPATH, "//input[@id= 'department']").send_keys(my_data[x]["Departement"])
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@id= 'submit']").click()
    # print(my_data[x]["Firstname"])

driver.close()