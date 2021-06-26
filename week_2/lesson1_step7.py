import math
import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

link = "http://suninjuly.github.io/get_attribute.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure_img = browser.find_element_by_id('treasure')
    x = treasure_img.get_attribute('valuex')
    y = calc(x)
    input_el = browser.find_element_by_id('answer')
    input_el.send_keys(y)

    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()

    browser.find_element_by_tag_name('button').click()

    time.sleep(1)

    print(Alert(browser).text.split()[-1])
finally:
    time.sleep(2)
    browser.quit()