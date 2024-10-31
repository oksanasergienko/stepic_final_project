from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="Choose browser language")

@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    print(f"\nstart browser for test in {language} language..")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()
