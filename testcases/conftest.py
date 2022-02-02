import time

import pytest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="class")
def setup(request):
    # assert 2 + 2 == 4
    print("HI DATA")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    wait = WebDriverWait(driver, 0)
    driver.get("http://10.81.1.227:8000")
    driver.maximize_window()
    request.cls.driver = driver
    request.cls.wait = wait
    time.sleep(2)
    # print('Hi')
    yield
    # driver.close()
