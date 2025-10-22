from selenium.webdriver.common.by import By
import os

def test_file_upload_sendkeys(setup):
    setup.get("https://demoqa.com/upload-download")
    input_el = setup.find_element(By.ID, "uploadFile")
    tmp = os.path.abspath("temp_upload.txt")
    with open(tmp, "w") as f:
        f.write("hello")
    input_el.send_keys(tmp)
    assert True
