import time

from selenium.webdriver.common.by import By
from pages.base_page import Base_page

class Check_price(Base_page):
    CAUTA_DESTINATIE = (By.XPATH, '//span[@class ="text"]')
    AVION_BUTTON = (By.ID, 'tarife-avion-tab')
    PRICE = (By.XPATH, '//*[@id="hotel-info"]/div[2]/div[1]/div[2]/div[2]/div/div/span[2]')

    def search_for_hotel(self):
        self.chrom.find_element(*self.CAUTA_DESTINATIE).click()
        self.chrom.find_element(By.ID, 'topsearch').send_keys('kleopatra royal')
        self.chrom.find_element(By.XPATH, '//*[text()="Kleopatra Royal Palm Hotel, Alanya"]').click()

    def verify_avion_button(self):
        self.chrom.find_element(*self.AVION_BUTTON).is_selected()

    def verify_the_price(self):
        pret = self.chrom.find_element(*self.PRICE).text
        assert pret <= '600€', f'Error: The price is very high!'