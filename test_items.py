link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_basket(browser):
    browser.implicitly_wait(10)
    browser.get(link)
    basket = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert basket, 'Кнопка не найдена'

