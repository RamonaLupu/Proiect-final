from behave import*

@when ('Home page: I navigate to login_page by click Contul meu')
def step_impl(context):
    context.base_page_object.go_to_login_page()

@when('Login page: I click on the button: Creeaza cont')
def step_impl(context):
    context.base_page_object.go_to_creeaza_cont()

@when('Register page: I leave the textbox for Nume empty')
def step_impl(context):
    context.register_unsuccesful_object.leave_nume_empty()

@when('Register page: I send Prenume')
def step_impl(context):
    context.base_page_object.send_prenume()

@when ('Register page: I send Email')
def step_impl(context):
    context.base_page_object.send_email()

@when('Register page: I send a password on the textbox Parola')
def step_impl(context):
    context.base_page_object.send_parola()

@when('Register page: I resend the password on the textBox Verificare parola')
def step_impl(context):
    context.base_page_object.confirm_parola()

@when('Register page: I click on the button: Creeaza cont')
def step_impl(context):
    context.base_page_object.click_creeaza_cont()

@then('Register page: I verify if the error is "Va rog introduceti numele dvs."')
def step_impl(context):
    context.register_unsuccesful_object.verify_error()
