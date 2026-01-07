import serial
import pyautogui
import time

puerto = '/dev/cu.usbmodem11101'  //Change this port to the specific one

def connect():
    while True:
        try:
            print(f"Attemping to connect to {puerto}...")
            ser = serial.Serial(puerto, 9600, timeout=0.1)
            print("¡Connected! Pedal is now working.")
            return ser
        except:
            print("Arduino not found. Re-attemping in 3 secconds...")  //adding error messages
            time.sleep(3)

arduino = connect()

while True:
    try:
        if arduino.in_waiting > 0:
            linea = arduino.readline().decode('utf-8').strip()
            if linea == "PULSADO":

              pyautogui.hotkey('') //here goes the softkey
    except:
        print("Lost connection. Reconnecting...")
        arduino = connect()
