from playwright.sync_api import Page, expect

def test_click_on_elements_and_check_navigation(page: Page):
    page.goto("https://demoqa.com/ ", wait_until="domcontentloaded", timeout=60000)
    page.click("text=Elements")

    # Проверяем, что мы на нужной странице, через элемент
    expect(page.get_by_text("Text Box", exact=True)).to_be_visible()


def test_text_boxes_are_visible(page: Page):
    page.goto("https://demoqa.com/elements ", wait_until="domcontentloaded", timeout=60000)
    textbox = page.get_by_text("Text Box", exact=True)
    expect(textbox).to_be_visible()