import time

from selenium.webdriver.common.by import By
from pages.base_page import Base_page
from selenium.webdriver.support.select import Select

class Check_the_offers(Base_page):
    RADIO_BUTTON_AVION =(By.XPATH, '//*[@id="search-live-form"]/div[1]/div/div/div[1]/label[1]/span')
    DESTINATIE = (By.CLASS_NAME, 'select2-search__field')
    ORAS = (By.ID, 'search-oras-plecare')
    PERIOADA = (By.ID, 'search-data')
    BUTTON_CAUTA = (By.XPATH, '//*[@id="searchLiveFormBtn"]')
    SEARCH_RESULTS = (By.ID, 'total-items')


    def click_on_rodio_button_avion(self):
        self.chrom.find_element(*self.RADIO_BUTTON_AVION).click()

    def choose_destinatia(self):
        self.chrom.find_element(*self.DESTINATIE).send_keys('Antalya')
        self.chrom.find_element(By.ID, 'select2-search-live-destination-results')
        self.chrom.find_element(By.XPATH, '//*[@id="select2-search-live-destination-results"]/li[1]/ul/li[2]/div/div[2]').click()



    def choose_oras_plecare(self, oras_plecare):
        category_dropdown = Select(self.chrom.find_element(*self.ORAS))
        category_dropdown.select_by_visible_text(oras_plecare)


    def choose_perioada(self):
        self.chrom.find_element(*self.PERIOADA).click()
        time.sleep(3)
        self.chrom.find_element(By.XPATH, '//*[@id="litepicker-data"]/div/div[1]/div/div[2]/div[1]/button[2]').click()
        time.sleep(3)
        self.chrom.find_element(By.XPATH, '//*[@id="litepicker-data"]/div/div[1]/div/div[2]/div[3]/div[20]').click()
        time.sleep(3)
        self.chrom.find_element(By.XPATH, '//*[@id="litepicker-data"]/div/div[1]/div/div[2]/div[3]/div[27]').click()
        time.sleep(3)

    def click_button_cauta(self):
        self.chrom.find_element(*self.BUTTON_CAUTA).click()
        time.sleep(10)

    def check_the_results(self):
        results= self.chrom.find_element(*self.SEARCH_RESULTS).text
        assert int(results) >= 5, f'Error: There are not enough offers for you. Look for another destination.'




