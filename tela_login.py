from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

Service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service = Service)

url_tela = 'https://lucifranco10.github.io/login.github.io/'
driver.get(url_tela)
sleep(2)

driver.maximize_window()
sleep(2)


usuário = driver.find_element(By.NAME,'username')
usuário.send_keys('luciane.franco')
sleep(2)


senha= driver.find_element(By.XPATH,'//*[@id="password"]')
senha.send_keys('1234')
sleep(2)



Button_login = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginForm > button"))
)
Button_login.click()
sleep(5)




try:
    alert = WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert_text = alert.text
    print(f"Alerta presente com o texto: {alert_text}")
    


    alert.accept()
    print("Alerta fechado com sucesso.")
except NoAlertPresentException:
    print("Nenhum alerta estava presente.")
except UnexpectedAlertPresentException as e:
    print(f"Erro inesperado: {e}")


sleep(5)

if driver.find_element(By.XPATH,'/html/body/h1/strong').is_displayed:
    print ('ESSA E A SEGUNDA TELA')

else:
    print('Não apareceu esta mensagem')


