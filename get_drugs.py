from selenium import webdriver
import pymysql
import re

# inicializando MySQL
db = pymysql.connect("localhost", "root", "endgame123", "base_tcc")


# formatando a string
def formatString(dataItem):
    data = dataItem[7:-1]
    replaceData = data.replace(",", "")
    formatData = replaceData.replace("'", "")
    return formatData


# post pro banco de dados
def postToDatabase(id, item):
    cursor = db.cursor()

    sql = "INSERT INTO medicamentos (id, nome_descricao) VALUES (%s, %s)"
    cursor.connection.ping()
    with cursor.connection as cursor:
        cursor.execute(sql, (int(id), item))
    db.close()


def main():
    # instanciando o site
    chrome = webdriver.Chrome()
    chrome.get('https://interacoesmedicamentosas.com.br/interacoes.php')

    # identificando os elementos da pagina
    drugList = chrome.find_element_by_id("lista")
    items = drugList.find_elements_by_tag_name("li")

    # varrendo lista de medicamdentos e mandando pro banco
    for item in items:
        data = item.get_attribute("onclick")
        id_item = formatString(data)
        id = int(re.search(r'\d+', id_item).group(0))
        item = " ".join(re.findall("[a-zA-Z-ã-é-â-ê-Á-í-ó]+", id_item))
        postToDatabase(id, item)
        print(id, item)


main()
