from selenium import webdriver
from behave import *

@given('entrar en la pagina')
def step_impl(context):
    context.browser.get('http://localhost:3000')

@when('se arriesga una palabra para perder')
def step_impl(context):
    context.browser.find_element_by_id('A').click()
    context.browser.find_element_by_id('B').click()
    context.browser.find_element_by_id('D').click()
    context.browser.find_element_by_id('Z').click()
    context.browser.find_element_by_id('X').click()
    context.browser.find_element_by_id('Q').click()
    context.browser.find_element_by_id('H').click()
    context.browser.find_element_by_id('Ñ').click()
    context.browser.find_element_by_id('W').click()
    context.browser.find_element_by_id('T').click()
    context.browser.find_element_by_id('Y').click()
    context.browser.find_element_by_id('I').click()
    context.browser.find_element_by_id('L').click()
    context.browser.find_element_by_id('K').click()
    context.browser.find_element_by_id('V').click()
    context.browser.find_element_by_id('P').click()

# @then('se pierde la partida')
# def step_impl(context):
#    title = context.browser.find_element_by_xpath(f"/html/body/div[1]/div[1]/div[1]/div[1]/div/div[1]/a").text
#    print('El titulo es: ', title)
#    assert title == "Ahorcado UTN"

@then('se pierde la partida')
def step_impl(context):
   title  = context.browser.find_element_by_partial_link_text("perdido").text
   print('TITULO: ', title)
   assert title == "Has perdido"

# cambiar nounlist para que pase
@when('se arriesga una palabra para ganar')
def step_impl(context):
    context.browser.find_element_by_id('A').click()
    context.browser.find_element_by_id('H').click()
    context.browser.find_element_by_id('L').click()
    context.browser.find_element_by_id('O').click()

@then('se gana la partida')
def step_impl(context):
   title  = context.browser.find_element_by_partial_link_text("Ganaste").text
   print('TITULO: ', title)
   assert title == "Ganaste!"