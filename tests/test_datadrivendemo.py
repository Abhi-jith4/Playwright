import re
from playwright.sync_api import Page, expect
import pytest

def get_csv_data()->list:
    import csv
    data=[]
    with open("test_data.csv") as f:
        reader=csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            data.append(row)    
    return data

def get_json_data()->list:
    import json
    with open("test_data/data.json") as f:
        data=json.load(f)
    return [(item["username"], item["password"]) for item in data]

@pytest.mark.parametrize(
    "username, password",
    get_json_data(),
)    

def test_example(page: Page, username , password) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.get_by_placeholder("Username").click()
    page.get_by_placeholder("Username").fill(username)
    page.get_by_placeholder("Password").click()
    page.get_by_placeholder("Password").fill(password)
    page.get_by_role("button", name="Login").click()
    expect(page.get_by_role("link", name="Dashboard")).to_be_visible()
