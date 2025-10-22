# Selenium DemoQA Automation (PyTest + Allure)

This project contains automated Selenium tests (one file per concept) targeting DemoQA (https://demoqa.com).
It is configured to generate Allure results. Use `pytest --alluredir=allure-results` to run tests and collect results,
then `allure generate allure-results -o allure-report --clean` to build the HTML report.

## Structure
- testCases/        : one test file per concept (browser, locators, dropdown, alerts, etc.)
- conftest.py       : pytest fixture (Edge browser using webdriver-manager)
- pytest.ini
- requirements.txt
- .gitignore

## How to run locally
1. python -m venv .venv
2. source .venv/bin/activate  (Windows: .venv\Scripts\activate)
3. pip install -r requirements.txt
4. pytest
5. Install Allure CLI and run: allure serve allure-results  (or generate + open)

