from pyfirmata import Arduino
import time
arduino = Arduino("COM4")
repeticiones = int(input("Escoge el número de repeticiones: "))
tiempo = float(input("Escoge la velocidad de las repeticiones: "))
for temp in range(repeticiones):
    arduino.digital[9].write(1)
    time.sleep(tiempo)
    arduino.digital[9].write(0)
    time.sleep(tiempo)
