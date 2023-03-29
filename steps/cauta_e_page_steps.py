from behave import *

@when('Home page: I search "Kleopatra Royal" from the Cauta destinatie, hotel')
def step_impl(context):
    context.evaluation_object.search_for_hotel()

@then('Oferta Cazare page: I verify if the tourist evaluation is "Foarte bine"')
def step_impl(context):
    context.evaluation_object.verify_the_evaluation()
