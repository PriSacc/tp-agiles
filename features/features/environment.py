from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = r"/home/prittylimon/drivers/chromedriver_linux64/chromedriver"

#se baja desde aca https://chromedriver.storage.googleapis.com/index.html?path=88.0.4324.96/ ,se descomprime y es un .exe que despues se referencia en el driver

def before_all(context):
    context.browser = webdriver.Chrome(executable_path=driver)   