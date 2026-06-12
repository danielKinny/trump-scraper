import json
from playwright.sync_api import sync_playwright

def extract_message(truth_info):
    return truth_info["content"]


def tester():
    with sync_playwright() as p:
        chrome = p.chromium.launch(headless=False)
        page_context = chrome.new_context()
        page = page_context.new_page()

        def processor(res):
            if "statuses" in res.url and res.status==200:
                try:
                    data = res.json()
                    open("data.txt", "w").write(json.dumps(data, indent=4))
                    for truth in data:
                        print(extract_message(truth))
                except Exception as e:
                    print(e)

        page.on("response", processor)
        page.goto("https://truthsocial.com/@realDonaldTrump")
        page.wait_for_timeout(10000)
        chrome.close()

tester()