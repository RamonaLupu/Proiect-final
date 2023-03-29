from selenium.webdriver.common.by import By
from pages.base_page import Base_page

class Button_check(Base_page):
    BLOG = (By.XPATH, '//*[text()="Blog"]')
    INAPOI_BUTTON = (By.XPATH, '//*[text()="Inapoi la site"]')

    def go_blog_page(self):
        self.chrom.find_element(*self.BLOG).click()

    def click_inapoi_button(self):
        self.chrom.find_element(*self.INAPOI_BUTTON).click()

    def verify_the_url(self):
        expected_url = 'https://www.karpaten.ro/home/'
        assert self.chrom.current_url == expected_url, 'Error: This is not the home_page!'