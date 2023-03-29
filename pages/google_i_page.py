import time

from selenium.webdriver.common.by import By
from pages.base_page import Base_page

class Google_invalid_mail(Base_page):
    AUTENTIFICA_TE_CU_GOOGLE = (By.XPATH, '//*[text()="Autentifica-te cu Google"]')
    EMAIL_TEXTBOX = (By.ID, 'identifierId')
    INAINTE_BUTTON = (By.XPATH, '//*[@id="identifierNext"]/div/button/span')
    ERROR_EMAIL = (By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[2]/div[2]/div')

    def autentifica_te_cu_google(self):
        self.chrom.find_element(*self.AUTENTIFICA_TE_CU_GOOGLE).click()

    def send_invalid_mail(self):
        self.chrom.find_element(*self.EMAIL_TEXTBOX).send_keys('ramo')

    def click_inainte_button(self):
        self.chrom.find_element(*self.INAINTE_BUTTON).click()

    def verify_error(self):
        actual_error = self.chrom.find_element(*self.ERROR_EMAIL).text
        expected_error = 'Contul Google nu a fost găsit'
        assert str(actual_error) == expected_error, f'Error: the error is not the expected one'
