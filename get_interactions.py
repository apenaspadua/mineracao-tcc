from selenium import webdriver
import pymysql
from selenium.webdriver import ActionChains
from random import randint
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# inicializando MySQL
db = pymysql.connect("localhost", "root", "endgame123", "base_tcc")


def postToDatabase(id, item):
    cursor = db.cursor()


def main():
    chrome = webdriver.Chrome()
    chrome.get('https://interacoesmedicamentosas.com.br/interacoes.php')

    drugList = chrome.find_element_by_id("lista")
    items = drugList.find_elements_by_tag_name("li")

    cont = 0

    while True:
        cont += 1
        index = randint(0, 1040)
        if cont <= 2:
            ActionChains(chrome).click(items[index]).perform()
        else:
            chrome.execute_script('getDados()')
            element_present = EC.presence_of_element_located((By.ID, 'resultado'))
            WebDriverWait(chrome, 60).until(element_present)

            print(element_present)

            # chrome.execute_script("arguments[0].click();", WebDriverWait(chrome, 60).until(
            #     EC.element_to_be_clickable((
            #         By.CSS_SELECTOR, "#botao"))
            # ))
            # elem = chrome.find_element_by_xpath("//*")
            # source_code = elem.get_attribute("innerHTML")
            #
            # print(source_code)


main()
