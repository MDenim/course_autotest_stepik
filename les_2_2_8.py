import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
	link = "http://suninjuly.github.io/file_input.html"
	browser  = webdriver.Chrome()
	browser.get(link)
	input1 = browser.find_element_by_css_selector("input[name='firstname']")
	input1.send_keys("Ivan")
	input2 = browser.find_element_by_css_selector("input[name='lastname']")
	input2.send_keys("Petrov")
	input3 = browser.find_element_by_css_selector("input[name='email']")
	input3.send_keys("Smolensk")
		
	current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
	file_path = os.path.join(current_dir,'test.txt')           # добавляем к этому пути имя файла 
	input4 = browser.find_element_by_css_selector("#file")
	input4.send_keys(file_path)	
	
	#Нажать на кнопку Submit.
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
		
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла