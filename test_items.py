import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    #check if there any text on add-button to a basket, if not - consider that there is no button or its displaying isn't correct
    text_of_submit = browser.find_element_by_css_selector("#add_to_basket_form button[type='submit']").text
    assert text_of_submit is not None, 'There is no text in submit button'

