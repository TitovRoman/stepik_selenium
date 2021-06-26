import math
import os
import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

link = "http://suninjuly.github.io/file_input.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def scrool_to(browser, element):
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    text_inputs = browser.find_elements_by_css_selector('input[type="text"]')
    for input_element in text_inputs:
        input_element.send_keys('qweqwe')

    file_input = browser.find_element_by_css_selector('input[type="file"]')
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, os.pardir, 'requirements.txt')
    file_input.send_keys(os.path.abspath(file_path))

    button = browser.find_element_by_tag_name('button')
    scrool_to(browser, button)
    button.click()

    time.sleep(1)

    print(Alert(browser).text.split()[-1])
finally:
    time.sleep(2)
    browser.quit()