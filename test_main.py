from selenium import webdriver # webdriver это и есть набор команд для управления браузером
from selenium.webdriver.common.by import By # импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

@pytest.mark.parametrize('city', ["Moscou", "Москва", "Тула"])
def test_guest_should_see_login_link(city):
    
    link = "http://127.0.0.1:5000/"
    browser = webdriver.Chrome()
    browser.get(link)    # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке    

    name_city = browser.find_element(By.ID, "name_city")
    name_city.clear()
    name_city.send_keys(city)

    but = browser.find_element(By.ID, "but_ok")
    but.click() 
    time.sleep(10)
    text_pred = browser.find_element(By.ID, "pred") #browser.find_element(By.ID, "ember518")  #ember510           #ember517
    print(text_pred.text)

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    #but3 = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.CLASS_NAME, ".submit-submission"))) # #ember504 > div > section > div > div.attempt__inner > div.attempt__actions > button

    #time.sleep(10)
    assert "Температура воздуха" in text_pred.text
