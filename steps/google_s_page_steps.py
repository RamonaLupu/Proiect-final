from behave import *

@when('Home page: I navigate to login_page')
def step_impl(context):
    context.base_page_object.go_to_login_page()


@when('Login page: I click on the button: Autentifica-te cu Google')
def step_impl(context):
    context.google_valid_mail_object.autentifica_te_cu_google()


@when('Google page: I send my mail')
def step_impl(context):
    context.google_valid_mail_object.send_valid_mail()

@when('Google page: I click Inainte')
def step_impl(context):
    context.google_valid_mail_object.click_inainte_button()


@then('Google page: I verify that the button: Incearca din nou is displayed')
def step_impl(context):
    context.google_valid_mail_object.verify_button_incearca()
