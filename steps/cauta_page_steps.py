from behave import*

@when('Home page: I click on the Avion radio button')
def step_impl(context):
    context.check_object.click_on_rodio_button_avion()

@when('Home page: I search for destinatie')
def step_impl(context):
    context.check_object.choose_destinatia()

@when('Home page: I search "{oras_plecare}"')
def step_impl(context, oras_plecare):
    context.check_object.choose_oras_plecare(oras_plecare)

@when('Home page: I choose the date')
def step_impl(context):
    context.check_object.choose_perioada()

@when('Home page: I click on the button: Cauta')
def step_impl(context):
    context.check_object.click_button_cauta()

@then('Home page: I have at least 5 results returned')
def step_impl(context):
    context.check_object.check_the_results()





