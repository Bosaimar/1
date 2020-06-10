from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # Проверяем, что значение уменьшилось до нужного значения
    element = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))

    # Нажать кнопку
    button = browser.find_element_by_id("book")
    button.click()

    # Прокрутить страницу вверх
    browser.execute_script('window.scrollBy(0,100);')

    # вычисление выражения
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


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
