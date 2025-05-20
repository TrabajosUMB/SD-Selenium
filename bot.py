import pyautogui
import time
import subprocess

def rpa_abrir_word():
    # Abrir Word en Windows
    subprocess.Popen(['start', 'winword'], shell=True)
    time.sleep(5)  # Esperar a que Word se abra

    # Maximizar ventana (Alt + Space, X)
    pyautogui.hotkey('alt', 'space')
    time.sleep(0.5)
    pyautogui.press('x')
    time.sleep(1)

    # Crear nuevo documento (Ctrl + N)
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(2)
    
def rpa_escribir_en_word(frase):
    rpa_abrir_word()
    pyautogui.write(frase, interval=0.05)
    
def rpa_guardar_archivo():
    # Presionar Enter para guardar con el nombre por defecto
    pyautogui.press('enter')
    time.sleep(10)

def rpa_cerrar_y_guardar_word():
    
    
    # Cerrar y guardarWord (Alt + F4)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)
    
    # Confirmar cierre si hay diálogo
    pyautogui.press('enter')
    time.sleep(1)
    
    # Guardar en el explorador de archivos
    rpa_guardar_archivo()



if __name__ == "__main__":
    rpa_escribir_en_word("Hola chicos de Distribuidos, este es un ejemplo automatizado con PyAutoGUI en Windows. Que mas profe se logro")
    rpa_cerrar_y_guardar_word()
