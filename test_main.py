import pytest
from selenium.webdriver.common.by import By # импортируем класс By, который позволяет выбрать способ поиска элемента
import time

@pytest.mark.parametrize('city', ["Moscou", "Москва", "Тула"]) # pytest -s -v -m parametrize test_main.py
def test_name_city(browser, city):  

    name_city = browser.find_element(By.ID, "name_city")
    name_city.clear()
    name_city.send_keys(city)

    but = browser.find_element(By.ID, "but_ok")
    but.click() 
    time.sleep(1)
    text_pred = browser.find_element(By.ID, "pred") 
    print(text_pred.text)

    assert "Температура воздуха" in text_pred.text
