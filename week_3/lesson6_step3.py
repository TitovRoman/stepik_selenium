import math
import time

import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()

class TestAliens:
    @pytest.mark.parametrize('url', [
        'https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1',
    ])
    def test_url(self, browser, url):
        browser.get(url)
        input_answer = browser.find_element_by_class_name('string-quiz__textarea')
        input_answer.send_keys(str(math.log(int(time.time()))))

        button = browser.find_element_by_class_name('submit-submission')
        button.click()

        feedback = browser.find_element_by_class_name('smart-hints__feedback').text
        assert feedback == 'Correct!', f"Feedback message != 'Correct!'. {feedback=}"
