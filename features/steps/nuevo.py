from selenium import webdriver
from behave import *

@when('we visit Ahorcado UTN')
def step(context):
   context.browser.get('http://localhost:3000')

@then('it should have a title Ahorcado UTN')
def step(context):
   assert context.browser.title == "Ahorcado UTN"
    
   