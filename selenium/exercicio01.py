"""Exercicio para logar no email usando selenium"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("--disable-web-security")
navegador = webdriver.Chrome(options=options) #instancia um navegador

try:
    navegador.get("https://accounts.google.com/InteractiveLogin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&osid=1&passive=1209600&service=mail&ifkv=ASKXGp0PlN8JvPP5NniYljqiBl2El_XGG165RHtxyH-z4Fkegnbo3Sis0bO2QTwBOXCyw7f059FNCw&theme=glif&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    time.sleep(2)

    elemento = navegador.find_element(By.ID, "identifierId") #Encontrar elemento pelo ID
    time.sleep(2)

    elemento.send_keys("alexsandromacedo1313@gmail.com") # Digita um texto no campo selecionado
    botao_entrar = navegador.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d") # Aperta em próximo
    elemento.send_keys(Keys.RETURN)
    time.sleep(8)




finally: #Fechar navegador

    navegador.close