import time
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By

driver = Firefox()
driver.get('https://richup.io/')
driver.maximize_window()
time.sleep(10)

try:
    driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[2]/div/button[2]').click()
except Exception:
    driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/span[1]/a').click()

time.sleep(5)
driver.find_element(By.XPATH,'/html/body/div[2]/div[4]/div[1]/div[1]/div[2]/div[1]/div/div[2]/div[1]/button[2]').click()
time.sleep(3)
try:
    driver.find_element(By.XPATH,'/html/body/div[2]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[2]/button').click()
except Exception:
    driver.find_element(By.XPATH,'/html/body/div[3]/div[4]/div/div[2]/div/div[1]/div[3]/div[1]/div[2]/button').click()
    
time.sleep(3)

# continuar test de colocar a caixiha vermelha 

# Encontrar o elemento div pelo seu seletor (substitua pelo seletor correto)
div_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div[2]/div/div/div[3]/div[1]/div[3]/div[1]")

# Adicionar uma borda vermelha usando JavaScript
driver.execute_script("arguments[0].style.border='4px solid red'", div_element)

# Aguarde um momento para visualizar o efeito (opcional)
driver.implicitly_wait(10)

time.sleep(20)

# remover a caixinha vermelha
driver.execute_script("arguments[0].style.border='0px solid red'", div_element)

# Encontrar o elemento div pelo seu seletor (substitua pelo seletor correto)
div_element = driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/div/div[2]/div/div/div[3]/div[3]/div[3]/div[1]")

# Adicionar uma borda vermelha usando JavaScript
driver.execute_script("arguments[0].style.border='4px solid red'", div_element)

# Aguarde um momento para visualizar o efeito (opcional)
driver.implicitly_wait(10)

time.sleep(20)

driver.close()
