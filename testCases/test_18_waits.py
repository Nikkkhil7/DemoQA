from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_waits(setup):
    setup.get("https://demoqa.com/dynamic-properties")
    WebDriverWait(setup, 10).until(EC.element_to_be_clickable((By.ID, "enableAfter")))
    assert True
