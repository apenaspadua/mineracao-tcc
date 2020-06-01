import re
import time
from random import randint

import mysql.connector
from selenium import webdriver
from selenium.webdriver import ActionChains

from Scripts.DatabaseModel import DatabaseModel

# instancia do modelo
databaseModel = DatabaseModel()

# inicializando webdriver
chrome = webdriver.Chrome()
chrome.get('https://interacoesmedicamentosas.com.br/interacoes.php')


# formatando a string
def formatString(dataItem):
    data = dataItem[7:-1]
    replaceData = data.replace(",", "")
    formatData = replaceData.replace("'", "")
    return formatData


# desestruturando a string response do servidor
def destroyString(response):
    interacao = response[:3]
    lista = []
    i = 0
    identify = 0
    if interacao != "Não":
        for index in response:
            lista.insert(i, index)
            if "\n" in response[i]:
                prepareToPost(''.join(lista), identify)
                identify += 1
                lista.clear()
            i += 1

        postToDatabase(databaseModel)
    else:
        print("Sem interacao\n")


# atribuindo os valores para os atributos
def prepareToPost(item, identify):
    if identify == 0:
        databaseModel.nomePriMed = item.replace('\n', '')

    elif identify == 1:
        databaseModel.nomeSegMed = item.replace('\n', '')

    elif identify == 2:
        print('')

    elif identify == 3:
        databaseModel.gravidade = item[24:-1]

    elif identify == 4:
        databaseModel.inicio = item[21:-1]

    elif identify == 5:
        databaseModel.probabilidade = item[29:-1]

    elif identify == 6:
        databaseModel.efeito = item[8:-1]

    elif identify == 7:
        databaseModel.mecanismo = item[11: -1]

    elif identify == 8:
        databaseModel.sujestao = item[21:-1]


# clicar no botao pra voltar
def backToList():
    back = chrome.find_element_by_id('voltar')
    ActionChains(chrome).click(back).perform()


# post no banco de dados
def postToDatabase(databaseModel):
    global connection, cursor
    try:
        connection = mysql.connector.connect(host="localhost", database="base_tcc", user="root", password="endgame123")
        cursor = connection.cursor()
        sql = """INSERT INTO interacoes_medicamentos (id, id_primeiro_medicamento, id_segundo_medicamento, nome_primeiro_medicamento, nome_segundo_medicamento, gravidade_interacao, inicio_interacao, prop_ocorrencia, efeito, mecanismo, sujestao_conduta)
              VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        recordTuple = ((databaseModel.getId,
                        databaseModel.getIdPriMed,
                        databaseModel.getIdSegMed,
                        databaseModel.getNomePriMed,
                        databaseModel.getNomeSegMed,
                        databaseModel.getGravidade,
                        databaseModel.getInicio,
                        databaseModel.getProb,
                        databaseModel.getEfeito,
                        databaseModel.getMecanismo,
                        databaseModel.getSujestao))
        cursor.execute(sql, recordTuple)
        connection.commit()
        print("-------------------------------")
        print("Record inserted successfully!")
        print("-------------------------------\n")

    except mysql.connector.Error as error:
        print("-------------------------------")
        print("Failed to insert record into {}".format(error))
        print("-------------------------------\n")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed\n")


def main():
    drugList = chrome.find_element_by_id("lista")
    items = drugList.find_elements_by_tag_name("li")

    cont = 0

    while True:
        cont += 1
        index = randint(0, 1040)
        databaseModel.id = randint(0, 9999)
        if cont <= 2:
            ActionChains(chrome).click(items[index]).perform()
            data = items[index].get_attribute("onclick")
            id_item = formatString(data)
            id = int(re.search(r'\d+', id_item).group(0))
            if cont == 1:
                databaseModel.idPriMed = int(id)
            else:
                databaseModel.idSegMed = int(id)
            print(id)
        else:
            chrome.execute_script('getDados()')
            time.sleep(3)
            element = chrome.find_element_by_id('resultado')
            destroyString(element.text + "\n")
            backToList()
            cont = 0


main()
