import os, time

def test_screenshot(setup):
    setup.get("https://demoqa.com")
    os.makedirs("screenshots", exist_ok=True)
    path = os.path.join("screenshots", f"snap_{int(time.time())}.png")
    setup.save_screenshot(path)
    assert os.path.exists(path)
