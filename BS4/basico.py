#importar a biblioteca BS4

from bs4 import BeautifulSoup
import requests

#URL da pagina web a ser raspada

url = 'https://produto.mercadolivre.com.br/MLB-3493531499-notebook-acer-a515-57-52a5-ci5-8gb-512gb-ssd-linux-156-fhd-_JM#polycard_client=homes-korribanSearchPromotions&position=48&search_layout=grid&type=item&tracking_id=e3949ce2-4cfb-43b9-b989-d3969f3709d7'

#Enviar uma solicitação GET para nossa página

response = requests.get(url)

#Verificar se solicitação foi bem sucedida

if response.status_code == 200:
    #Criar um objeto BeautifulSoup para analisar o nosso conteúdo html da página

    soup = BeautifulSoup(response.text, 'html.parser')

#Procurar o primeiro elemento h1
h1 = soup.find('h1')
#Exibir o texto dentro da tag h1

print(f'Titulo da página: {h1.text}')

#Exibir todos os elementos HTML correspondentes a uma tag específica

#Procura por todos os links na página
todos_links = soup.find_all('a')

#Exibir os URLS de todos os links na página
for link in todos_links:
    print(link.get('href'))

#Acessar atributos de um elemento HTML
img_src = soup.find('img')['src']

#Navegar pela arvore DOM, nagar pelo HTML para encontrar elementos alinhados.

conteudo_div = soup.find('div', class_='ui-pdp-header__title-container')
conteudo_spam = soup.find('div', class_='andes-money-amount__fraction')


#Exibir o texto dentro da tag < div class='conteudo'>

print('Conteudo da Div: ')
print(conteudo_div.text.strip())
print('Preço do Produto: ')
print(conteudo_spam.isnumeric.strip())

#Encontrar todos os elementos de uma classe específica

"""todos_elementos_classe_x = soup.find_all(class_='')

print(todos_elementos_classe_x.text.strip())

#Encontrar"""
