from selenium.webdriver.common.by import By
from pages.base_page import Base_page

class Logo_check(Base_page):
    DESPRE_NOI = (By.XPATH, '//*[@id="topbar"]/ul/li[2]/a')
    LOGO = (By.XPATH, '//img[@alt="Agentie de Turism 2023"]')

    def go_despre_noi_page(self):
        self.chrom.find_element(*self.DESPRE_NOI).click()

    def verify_the_logo(self):
        assert self.chrom.find_element(*self.LOGO).is_displayed()