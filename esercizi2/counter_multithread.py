import threading
import time

# Funzione per contare in avanti
def count_up():
    for i in range(1, 11):
        print(f"count up: {i}")
        time.sleep(1)

# Funzione per contare all'indietro
def count_down():
    for i in range(10, 0, -1):
        print(f"count down: {i}")
        time.sleep(1)

# Creazione dei thread
thread1 = threading.Thread(target=count_up)
thread2 = threading.Thread(target=count_down)

# Avvio dei thread
thread1.start()
thread2.start()

# Sincronizzazione dei thread
thread1.join()
thread2.join()
