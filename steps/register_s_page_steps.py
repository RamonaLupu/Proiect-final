from behave import*

@when('Home page: I go to login_page')
def step_impl(context):
    context.base_page_object.go_to_login_page()


@when('Login page: I click on Creeaza cont')
def step_impl(context):
    context.base_page_object.go_to_creeaza_cont()


@when('Register page: I send a Nume')
def step_impl(context):
    context.register_successful_object.send_nume()


@when('Register page: I send an Prenume')
def step_impl(context):
    context.base_page_object.send_prenume()


@when('Register page: I send an adress mail')
def step_impl(context):
    context.base_page_object.send_email()


@when('Register page: I send  password on the textbox Parola')
def step_impl(context):
    context.base_page_object.send_parola()


@when('Register page: I resend the same password on the textBox Verificare parola')
def step_impl(context):
    context.base_page_object.confirm_parola()


@then('Register page: I verify if the message for successful register is displayed')
def step_impl(context):
    context.register_successful_object.verify_the_successful_message()