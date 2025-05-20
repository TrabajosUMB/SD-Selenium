from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Inicializar navegador (Chrome en este ejemplo)
driver = webdriver.Chrome()

# Ir a la página con el formulario
driver.get("https://itech.com.co/contactanos/")  #Reemplaza con la URL real

# Esperar a que se cargue el formulario
try:
    # Aquí va tu código RPA
    #pass  # Reemplaza este pass con tu código
    # Esperar a que se cargue el formulario
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "wpcf7-form"))
    )
    # Nombre
    campo_nombre = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "your-name"))
    )
    campo_nombre.send_keys("John")
    
    # Apellido
    campo_apellido = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "your-surname"))
    )
    campo_apellido.send_keys("Doe")
    
    # Email
    campo_email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "your-email"))
    )
    campo_email.send_keys("john.doe@example.com")
    
    # Teléfono
    campo_telefono = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "your-phone"))
    )
    campo_telefono.send_keys("123456789")
    # Ciudad
    campo_ciudad = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "your-city"))
    )
    campo_ciudad.send_keys("Bogota")
    # Mensaje
    campo_mensaje = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "your-message"))
    )
    campo_mensaje.send_keys("Hola, me gustaria contactarte")
    # Verificación del quiz matemático
    campo_verificacion = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "math-quiz"))
    )
    campo_verificacion.send_keys("35")  # Resultado de 14+21
    
    # Checkbox de aceptación
    checkbox = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "your-acceptance"))
    )
    checkbox.click()
    
    # Botón enviar
    boton_enviar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input[type='submit'"))
    )
    boton_enviar.click()
    
    

except Exception as e:
    checkbox = driver.find_element(By.NAME, "your-acceptance")
    driver.execute_script("arguments[0].click();", checkbox)
    print(f"Se produjo un error: {e}")
finally:
    # Cerrar el navegador al finalizar
    print("Navegador cerrado")




# Esperar para visualizar resultado
time.sleep(20)

# driver.quit()
