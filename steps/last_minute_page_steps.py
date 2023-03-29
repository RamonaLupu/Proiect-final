from behave import*

@when(u'Home page: I go to LastMinute_page')
def step_impl(context):
    context.url_object.go_last_minute_page()


@when(u'LastMinute page: I click on the Logo')
def step_impl(context):
    context.url_object.click_logo()


@then(u'Home page: I verify the url home_page')
def step_impl(context):
    context.url_object.verify_the_url()
