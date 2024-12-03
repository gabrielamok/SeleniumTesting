from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Setup WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver is updated and in PATH

# Create output directory
output_dir = "amazon_results"
os.makedirs(output_dir, exist_ok=True)

try:
    # Step 1: Navigate to Amazon Brazil homepage
    driver.get("https://www.amazon.com.br/?tag=admarketbr-20&ref=pd_sl_6c82a9b71de078af1d8f2d57ef82089e683e05cacdf02edcf6029b23")
    driver.save_screenshot(os.path.join(output_dir, "homepage_debug.png"))
    print("Navigated to Amazon Brazil.")

    # Step 2: Wait for the search box
    search_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "twotabsearchtextbox"))
    )
    search_box.send_keys("laptop")
    search_box.send_keys(Keys.RETURN)
    print("Searched for 'laptop'.")
    driver.save_screenshot(os.path.join(output_dir, "after_search_debug.png"))

    # Step 3: Wait for results
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".s-main-slot"))
    )
    driver.save_screenshot(os.path.join(output_dir, "results_debug.png"))
    print("Search results loaded.")

    # Step 4: Click on the first product
    first_product = driver.find_element(By.CSS_SELECTOR, ".s-main-slot .s-result-item")
    first_product.click()
    print("Clicked on the first product.")
    driver.save_screenshot(os.path.join(output_dir, "product_page_debug.png"))

    # Step 5: Extract details
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "productTitle"))
    )
    title = driver.find_element(By.ID, "productTitle").text
    price = driver.find_element(By.CSS_SELECTOR, ".a-price .a-offscreen").text
    rating = driver.find_element(By.CSS_SELECTOR, ".a-icon-alt").get_attribute("innerHTML")

    # Save details
    details_file = os.path.join(output_dir, "product_details.txt")
    with open(details_file, "w", encoding="utf-8") as file:
        file.write(f"Product Title: {title}\n")
        file.write(f"Product Price: {price}\n")
        file.write(f"Product Rating: {rating}\n")
    print(f"Product details saved to {details_file}.")

except Exception as e:
    # Save screenshot if error occurs
    driver.save_screenshot(os.path.join(output_dir, "error_debug.png"))
    print(f"An error occurred: {e}")

finally:
    driver.quit()
