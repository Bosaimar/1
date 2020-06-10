from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

URL = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(URL)
    # вычисление выражения
    def calc(x,y):
      return str(int(x) + int(y))
    # получение первого значения выражения
    x_element = browser.find_element_by_css_selector('span#num1.nowrap')
    x = x_element.text
    # получение второго значения выражения
    y_element = browser.find_element_by_css_selector('span#num2.nowrap')
    y = y_element.text 
    # вызов функци вычисления выражения
    s = calc(x,y)
    # выбор значения из выпадающего списка
    select = Select(browser.find_element_by_css_selector('select#dropdown'))
    select.select_by_value(s)
    

    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла