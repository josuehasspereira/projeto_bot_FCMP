import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Definindo as informações da placa de vídeo que queremos procurar
modelo = 'RTX 2060'
capacidade = '6GB'
preco_maximo = 1150

# Definindo a URL da página de busca do Marketplace do Facebook
url = f'https://www.facebook.com/marketplace/108420019205709/search/?query={modelo} {capacidade}'

# Configurando o driver do Chrome
chrome_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
driver_path = r'C:\Users\Josué\Documents\chromedriver2\chromedriver.exe'

driver_path = r'C:\Users\Josué\Documents\chromedriver2\chromedriver.exe'


options = webdriver.ChromeOptions()
options.binary_location = chrome_path
service = webdriver.chrome.service.Service(executable_path=driver_path)
driver = webdriver.Chrome(executable_path=driver_path, options=options)

# Navegando para a página de busca do Marketplace do Facebook
driver.get(url)

# Aguardando o carregamento completo da página
time.sleep(10)

# Obtendo todos os resultados da busca
results = driver.find_elements_by_xpath('//div[@data-testid="marketplace_feed_item"]')

# Criando uma lista para armazenar os resultados encontrados
anuncios = []

# Iterando pelos resultados e adicionando à lista os que atendem aos critérios de preço
for result in results:
    try:
        preco = float(result.find_element_by_class_name('a-price').text.replace('.', '').replace(',', '.'))
        if preco <= preco_maximo:
            anuncios.append(result.find_element_by_tag_name('a').get_attribute('href'))
        if len(anuncios) == 5:
            break
    except:
        continue

# Abrindo os anúncios no navegador Chrome
for anuncio in anuncios:
    driver.execute_script(f"window.open('{anuncio}');")

# Fechando o driver do Chrome
driver.quit()
