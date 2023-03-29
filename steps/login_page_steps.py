from behave import*
@given('Home page: I open karpaten home_page')
def step_impl(context):
    context.login_object.navigate_to_home_page()

@when('Home page: I go to login_page by click Contul meu')
def step_impl(context):
    context.base_page_object.go_to_login_page()

@when('Login page: I send an invalid e-mail and password')
def step_impl(context):
    context.login_object.send_invalid_email_and_password()

@when('Login page: I click on the button: Intra in cont')
def step_impl(context):
    context.login_object.click_button_intra_in_cont()

@then('Login page: I verify if the error is "Date de autentificare invalide."')
def step_impl(context):
    context.login_object.verify_the_error()
