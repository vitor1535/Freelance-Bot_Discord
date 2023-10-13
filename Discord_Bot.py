import pyautogui
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# Definir variaveis
delayAmizade = 5
delayScroll = 10
nicksAdicionados = []


# Criar o navegador
opt = Options()
opt.add_experimental_option("debuggerAddress","localhost:8989")
driver = webdriver.Chrome(options = opt)

# Acessar o site
driver.get("https://discord.com/channels/@me")

# Acessa os membros do discord, envia pedido de amizade e insere em uma lista aqueles que foram selecionados
while(True):

    lista = driver.find_elements("xpath", "//span[@class='username-3_PJ5r desaturateUserColors-1O-G89']")

    try:
        for item in lista:
            if (item.text not in nicksAdicionados):
                nicksAdicionados.append(item.text)
                abrirCaixa = item
                actions = ActionChains(driver)
                actions.context_click(abrirCaixa).perform()
                time.sleep(2)
                driver.find_element("xpath", '//*[@id="user-context-add-friend"]').click()
                time.sleep(delayAmizade)
                driver.find_element("xpath", '//*[@id="checkbox"]')
                time.sleep(2)

    except:
        print("Erro!")

    pyautogui.click(1914,1031)
    time.sleep(delayScroll)

    if (nicksAdicionados[len(nicksAdicionados) - 1][0] == 'z' or  nicksAdicionados[len(nicksAdicionados) - 1][0] == 'Z' or nicksAdicionados[len(nicksAdicionados) - 1][0] > 'z'):
        break

