from behave import *

@when ('Home page: I click on Blog')
def step_impl(context):
    context.check_the_button_object.go_blog_page()

@when ('Blog Page: I click on button: Inapoi la site')
def step_impl(context):
    context.check_the_button_object.click_inapoi_button()

@then ('Home page: I verify if the currect url is "https://www.karpaten.ro/home/"')
def step_impl(context):
    context.check_the_button_object.verify_the_url()