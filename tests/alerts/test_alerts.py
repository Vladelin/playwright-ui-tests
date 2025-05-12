from playwright.sync_api import Page
import time  # Для задержки

from playwright.sync_api import Page

from playwright.sync_api import Page

from playwright.sync_api import Page

def test_alert_accept(page: Page):
    page.set_default_timeout(40000)
    page.goto("https://demoqa.com/alerts ", wait_until="domcontentloaded", timeout=60000)

    # Ждём появление второй кнопки "Click me"
    page.wait_for_selector("text=Click me")
    second_button = page.locator("text=Click me").nth(1)

    # Кликаем по ней
    with page.expect_event('dialog') as alert:
        second_button.click()

    # Принимаем алерт
    dialog = alert.value
    dialog.accept()


def test_confirm_box_result(page: Page):
    page.set_default_timeout(30000)
    page.goto("https://demoqa.com/alerts ", wait_until="domcontentloaded", timeout=60000)

    # Ждём появления второй кнопки и кликаем
    second_button = page.locator("text=Click me").nth(1)
    page.wait_for_selector("text=Click me")  # Ждём, пока элементы станут видимыми
    second_button.click()

    # Принимаем confirm
    dialog = page.wait_for_event('dialog', timeout=30000)
    dialog.accept()
