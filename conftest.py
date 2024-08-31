import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser_name", action='store', default="firefox",
                     help="Choose browser: chrome or firefox")

# создадим фикстуру browser, которая будет создавать объект WebDriver
@pytest.fixture(scope="function") # область видимости (фикстура будет вызываться один раз для тестового метода)
def browser(request):                      
    browser_name = request.config.getoption("browser_name")      
    #browser = None
    link = "http://127.0.0.1:5000/"
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":        
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox() # service=FXService('/usr/bin/firefox')
    browser.get(link)
    #else:
    #    raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()