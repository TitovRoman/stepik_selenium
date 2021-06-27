import time
import unittest

from selenium import webdriver


class TestUniqueSelectors(unittest.TestCase):
    def base_test(self, link):
        try:
            browser = webdriver.Chrome()
            browser.get(link)

            first_name = browser.find_element_by_xpath('//label[contains(text(), "First name")]/following::input')
            first_name.send_keys('Name')
            last_name = browser.find_element_by_xpath('//label[contains(text(), "Last name")]/following::input')
            last_name.send_keys('Last Name')
            email = browser.find_element_by_xpath('//label[contains(text(), "Email")]/following::input')
            email.send_keys('Email')

            button = browser.find_element_by_tag_name('button')
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element_by_tag_name("h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

        finally:
            time.sleep(2)
            browser.quit()

    def test_url1(self):
        self.base_test('http://suninjuly.github.io/registration1.html')

    def test_url2(self):
        self.base_test('http://suninjuly.github.io/registration2.html')
