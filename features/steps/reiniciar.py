# from selenium import webdriver
# from behave import *

# title_pre = 0

# @given('entrar en la web')
# def step_impl(context):
#     context.browser.get('http://localhost:3000')

# @when('se hace click en nuevo juego')
# def step(context):
#     title_pre  = context.browser.find_element_by_id('numperdido')
#     context.browser.find_element_by_id('admito').click()

# @then('se reinicia la partida')
# def step(context):
#     title  = context.browser.find_element_by_id('numperdido')
#     assert title == title_pre + 1
