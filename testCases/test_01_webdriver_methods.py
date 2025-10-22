def test_webdriver_methods(setup):
    setup.get("https://demoqa.com")
    url = setup.current_url
    title = setup.title
    handle = setup.current_window_handle
    assert url.startswith("https://")
    assert isinstance(title, str)
    assert isinstance(handle, str)
