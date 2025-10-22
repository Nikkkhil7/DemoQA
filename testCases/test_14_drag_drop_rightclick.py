from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def test_drag_and_drop_and_rightclick(setup):
    setup.get("https://demoqa.com/droppable")
    src = setup.find_element(By.ID, "draggable")
    tgt = setup.find_element(By.ID, "droppable")
    ActionChains(setup).drag_and_drop(src, tgt).perform()
    setup.get("https://demoqa.com/buttons")
    btn = setup.find_element(By.ID, "rightClickBtn")
    ActionChains(setup).context_click(btn).perform()
    assert True
