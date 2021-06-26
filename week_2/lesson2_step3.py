import math
import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select

link = "http://suninjuly.github.io/selects2.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    summa = int(num1) + int(num2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(summa))  # ищем элемент с текстом "Python"

    browser.find_element_by_tag_name('button').click()

    time.sleep(1)

    print(Alert(browser).text.split()[-1])
finally:
    time.sleep(2)
    browser.quit()