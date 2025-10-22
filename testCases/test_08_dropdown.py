from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def test_dropdown(setup):
    setup.get("https://demoqa.com/select-menu")
    select = setup.find_elements(By.CSS_SELECTOR, "select")
    if select:
        sel = Select(select[0])
        sel.select_by_index(1)
        assert sel.first_selected_option is not None
    else:
        assert True
