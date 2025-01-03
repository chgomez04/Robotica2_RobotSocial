import serial
import time
import datetime

####Para la parte del motor#####
arduino = serial.Serial("COM8",9600,timeout=1.0)
time.sleep(1)

pos_act0 = 90
pos_act1 = 45

valores = [" ", " ", " ", " "]
valores[0] = (str(pos0)) 
valores[1] = (str(pos1))
valores[2] = (str(pos2))
valores[3] = (str(emociones))
mot=valores[0]+","+valores[1]+","+valores[2]+","+valores[3]
cad="mot:"+mot
arduino.write(cad.encode('ascii'))
#print(cad)
cad =arduino.readline().decode('ascii').strip()
#print(cad)