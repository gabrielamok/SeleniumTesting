from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuração do WebDriver
driver = webdriver.Chrome()  # Certifique-se de que o chromedriver esteja no PATH ou forneça o caminho completo.
driver.maximize_window()

try:
    # Acessando o site
    driver.get("https://the-internet.herokuapp.com")

    # Esperando até que a seção 'Broken Images' seja visível e clicando nela
    wait = WebDriverWait(driver, 10)
    broken_images_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Broken Images")))
    broken_images_link.click()

    # Aguardando o carregamento da página de "Broken Images"
    time.sleep(3)  # Melhor usar WebDriverWait para uma espera mais confiável, mas time.sleep é suficiente aqui para fins demonstrativos

    # Tirando um screenshot da página
    screenshot_path = "broken_images_screenshot.png"
    driver.save_screenshot(screenshot_path)
    print(f"Captura de tela salva em: {screenshot_path}")

finally:
    # Fechar o navegador
    driver.quit()
