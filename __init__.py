from selenium import webdriver
from firebase import firebase

# inicializando Firebase
firebaseInstance = firebase.FirebaseApplication("https://interacoes-medicamentosas.firebaseio.com/", None)


def postToDatabase(item):
    drug_data = {
        'name': item
    }
    response = firebaseInstance.post('/Drugs/', drug_data)
    print(response)


def main():
    chrome = webdriver.Chrome()
    chrome.get('https://interacoesmedicamentosas.com.br/interacoes.php')

    drugList = chrome.find_element_by_id("lista")
    items = drugList.find_elements_by_tag_name("li")

    for item in items:
        drug = item.text
        postToDatabase(drug)
        print(drug)


main()
