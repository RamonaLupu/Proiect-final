from selenium.webdriver.common.by import By
from pages.base_page import Base_page

class Check_evaluation(Base_page):
    CAUTA_DESTINATIE = (By.XPATH, '//span[@class ="text"]')
    HOTEL = (By.XPATH, '//*[text()="Kleopatra Royal Palm Hotel, Alanya"]')
    SCORE = (By.XPATH, '//*[@id="hotel-info"]/div[2]/div[1]/div[2]/div[1]/div[2]/div/div/span[2]/strong')

    def search_for_hotel(self):
        self.chrom.find_element(*self.CAUTA_DESTINATIE).click()
        self.chrom.find_element(By.ID, 'topsearch').send_keys('kleopatra royal')
        self.chrom.find_element(*self.HOTEL).click()

    def verify_the_evaluation(self):
        evaluation = self.chrom.find_element(*self.SCORE).text
        assert evaluation.__contains__('Foarte bine')
