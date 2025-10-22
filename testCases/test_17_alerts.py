from selenium.webdriver.common.by import By

def test_alerts(setup):
    setup.get("https://demoqa.com/alerts")
    setup.find_element(By.ID, "alertButton").click()
    alert = setup.switch_to.alert
    text = alert.text
    alert.accept()
    assert text != ''
