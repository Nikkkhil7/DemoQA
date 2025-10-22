from selenium.webdriver.common.by import By

def test_radio_button(setup):
    setup.get("https://demoqa.com/radio-button")
    yes = setup.find_element(By.XPATH, "//label[contains(text(),'Yes')]")
    yes.click()
    out = setup.find_element(By.CLASS_NAME, "text-success").text
    assert "Yes" in out
