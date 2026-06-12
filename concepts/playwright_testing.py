import json
from playwright.sync_api import sync_playwright

def tester():
    with sync_playwright() as p:
        chrome = p.chromium.launch(headless=False)
        page_context = chrome.new_context()
        page = page_context.new_page()

        def processor(res):
            if "statuses" in res.url and res.status==200:
                print("found api endpoint")

                try:
                    data = res.json()
                    open("data.txt", "w").write(json.dumps(data, indent=4))
                    print(json.dumps(data, indent=4))
                except Exception as e:
                    print(e)

        page.on("response", processor)
        page.goto("https://truthsocial.com/@realDonaldTrump")
        page.wait_for_timeout(10000)
        chrome.close()

tester()