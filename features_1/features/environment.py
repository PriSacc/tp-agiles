from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = r"C:\drivers\chromedriver.exe"

#se baja desde aca https://chromedriver.storage.googleapis.com/index.html?path=88.0.4324.96/ ,se descomprime y es un .exe que despues se referencia en el driver

def before_all(context):
    context.browser = webdriver.Chrome(executable_path=driver)
   