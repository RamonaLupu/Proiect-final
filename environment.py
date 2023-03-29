from browser import Browser
from pages.login_page import Login
from pages.base_page import Base_page
from pages.register_i_page import Register_unsuccessful
from pages.register_s_page import Register_successful
from pages.cauta_page import Check_the_offers
from pages.despre_noi_page import Logo_check
from pages.last_minute_page import Url_check
from pages.oferta_cazare_page import Check_price
from pages.cauta_e_page import Check_evaluation
from pages.google_i_page import Google_invalid_mail
from pages.google_s_page import Google_valid_mail
from pages.blog_page import Button_check


def before_all(context):
    context.browser = Browser()
    context.base_page_object = Base_page()
    context.login_object = Login()
    context.register_unsuccesful_object = Register_unsuccessful()
    context.register_successful_object = Register_successful()
    context.check_object = Check_the_offers()
    context.logo_object = Logo_check()
    context.url_object = Url_check()
    context.check_price_object = Check_price()
    context.evaluation_object = Check_evaluation()
    context.google_mail_object = Google_invalid_mail()
    context.google_valid_mail_object = Google_valid_mail()
    context.check_the_button_object = Button_check()

def after_all(context):
    context.browser.close()