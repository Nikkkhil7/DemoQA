from selenium.webdriver.common.by import By

def test_webtable(setup):
    setup.get("https://demoqa.com/webtables")
    rows = setup.find_elements(By.CSS_SELECTOR, ".rt-tr-group")
    assert len(rows) > 0
