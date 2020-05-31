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
    button = chrome.find_element_by_id("botao")

    cont = 0

    while True:
        cont += 1
        index = randint(0, 1040)
        if cont <= 2:
            ActionChains(chrome).click(items[index]).perform()
        else:
            cont = 0
            # ActionChains(chrome).click(button).perform()

            # window_after = chrome.window_handles[0]
            # chrome.switch_to.window(window_after)


main()
