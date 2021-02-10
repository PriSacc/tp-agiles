from behave import given, when, then

@given(u'Que ingreso al juego')
def step_impl(context):
    context.behave_driver.get('https://localhost:3000')

@when(u'Arriesgo una palabra erronea')
def step_impl(context):
    context.browser.find_element_by_xpath(f'/html/body/div/div/div/div[2]/div/div/form[2]/div/div[1]/div/input').send_keys('--')
    #context.browser.find_element_by_name('ingreso').send_keys('NombreUsuario')
    context.browser.find_element_by_xpath(f"/html/body/div/div/div/div[2]/div/div/form[2]/div/div[2]/button").click()
    
@then(u'Juego perdido')
def step_impl(context):
    text = context.browser.find_element_by_xpath(f"/html/body/div/div/div/div[2]/div/div/h1").text
    assert text[:18] == "No re vimo wachim"