from playwright.sync_api import Page, expect

def test_homepage_has_correct_title(page: Page):
    page.goto("https://demoqa.com/",wait_until="domcontentloaded", timeout=60000)
    expect(page).to_have_title("DEMOQA")


def test_homepage_has_elements_card_visible(page: Page):
    page.goto("https://demoqa.com/",wait_until="domcontentloaded", timeout=60000)

    # Проверяем, что карточка "Elements" видна
    elements_card = page.get_by_text("Elements", exact=True)
    expect(elements_card).to_be_visible()