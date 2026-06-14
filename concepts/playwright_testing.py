import json
from playwright.sync_api import sync_playwright
import html2text

def extract_message(truth_info):
    data,id = [],[]
    for truth in truth_info:
        if truth["content"] != "<p></p>" and "iran" in truth["content"].lower():
            data.append(truth["content"])
            id.append(truth["id"])
    return data,id

def converter(text):
    h = html2text.HTML2Text()
    return h.handle(text)

def tester():
    with sync_playwright() as p:
        chrome = p.chromium.launch(headless=False)
        page_context = chrome.new_context()
        page = page_context.new_page()

        def processor(res):
            if "statuses" in res.url and res.status==200:
                try:
                    data, id = extract_message(res.json())
                    for message in data:
                        print(converter(message))
                    
                    with open("concepts\\latest.txt", "a") as f:
                        for i in id:
                            f.write(i + "\n")
                        
                except Exception as e:
                    print(e)
                

        page.on("response", processor)
        page.goto("https://truthsocial.com/@realDonaldTrump")
        page.wait_for_timeout(10000)
        chrome.close()

tester()


#since data is coming as html maybe it is worthwhile to create a website for it but not right now