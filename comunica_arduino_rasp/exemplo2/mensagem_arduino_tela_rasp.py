import serial

'''
printa no terminal do rasp a mensagem enviada pelo arduíno
'''

ser = serial.Serial("/dev/ttyACM0", 9600)
ser.flush()

while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        print(line)