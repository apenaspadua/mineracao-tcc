from selenium import webdriver
import pymysql
from selenium.webdriver import ActionChains
from random import randint
import time
import re


# inicializando MySQL
db = pymysql.connect("localhost", "root", "endgame123", "base_tcc")


def formatString(dataItem):
    data = dataItem[7:-1]
    replaceData = data.replace(",", "")
    formatData = replaceData.replace("'", "")
    return formatData


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
            data = items[index].get_attribute("onclick")
            id_item = formatString(data)
            id = int(re.search(r'\d+', id_item).group(0))
            print(id)
        else:
            chrome.execute_script('getDados()')
            time.sleep(3)
            element = chrome.find_element_by_id('resultado')
            print(element.text + '\n')
            back = chrome.find_element_by_id('voltar')
            ActionChains(chrome).click(back).perform()
            cont = 0


main()
