from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

URL = " http://SunInJuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(URL)

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
    
    # установка чек-бокса I'm the robot
    option1 = browser.find_element_by_id('robotCheckbox')
    option1.click()
    
    # включение радиобатон Robots rule
    option1 = browser.find_element_by_id('robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", option1)
    option1.click()
    
    # изменение положения кнопки
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    #  "'button = document.getElementsByTagName(\"button\")[0]';'button.scrollIntoView(true)';"
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла