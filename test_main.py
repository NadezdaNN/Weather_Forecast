# pytest -s -v test_main.py
# pytest -s -v --browser_name=chrome test_main.py

from selenium import webdriver # webdriver это и есть набор команд для управления браузером
from selenium.webdriver.common.by import By # импортируем класс By, который позволяет выбрать способ поиска элемента
#from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service as FXService
import time
import pytest

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")

# создадим фикстуру browser, которая будет создавать объект WebDriver
'''@pytest.fixture(scope="function") # область видимости (фикстура будет вызываться один раз для тестового метода)
def browser(request):                      
    browser_name = request.config.getoption("browser_name")
    browser = None
    link = "http://127.0.0.1:5000/"
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":        
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(service=FXService('/usr/bin/firefox'))
    browser.get(link)
    #else:
    #    raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()'''


# создадим фикстуру browser, которая будет создавать объект WebDriver
@pytest.fixture(scope="function") # область видимости (фикстура будет вызываться один раз для тестового метода)
def browser(request):        
    print("\nstart browser for test..")
    link = "http://127.0.0.1:5000/"    
    browser = webdriver.Chrome()
    browser.get(link) # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке 
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('city', ["Moscou", "Москва", "Тула"]) # pytest -s -v -m parametrize test_main.py
def test_name_city(browser, city):  

    name_city = browser.find_element(By.ID, "name_city")
    name_city.clear()
    name_city.send_keys(city)

    but = browser.find_element(By.ID, "but_ok")
    but.click() 
    time.sleep(1)
    text_pred = browser.find_element(By.ID, "pred") #browser.find_element(By.ID, "ember518")  #ember510           #ember517
    print(text_pred.text)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    #but3 = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, ".submit-submission"))) # #ember504 > div > section > div > div.attempt__inner > div.attempt__actions > button

    #time.sleep(10)
    assert "Температура воздуха" in text_pred.text #, 'message' 
