from playwright.sync_api import Page, Locator, expect


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    def get_locator(self, nth: int = 0, **kwargs) -> Locator:
        # "Лениво" инициализируем локатор, подставляя динамические значения в шаблон
        locator = self.locator.format(**kwargs)
        return self.page.get_by_test_id(locator).nth(nth)  # Выбираем элемент по индексу

    def click(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        locator = self.get_locator(nth, **kwargs)
        expect(locator).to_have_text(text)
