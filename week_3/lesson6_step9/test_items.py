import time


def test_add_to_basket_button(browser):
    url = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(url)
    time.sleep(4)
    button = browser.find_elements_by_class_name('btn-add-to-basket')
    assert len(button) == 1, 'The page must have one add to cart button'
