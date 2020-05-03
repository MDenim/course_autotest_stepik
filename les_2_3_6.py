import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	link = "http://suninjuly.github.io/redirect_accept.html"
	browser  = webdriver.Chrome()
	browser.get(link)
	#Нажать на кнопку 
	button = browser.find_element_by_css_selector("button.trollface")
	button.click()	
	#Переключиться на новую вкладку
	browser.switch_to.window(browser.window_handles[1])
	#Считать значение для переменной x.
	x_element = browser.find_element_by_css_selector("#input_value")
	x = x_element.text
	#Посчитать математическую функцию от x (код для этого приведён ниже).
	y = calc(x)
	#Ввести ответ в текстовое поле.
	input1 = browser.find_element_by_css_selector('#answer')
	input1.send_keys(y)
	#Нажать на кнопку Submit.
	button = browser.find_element_by_css_selector("button.btn")
	button.click()
		
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла