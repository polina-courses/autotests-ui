from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    # Открываем браузер и создаем новую страницу
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Переходим на страницу входа
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем поле email
    email_input = page.locator('//input[@id=":r0:"]')
    email_input.fill("user.name@gmail.com")

    # Заполняем поле username
    email_input = page.locator('//input[@id=":r1:"]')
    email_input.fill("username")

    # Заполняем поле пароль
    password_input = page.locator('//input[@id=":r2:"]')
    password_input.fill("password")

    # Нажимаем на кнопку Registration
    reg_button = page.get_by_test_id('registration-page-registration-button')
    reg_button.click()

    # Проверяем, что переход выполнен успешно
    h6_locator = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(h6_locator).to_be_visible()
    expect(h6_locator).to_have_text("Dashboard")