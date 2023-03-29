from behave import*

@when('Home page: I go to Despre-noi_page by click Despre noi')
def step_impl(context):
    context.logo_object.go_despre_noi_page()


@then('Despre-noi page: I verify if the logo is displayed')
def step_impl(context):
    context.logo_object.verify_the_logo()
