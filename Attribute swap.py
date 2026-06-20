import time
import threading
import keyboard
import pydirectinput

# Configurações
pydirectinput.FAILSAFE = False
pydirectinput.PAUSE = 0

swap_lock = threading.Lock()

def swap():
    if not swap_lock.acquire(blocking=False):
        return

    try:
        pydirectinput.click()
        pydirectinput.press('3')

        time.sleep(0.008)

        pydirectinput.press('1')
        pydirectinput.press('1')

    finally:
        swap_lock.release()

print("Macro ativo | ESC para sair")

while True:
    # funciona mesmo segurando outras teclas
    if keyboard.is_pressed('x'):
        swap()

        # evita repetir infinitamente enquanto segura
        while keyboard.is_pressed('x'):
            time.sleep(0.01)

    if keyboard.is_pressed('esc'):
        break

    time.sleep(0.001)