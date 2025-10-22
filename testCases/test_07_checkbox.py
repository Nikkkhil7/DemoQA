from selenium.webdriver.common.by import By

def test_checkbox(setup):
    setup.get("https://demoqa.com/checkbox")
    setup.find_element(By.CSS_SELECTOR, "button[title='Expand all']").click()
    box = setup.find_element(By.XPATH, "//span[@class='rct-checkbox']")
    box.click()
    assert True
