from selenium.webdriver.common.by import By
from pages.base_page import Base_page

class Register_unsuccessful(Base_page):
    ERROR_REGISTER = (By.XPATH, '//*[@id="registrationFormResponse"]/div/div[2]')

    def leave_nume_empty(self):
        self.chrom.find_element(*self.NUME).send_keys('')

    def verify_error(self):
        actual_error = self.chrom.find_element(*self.ERROR_REGISTER).text
        expected_error = 'Va rog introduceti numele dvs.'
        assert actual_error == expected_error, f'Error: the error is not the expected one'

