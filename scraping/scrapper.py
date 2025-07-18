from playwright.sync_api import sync_playwright

def fetch_chapter(url, screenshot_path="chapter1.png"):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(url)
        content = page.inner_text("body")
        page.screenshot(path=screenshot_path)
        browser.close()
    return content
