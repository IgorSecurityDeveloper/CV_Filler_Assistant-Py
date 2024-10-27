from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Função que inicia o navegador e preenche o formulário
def fill_form():
    url = url_entry.get()  # Obtém a URL digitada
    name = name_entry.get()  # Obtém o nome digitado
    email = email_entry.get()  # Obtém o email digitado

    if url and name and email:
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Executa em modo headless (sem abrir o navegador visível)
        service = Service('chromedriver')  # Substitua pelo caminho correto do driver
        driver = webdriver.Chrome(service=service, options=chrome_options)
        
        driver.get(url)
        
        try:
            # Varredura e preenchimento dos campos (os seletores devem ser ajustados para o site específico)
            name_field = driver.find_element(By.NAME, 'name')  # Substitua pelo seletor correto do campo de nome
            name_field.send_keys(name)
            
            email_field = driver.find_element(By.NAME, 'email')  # Substitua pelo seletor correto do campo de email
            email_field.send_keys(email)

            # Adicionar mais campos conforme necessário
            driver.find_element(By.XPATH, '//input[@type="submit"]').click()  # Exemplo para clicar no botão submit
        except Exception as e:
            print(f"Erro ao preencher o formulário: {e}")
        finally:
            driver.quit()
    else:
        print("Preencha todos os campos e a URL antes de iniciar.")