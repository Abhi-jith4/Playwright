import pytest
from playwright.sync_api import sync_playwright

def test_google_url():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)  

        context=browser.new_context()
        page=context.new_page()
        page.goto("https://google.com/")
        assert page.url=="https://www.google.com/", f"Expected URL to be 'https://www.google.com/', but got '{page.url}'"
        browser.close()