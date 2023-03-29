from selenium.webdriver.common.by import By
from pages.base_page import Base_page

class Register_successful(Base_page):
    SUCCESSFUL_MESSAGE = (By.XPATH, '//*[@id="main"]/div/article/section/div[2]/div/div[1]/form/div[1]')

    def send_nume(self):
        self.chrom.find_element(*self.NUME).send_keys('Popescu')

    def verify_the_successful_message(self):
        assert self.chrom.find_element(*self.SUCCESSFUL_MESSAGE).is_displayed()



