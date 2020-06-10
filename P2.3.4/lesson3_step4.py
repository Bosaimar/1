from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os
import math

URL = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(URL)

    # нажать на кнопку
    button = browser.find_element_by_tag_name('button')
    button.click()

    # Принять Confirm
    confirm = browser.switch_to.alert
    confirm.accept()

    # вычисление выражения
    def calc(x):
      return str(math.log(abs(12*math.sin(int(x)))))
    
    # получение значения x
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    
    # вызов функци вычисления выражения
    y = calc(x)
    
    # ввод значения 
    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)
	
	# Нажать кнопку Submit
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()




finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла