from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def test_mouse_hover(setup):
    setup.get("https://demoqa.com/tool-tips")
    element = setup.find_element(By.ID, "toolTipButton")
    ActionChains(setup).move_to_element(element).perform()
    assert True
