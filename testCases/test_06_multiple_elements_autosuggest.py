from selenium.webdriver.common.by import By

def test_multiple_elements_and_autosuggest(setup):
    setup.get("https://demoqa.com/auto-complete")
    inp = setup.find_element(By.ID, "autoCompleteMultipleInput")
    inp.send_keys("Re")
    assert inp.get_attribute("value") is not None
