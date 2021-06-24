import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    elements = browser.find_elements_by_tag_name('input')
    for element in elements:
        element.send_keys("Abra-Cadabra")

    browser.find_element_by_tag_name('button').click()
    print(Alert(browser).text.split()[-1])

finally:
    time.sleep(5)
    browser.quit()