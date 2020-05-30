from selenium import webdriver
import pymysql
from selenium.webdriver import ActionChains

# inicializando MySQL
db = pymysql.connect("localhost", "root", "endgame123", "base_tcc")


def postToDatabase(id, item):
    cursor = db.cursor()


def main():
    chrome = webdriver.Chrome()
    chrome.get('https://interacoesmedicamentosas.com.br/interacoes.php')

    drugList = chrome.find_element_by_id("lista")
    items = drugList.find_elements_by_tag_name("li")
    botao = chrome.find_element_by_id("botao")

    cont = 0

    for item in items:
        cont += 1
        if cont <= 2:
            ActionChains(chrome).click(item).perform()
        else:
            ActionChains(chrome).click(botao).perform()


main()
