from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Открыть браузер с интерфейсом
    page = browser.new_page()
    page.goto("https://demoqa.com/", timeout=60000)
    print("Заголовок страницы:", page.title())
    browser.close()