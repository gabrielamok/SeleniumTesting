from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuração do WebDriver
driver = webdriver.Chrome()  # Certifique-se de que o chromedriver esteja no PATH ou forneça o caminho completo.
driver.maximize_window()

try:
    # Acessar o site principal
    driver.get("https://the-internet.herokuapp.com")

    # Esperar e clicar no link 'Dynamic Controls'
    wait = WebDriverWait(driver, 10)
    dynamic_controls_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Dynamic Controls")))
    dynamic_controls_link.click()

    # Esperar a caixa de seleção "A Checkbox" e marcar
    checkbox = wait.until(EC.presence_of_element_located((By.ID, "checkbox")))
    
    if not checkbox.is_selected():  # Verificar se a checkbox não está selecionada
        checkbox.click()  # Marcar a checkbox

    # Esperar o botão 'Enable' e clicar
    enable_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Enable']")))
    enable_button.click()

    # Esperar a mensagem "It's enabled!" aparecer na página
    result_text = wait.until(EC.presence_of_element_located((By.ID, "message")))

    # Tirar o screenshot da página
    screenshot_path = "dynamic_controls_screenshot.png"
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot salva em: {screenshot_path}")

finally:
    # Fechar o navegador
    driver.quit()
