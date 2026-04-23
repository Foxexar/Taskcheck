from playwright.sync_api import sync_playwright
import requests
import os

URL = "https://bitjita.com/players/1297036692699954158/traveler-tasks"
WEBHOOK = os.environ["WEBHOOK"]

def fetch_page_text():
    with sync_playwright() as p:
        browser = p.chromium.launch(args=["--no-sandbox"])
        page = browser.new_page()

        page.goto(URL, timeout=60000, wait_until="domcontentloaded")
        page.wait_for_timeout(3000)  # ensures JS-rendered content loads

        text = page.inner_text("body").lower()

        browser.close()
        return text

text = fetch_page_text()

if ("brick slabs" in text) and ("construction level 60-120" in text):
    requests.post(WEBHOOK, json={
        "content": "Brico slab task detected"
    })
