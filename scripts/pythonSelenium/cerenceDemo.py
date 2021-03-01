from selenium import webdriver
from PIL import Image
driver = webdriver.Chrome(executable_path="C:\\Users\\ishita_nigam\\IdeaProjects\\chromedriver.exe")
driver.maximize_window()
driver.get('https://www.cerence.com/home')

str1 = driver.find_element_by_class_name('bg-cover').text
str2 = driver.find_element_by_class_name('font-monserrat-48').text
with open('cerencedemo.txt', 'w', encoding='utf-8') as writer:
    writer.write(str1)
    writer.writelines('\n')
    writer.write(str2)
print(str1, str2, sep='\n')

driver.close()

