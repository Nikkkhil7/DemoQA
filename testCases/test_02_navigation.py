def test_navigation(setup):
    setup.get("https://demoqa.com/text-box")
    setup.get("https://demoqa.com/checkbox")
    setup.back()
    setup.forward()
    setup.refresh()
    assert True
