from selenium.webdriver.common.by import By

def test_frame_handling(setup):
    setup.get("https://demoqa.com/frames")
    frames = setup.find_elements(By.TAG_NAME, "iframe")
    if frames:
        setup.switch_to.frame(frames[0])
        setup.switch_to.default_content()
    assert True
