from random import randint
import selenium
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

palpites = int(input('QUANTOS PALPITES ?: '))
driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://www.loteriasonline.caixa.gov.br/silce-web/?utm_source=site_loterias&utm_medium=cross&utm_campaign=loteriasonline&utm_term=lotomania#/lotomania")
sim = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'botaosim')))
sim.click()
WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.gepup-loterias-link.data-jogo-lotomania')))[0].click()
for palpitar in range(0, palpites):
    lista = []
    for c in range(1, 51):
        while True:
            numero = randint(0, 99)
            if not numero in lista:
                lista.append(numero)
                break
    #print('||| LOTO MANIA DA PREGUIÇA |||')
    #print(len(lista), 'Numeros')
    sozinhos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = 0
    lista2 = []
    for c in lista:
        x+=1
        if x == 10:
            x = 0
            str(c)
            if c in sozinhos:
                lista2.append('0'+ str(c))
            else:
                lista2.append(str(c))
        else:
            str(c)
            if c in sozinhos:
                lista2.append('0'+ str(c))
            else:
                lista2.append(str(c))
    print(lista2)
    numeros = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.data-selecionar-numero-lotomania.ng-binding')))
    numeros2 = []
    for c in numeros:
        #print(c.get_attribute('innerHTML'))
        if c.get_attribute('innerHTML') in lista2:
            numeros2.append(c)

    print('Numeros2: ', len(numeros2))
    for c in numeros2:
        actions = ActionChains(driver)
        actions.move_to_element(c)
        actions.click(c)
        actions.perform()
    driver.find_element_by_id('colocarnocarrinho').click()
