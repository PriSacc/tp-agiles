from behave import *
from behave_webdriver.steps import *
from urllib.parse import urljoin

@given('I send a {method} request to the page "{page}"')
def send_request_page(context, method, page):
    url = urljoin(context.base_url, page)
    context.response = BehaveRequestDriver().request(method, url)

@then('I expect the response text contains "{text}"')
def check_response_text_contains(context, text):
    assert text in context.response.text