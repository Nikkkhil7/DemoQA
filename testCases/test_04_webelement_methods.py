from selenium.webdriver.common.by import By

def test_webelement_methods(setup):
    setup.get("https://demoqa.com/text-box")
    name = setup.find_element(By.ID, "userName")
    assert name.is_displayed()
    assert name.is_enabled()
    name.send_keys("Automation")
    assert "Automation" in name.get_attribute("value")
