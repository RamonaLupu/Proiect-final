from behave import *

@when('Home page: In the textbox of Cauta destinatie,hotel I write "Kleopatra Royal Palm Hotel Alanya"')
def step_impl(context):
    context.check_price_object.search_for_hotel()

@when('Oferta Cazare page: I check if the avion button is selected')
def step_impl(context):
    context.check_price_object.verify_avion_button()

@then('Oferta Cazare page: I verify if the starting price is less than 600€')
def step_impl(context):
    context.check_price_object.verify_the_price()