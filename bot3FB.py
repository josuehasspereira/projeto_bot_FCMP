from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service

# Caminho do ChromeDriver
caminho_chromedriver = r"C:\Users\Josué\Documents\chromedriver2\chromedriver.exe"

url = f'https://www.facebook.com'
urlMarket = f'https://www.facebook.com/marketplace/joinville/search?minPrice=900&maxPrice=1200&query=RTX%202060&exact=false'

# Configurar as opções do ChromeDriver
opcoes = webdriver.ChromeOptions()
# Comente a próxima linha se quiser que o Chrome seja aberto em modo headless
opcoes.headless = False

# Criar uma instância do ChromeDriver
driver = webdriver.Chrome(executable_path=caminho_chromedriver, options=opcoes)

# Acessar a página do Mercado Livre
driver.get(url)

# Esperar a página carregar
driver.implicitly_wait(10)

# Navega até a página de login do Facebook
driver.get("https://www.facebook.com/login")

# Insere as informações de usuário e senha
username_field = driver.find_element(By.CSS_SELECTOR, 'input#email')
username_field.send_keys("josue.hass@hotmail.com")

password_field = driver.find_element(By.CSS_SELECTOR, 'input#pass')
password_field.send_keys("cleopatrap4$Sw0rD()")

# Clica no botão de login
login_button = driver.find_element(By.XPATH, "//button[contains(., 'Entrar') or contains(., 'Log In') or contains(., 'Log in') or contains(., 'Entrar com e-mail')] | //input[@type='submit']")
login_button.click()

driver.implicitly_wait(10)

driver.execute_script(f"window.open('{urlMarket}', '_blank');")

# Alternar para a nova guia
driver.switch_to.window(driver.window_handles[1])

# Obter a URL do resultado
url_resultado = driver.current_url

# Realizar alguma operação com cada resultado, por exemplo, imprimir a URL
print('URL do resultado:', url_resultado)

# Alternar de volta para a guia anterior
driver.switch_to.window(driver.window_handles[1])

text = "/marketplace/item/"

elementsLinks = driver.find_elements(By.XPATH,'//a[contains(@href, "%s")]' % text)
print("//-----------------------------//")
i = 5
#for i in range(10):
#    driver.execute_script(f"window.open('{elementsLinks[i].get_attribute('href')}', '_blank');")
driver.execute_script(f"window.open('{elementsLinks[i].get_attribute('href')}', '_blank');")

driver.implicitly_wait(20)

text = "Enviar"
#div[aria-label='Enviar']
#id="facebook"
enviar_mensagem = driver.find_elements(By.XPATH, '//div[contains(@aria-label, "%s")]' % text)
print("*******")
print(enviar_mensagem[0])

input("Pressione enter")
driver.quit()
quit()
