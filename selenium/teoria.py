#importar biblioteca selenium

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Instanciar um navegador ( Chrome, neste exemplo)

navegador = webdriver.Chrome()

#Navegadar para uma URL


try: #Encapsula um codigo que pode dar erro
    navegador.get("https://www.google.com.br/")

    elemento = navegador.find_element(By.ID, "APjFqb") #Encontrar elemento pelo ID
    time.sleep(2)

    #elemento.click()

    elemento.send_keys("Greve de Metro em São Paulo") #Digita um texto no campo selecionado
    elemento.send_keys(Keys.RETURN)
    time.sleep(2)

except:
    print("Erro")

finally: #Fechar navegador

    navegador.close

