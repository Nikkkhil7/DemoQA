def test_scroll(setup):
    setup.get("https://demoqa.com")
    setup.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    setup.execute_script("window.scrollTo(0, 0);")
    assert True
