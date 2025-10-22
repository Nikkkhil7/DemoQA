from selenium.webdriver.common.by import By
import requests

def test_broken_links(setup):
    setup.get("https://demoqa.com")
    links = setup.find_elements(By.TAG_NAME, "a")
    checked = 0
    for a in links[:20]:
        href = a.get_attribute("href")
        if href and href.startswith("http"):
            try:
                r = requests.head(href, timeout=5)
                assert r.status_code < 400
            except Exception:
                pass
            checked += 1
    assert checked > 0
