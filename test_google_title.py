import pytest
from playwright.sync_api import sync_playwright

def test_google_title():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Set headless=True to hide the browser
        context = browser.new_context()
        page = context.new_page()

        page.goto("https://www.google.com")

        # Wait for the title to be available (Google may do redirects or show consent dialog)
        page.wait_for_load_state("load")
        title = page.title()

        assert "Google" in title, f"Expected 'Google' in title, but got '{title}'"

        browser.close()