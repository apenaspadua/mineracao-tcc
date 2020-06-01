from selenium import webdriver
import pymysql
from selenium.webdriver import ActionChains
from random import randint
import time
import re

from Scripts.DatabaseModel import DatabaseModel

# inicializando MySQL
db = pymysql.connect("localhost", "root", "endgame123", "base_tcc")

# instancia do modelo
databaseModel = DatabaseModel()

# inicializando webdriver
chrome = webdriver.Chrome()
chrome.get('https://interacoesmedicamentosas.com.br/interacoes.php')


def formatString(dataItem):
    data = dataItem[7:-1]
    replaceData = data.replace(",", "")
    formatData = replaceData.replace("'", "")
    return formatData


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


def backToList():
    back = chrome.find_element_by_id('voltar')
    ActionChains(chrome).click(back).perform()


def postToDatabase(databaseModel):
    cursor = db.cursor()
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
    db.commit()
    print("Record inserted successfully!\n")


    # cursor.connection.ping()
    # with cursor.connection as cursor:
    #     cursor.execute(sql,
    #     db.close()
    #     print("deu certo")


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
