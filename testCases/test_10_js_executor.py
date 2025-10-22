def test_js_executor(setup):
    setup.get("https://demoqa.com")
    title = setup.execute_script("return document.title;")
    assert isinstance(title, str)
