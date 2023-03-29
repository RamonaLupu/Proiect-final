import time

from browser import Browser
from selenium.webdriver.common.by import By

class Base_page(Browser):
    CONTUL_MEU = (By.XPATH, '//*[@id="topbar"]/ul/li[8]/a')
    BUTTON_CREEAZA_CONT1 = (By.XPATH, '//*[@id="main"]/div/article/section/div[2]/div/div[1]/form/div[3]/div[1]/div/a')
    NUME = (By.ID, 'karpaten_registrationUserFormType_lastName')
    PRENUME = (By.ID, 'karpaten_registrationUserFormType_firstName')
    EMAIL_CONT = (By.ID, 'karpaten_registrationUserFormType_email')
    PAROLA_CONT = (By.ID, 'account-parola')
    VERIFICARE_PAROLA = (By.ID, 'account-conf-parola')
    BUTTON_CREEAZA_CONT2 = (By.ID, 'registrationFormBtn')

    def go_to_login_page(self):
         self.chrom.find_element(*self.CONTUL_MEU).click()

    def go_to_creeaza_cont(self):
        self.chrom.find_element(*self.BUTTON_CREEAZA_CONT1).click()

    def send_prenume(self):
        self.chrom.find_element(*self.PRENUME).send_keys('Ovidiu')

    def send_email(self):
        self.chrom.find_element(*self.EMAIL_CONT).send_keys('ovi@krpt.com')

    def send_parola(self):
        self.chrom.find_element(*self.PAROLA_CONT).send_keys('123.qwe.A')

    def confirm_parola(self):
        self.chrom.find_element(*self.VERIFICARE_PAROLA).send_keys('123.qwe.A')

    def click_creeaza_cont(self):
        self.chrom.find_element(*self.BUTTON_CREEAZA_CONT2).click()