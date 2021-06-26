import math
import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select

link = "http://SunInJuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

def scrool_to(browser, element):
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)

try:
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('input_value').text
    y = calc(x)
    input_el = browser.find_element_by_id('answer')
    input_el.send_keys(y)

    robot_checkbox = browser.find_element_by_id('robotCheckbox')
    scrool_to(browser, robot_checkbox)
    robot_checkbox.click()

    robots_rule = browser.find_element_by_id('robotsRule')
    scrool_to(browser, robots_rule)
    robots_rule.click()

    button = browser.find_element_by_tag_name('button')
    scrool_to(browser, button)
    button.click()

    time.sleep(1)

    print(Alert(browser).text.split()[-1])
finally:
    time.sleep(2)
    browser.quit()