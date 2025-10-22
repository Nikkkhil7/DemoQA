def test_window_handling(setup):
    setup.get("https://demoqa.com")
    setup.execute_script("window.open('https://demoqa.com/automation-practice-switch-windows')")
    handles = setup.window_handles
    assert len(handles) >= 2
    setup.switch_to.window(handles[-1])
    setup.close()
    setup.switch_to.window(handles[0])
    assert True
