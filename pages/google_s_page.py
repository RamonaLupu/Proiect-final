import time

from selenium.webdriver.common.by import By
from pages.base_page import Base_page


class Google_valid_mail(Base_page):
    AUTENTIFICA_TE_CU_GOOGLE = (By.XPATH, '//*[text()="Autentifica-te cu Google"]')
    EMAIL_TEXTBOX = (By.ID, 'identifierId')
    INAINTE_BUTTON = (By.XPATH, '//*[@id="identifierNext"]/div/button/span')
    INCEARCA_BUTTON = (By.XPATH, '//*[@id="next"]/div/button/div[3]')

    def autentifica_te_cu_google(self):
        self.chrom.find_element(*self.AUTENTIFICA_TE_CU_GOOGLE).click()

    def send_valid_mail(self):
        self.chrom.find_element(*self.EMAIL_TEXTBOX).send_keys('lupuramonac@gmail.com')

    def click_inainte_button(self):
        self.chrom.find_element(*self.INAINTE_BUTTON).click()

    def verify_button_incearca(self):
        assert self.chrom.find_element(*self.INCEARCA_BUTTON).is_displayed()