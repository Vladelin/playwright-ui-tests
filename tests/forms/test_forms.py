from playwright.sync_api import Page, expect

def test_register_form_is_visible(page: Page):
    page.goto("https://demoqa.com/automation-practice-form ", wait_until="domcontentloaded", timeout=60000)
    form = page.locator("#userForm")
    expect(form).to_be_visible()


def test_submit_button_works(page: Page):
    page.goto("https://demoqa.com/automation-practice-form ", wait_until="domcontentloaded", timeout=60000)

    # Заполняем форму
    page.fill("#firstName", "John")
    page.fill("#lastName", "Doe")
    page.fill("#userEmail", "john@example.com")
    page.fill("#userNumber", "2435456857")
    page.fill("#currentAddress", "street something")

    # Открываем календарь
    page.click("#dateOfBirthInput")

    # Выбираем месяц (May)
    page.select_option(".react-datepicker__month-select", "May")

    # Выбираем год (2025)
    page.select_option(".react-datepicker__year-select", "2025")

    # Выбираем дату (12)
    page.click(".react-datepicker__day--012")

    # Проверяем, что дата установлена
    expect(page.locator("#dateOfBirthInput")).to_have_value("12 May 2025")

    # Кликаем Submit
    page.click("#submit")

