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

url_hotmart = 'https://lucifranco10.github.io/login.github.io/'
driver.get(url_hotmart)
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
sleep(2)




