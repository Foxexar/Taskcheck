from playwright.sync_api import sync_playwright
import requests, os

URL="https://bitjita.com/players/1297036692699954158/traveler-tasks"
WEBHOOK=os.environ["WEBHOOK"]

with sync_playwright() as p:
    b=p.chromium.launch()
    page=b.new_page()
    page.goto(URL, timeout=60000)
    html=page.content().lower()
    b.close()

if "brick slabs" in html and "construction level 60-120" in html:
    requests.post(WEBHOOK,json={"content":"Brico slab task detected"})
