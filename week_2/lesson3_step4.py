import math
import os
import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_tag_name('button').click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    input_el = browser.find_element_by_id('answer')
    input_el.send_keys(y)

    button = browser.find_element_by_tag_name('button')
    button.click()

    time.sleep(1)

    print(Alert(browser).text.split()[-1])
finally:
    time.sleep(2)
    browser.quit()