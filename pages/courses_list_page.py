from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CoursesListPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('courses-list-toolbar-create-course-button')
        self.course_title = page.get_by_test_id('course-widget-title-text')
        self.course_image = page.get_by_test_id('course-preview-image')
        self.course_max_score_text = page.get_by_test_id('course-max-score-info-row-view-text')
        self.course_min_score_text = page.get_by_test_id('course-min-score-info-row-view-text')
        self.course_estimated_time_text = page.get_by_test_id('course-estimated-time-info-row-view-text')


    def check_visible_courses_title(self):
        expect(self.courses_title).to_be_visible()
        expect(self.courses_title).to_have_text('Courses')


    def check_visible_create_course_button(self):
        expect(self.create_course_button).to_be_visible()


    def check_visible_course_card(self, index: int, title: str, max_score: str, min_score: str, estimated_time: str):
        expect(self.course_image.nth(index)).to_be_visible()
        fields = [
            (self.course_title, title),
            (self.course_max_score_text, f"Max score: {max_score}"),
            (self.course_min_score_text, f"Min score: {min_score}"),
            (self.course_estimated_time_text, f"Estimated time: {estimated_time}"),
        ]
        for locator, expected_text in fields:
            element = locator.nth(index)
            expect(element).to_be_visible()
            expect(element).to_have_text(expected_text)