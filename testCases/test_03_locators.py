from selenium.webdriver.common.by import By

def test_locators(setup):
    setup.get("https://demoqa.com/text-box")
    el = setup.find_element(By.ID, "userName")
    el.clear()
    el.send_keys("Nikhil")
    assert el.get_attribute("value") == "Nikhil"
