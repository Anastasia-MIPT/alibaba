import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
DAC = [10, 9, 11, 5, 6, 13, 19, 26]
GPIO.setup (DAC, GPIO.OUT)

def dBTL(dN):
    bdN = bin(dN)
    dddN = bdN[2:15:1]
    N = dddN.zfill(8)
    a = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(8):
        a[i] = int(N[i])
    return a

def lightNumber(number):
    b = dBTL(number)
    for i in range(8):
        GPIO.output(DAC[7-i], b[i])

def repititionsNumber(amount):
    for i in range(amount):
        for k in range (0, 255):
            lightNumber(k)
            time.sleep (0.01)
        for k in range (255, 0, -1):
            lightNumber(k)
            time.sleep (0.01)

print ("Введите число повторений")
amount = int(input())
repititionsNumber(amount)