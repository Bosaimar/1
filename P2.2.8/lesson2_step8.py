from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os

URL = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(URL)

    # Зполнение поля First name
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Ivan")
    # Зполнение поля Last name
    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("Petrov")
    # Зполнение поля Email
    input3 = browser.find_element_by_name("email")
    input3.send_keys("Smolensk@bt.ru")
    
    # Добавление файла
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    element = browser.find_element_by_name('file')
    element.send_keys(file_path)

    # изменение положения кнопки
    button = browser.find_element_by_xpath("//button[text()='Submit']")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла