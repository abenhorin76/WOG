# Script created with Selenium 4.27 version
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def test_scores_service(app_url):
    service = Service(executable_path="c:\\temp\\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.get(app_url)
    score_element = driver.find_element(By.ID, 'score')
    score_value = int(score_element.text)
    if 1<= score_value <= 1000:
            score_valid = True
    else:
        score_valid = False
    driver.quit()
    return score_valid


def main_function():
    test_result = test_scores_service('http://localhost:5000')
    if test_result:
        exit(0)
    else:
        exit(-1)

main_function()
