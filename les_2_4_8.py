from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

try:
  browser.get("http://suninjuly.github.io/explicit_wait2.html")
  # говорим Selenium проверять в течение 15 секунд, пока цена не упадет до 100 
  WebDriverWait(browser, 15).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "100")
      )
  button = browser.find_element_by_css_selector("#book")
  button.click()
  #Переключиться на новую вкладку
  #browser.switch_to.window(browser.window_handles[1])
  #Считать значение для переменной x.
  x_element = browser.find_element_by_css_selector("#input_value")
  x = x_element.text
  #Посчитать математическую функцию от x (код для этого приведён ниже).
  y = calc(x)
  #Ввести ответ в текстовое поле.
  input1 = browser.find_element_by_css_selector('#answer')
  input1.send_keys(y)
  #Нажать на кнопку Submit.
  button = browser.find_element_by_css_selector("#solve")
  button.click()
  #assert "successful" in message.text
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла  