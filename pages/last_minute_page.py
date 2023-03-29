from selenium.webdriver.common.by import By
from pages.base_page import Base_page

class Url_check(Base_page):
    LAST_MINUTE = (By.XPATH, '//img[@alt="Last minute"]')
    LOGO = (By.XPATH, '//img[@alt="Agentie de Turism 2023"]')
    URL_HOME_PAGE = 'https://www.karpaten.ro/'

    def go_last_minute_page(self):
        self.chrom.find_element(*self.LAST_MINUTE).click()

    def click_logo(self):
        self.chrom.find_element(*self.LOGO).click()

    def verify_the_url(self):
        url_home_page = 'https://www.karpaten.ro/'
        assert self.chrom.current_url == url_home_page, 'Error: This is not the home_page!'