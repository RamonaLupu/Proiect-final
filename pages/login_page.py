from selenium.webdriver.common.by import By
from pages.base_page import Base_page

class Login(Base_page):
    ACCEPT = (By.XPATH, '//*[@id="fairlane-cookie-consent"]/button')
    EMAIL = (By.ID, 'username')
    PAROLA = (By.ID, '_password')
    BUTTON_INTRA_IN_CONT = (By.XPATH, '//*[@id="main"]/div/article/section/div[2]/div/div[1]/form/div[3]/div[2]/div/button')
    EROARE = (By.XPATH, '//*[@id="main"]/div/article/section/div[2]/div/div[1]/form/div[1]')

    def navigate_to_home_page(self):
        self.chrom.get ('https://www.karpaten.ro/')
        # self.chrom.find_element(*self.ACCEPT).click()

    def send_invalid_email_and_password(self):
        self.chrom.find_element(*self.EMAIL).send_keys('lrcatalina')
        self.chrom.find_element(*self.PAROLA).send_keys('123.qwe.A')

    def click_button_intra_in_cont(self):
        self.chrom.find_element(*self.BUTTON_INTRA_IN_CONT).click()

    def verify_the_error(self):
        actual_error = self.chrom.find_element(*self.EROARE).text
        expected_error = 'Date de autentificare invalide.'
        assert actual_error == expected_error, f'Error: the error is not the expected one'

