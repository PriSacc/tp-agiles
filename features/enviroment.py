from selenium import webdriver # or any custom webdriver
from behave_webdriver.driver import BehaveDriverMixin
from seleniumrequests import RequestMixin # or your own mixin

class BehaveRequestDriver(BehaveDriverMixin, RequestMixin, webdriver.Chrome):
    pass

def before_all(context):
    context.behave_driver = BehaveRequestDriver()