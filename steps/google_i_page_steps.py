from behave import *

@when('Home page: I click Contul meu')
def step_impl(context):
    context.base_page_object.go_to_login_page()


@when('Login page: I click the button: Autentifica-te cu Google')
def step_impl(context):
    context.google_mail_object.autentifica_te_cu_google()


@when('Facebook page: I send an invalid e-mail')
def step_impl(context):
    context.google_mail_object.send_invalid_mail()


@when('Facebook page: I click the button: Inainte')
def step_impl(context):
    context.google_mail_object.click_inainte_button()


@then('Facebook page: I verify that the error is "Contul Google nu a fost găsit"')
def step_impl(context):
   context.google_mail_object.verify_error()
