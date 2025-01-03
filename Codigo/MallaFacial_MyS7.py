#Libreria openCv
import cv2 
import mediapipe as mp
import math

#Libreria Arduino
from ctypes import c_int16
import serial
import time
import threading
import datetime

##libreria para sonido
from playsound import playsound
import pygame 

pygame.init()
pygame.mixer.init()

###Para las emociones
emociones = 1
####### para el sonido#####
def sonido1():
    global emociones 
    print(emociones)
    if emociones == 1: ##Normal
        playsound("E:/fiuna2_2021/R2/proyectoR2/codigo/risas.mp3")
        time.sleep(2)
    if emociones == 2: ##Feliz
        playsound("E:/fiuna2_2021/R2/proyectoR2/codigo/risas.mp3")
        time.sleep(2)
    if emociones == 1: ##Normal
        playsound("E:/fiuna2_2021/R2/proyectoR2/codigo/risas.mp3")
        time.sleep(2)

def sonido(emocion):
    '''
    sonido_fondo = pygame.mixer.Sound("risas.mp3")
    pygame.mixer.Sound.play(sonido_fondo)
    time.sleep(1)
    pygame.mixer.Sound.stop(sonido_fondo)
    '''
    
    
    print(emocion)
    
    if emocion == 2: ##Feliz

        sonido_fondo = pygame.mixer.Sound("risas.mp3")
        pygame.mixer.Sound.stop(sonido_fondo)
        time.sleep(2)
        pygame.mixer.Sound.play(sonido_fondo)

        
        
    '''
    if emocion == 3: ##asombro
        sonido_fondo1 = pygame.mixer.Sound("sorpresa.wav")
        pygame.mixer.Sound.play(sonido_fondo1)
        time.sleep(1)
        pygame.mixer.Sound.stop(sonido_fondo1)
    '''




####Para la parte del motor#####
arduino = serial.Serial("COM8",9600,timeout=1.0)
time.sleep(1)

pos_act0 = 90
pos_act1 = 45
pos_act2 = round( ((pos_act1-30)/(55 - 30))* (125 - 150) + 150 )

posAct0 = 90
posAct1 = 45
posAct2 = round( ((pos_act1-30)/(55 - 30))* (125 - 150) + 150 )
######para mirar cada rostro
def mirar_rostros(xc, yc):
    global pos_act0
    global pos_act1
    global pos_act2
    global emociones

    if xc < 640:
        angx = int(((xc - 0)/(639 - 0))*( 0 - 20) + 20)
        pos = pos_act0 - angx
        print("pos=",pos)
        if pos > 0:
            pos0 = pos
        else: 
            pos0 = 0
    if xc >= 640:
        angx = int(((xc - 640)/(1280 - 640))*( 20 - 0) + 0)
        pos = pos_act0 + angx
        print("pos",pos)
        if pos < 180:
            pos0 = pos
        else: 
            pos0 = 180
    if yc < 260:
        angy = int(((yc - 0)/(359 -0))*(0 - 13) + 13)
        angy = pos_act1 + angy
        if angy < 55:
            pos1 = angy
            anguloZ = round( ((pos_act1-30)/(55 - 30))* (125 - 150) + 150 )
            pos2 = anguloZ
        else:
            pos1 = 55
            anguloZ = round( ((pos_act1-30)/(55 - 30))* (125 - 150) + 150 )
            pos2 = anguloZ
    if yc >= 260:
        angy = int(((yc - 360)/(720 - 360))*(12 - 0) + 0)
        angy = pos_act1 - angy
        if angy > 30:
            pos1 = angy
            anguloZ = round( ((pos_act1-30)/(55 - 30))* (125 - 150) + 150 )
            pos2 = anguloZ
        else:
            pos1 = 30
            anguloZ = round( ((pos_act1-30)/(55 - 30))* (125 - 150) + 150 )
            pos2 = anguloZ
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


####para centrar la cara en el centro###
def motor_centro(x, y):
    global pos_act0
    global pos_act1
    global pos_act2
    global emociones
    #print(x ," , ", y)
    ####para el eje x
    #Ax = int(((x - 0)/(1280 - 0))*(180 - 0) + 0)
    if x < 530 or x > 740 or y < 260 or y > 460:
        if x <530:
            
            if pos_act0 >= 2:
                pos_act0 = pos_act0 - 2
            else:
                pos_act0 = 0
        if x > 740:
            if (pos_act0 <= 178):
                pos_act0 = pos_act0 + 2
            else:
                pos_act0 = 180
        #para el eje y 
        #Ay = int(((y - 0)/(720 - 0))*(45 - 35) + 0)
        
        if y < 260:
            if pos_act1 < 55:
                pos_act1 = pos_act1 +1
                anguloZ = round( ((pos_act1-30)/(55 - 30))* (125 - 150) + 150 )
                pos_act2 = anguloZ
            else:
                pos_act1 = 55
                anguloZ = round( ((pos_act1-30)/(55 - 30))* (125 - 150) + 150 )
                pos_act2 = anguloZ

        if y > 460:
            if (pos_act1 > 30):
                pos_act1 = pos_act1 - 1
                anguloZ = round( ((pos_act1-30)/(55 - 30))* (125 - 150) + 150 )
                pos_act2 = anguloZ
            else:
                pos_act1 = 30
                anguloZ = round( ((pos_act1-30)/(55 - 30))* (125 - 150) + 150 )
                pos_act2 = anguloZ

        valores = [" ", " ", " ", " "]
        valores[0] = (str(pos_act0)) 
        valores[1] = (str(pos_act1))
        valores[2] = (str(pos_act2))
        valores[3] = (str(emociones))
        mot=valores[0]+","+valores[1]+","+valores[2]+","+valores[3]
        cad="mot:"+mot
        arduino.write(cad.encode('ascii'))
        #print(cad)
        cad =arduino.readline().decode('ascii').strip()
        #print(cad)


###imita movimiento "No"####
def imitaMovimiento(xc, yc, xf, yf, angulo):
    global pos_act0
    global pos_act1
    global pos_act2
    global emociones
    angulo1 = int(((angulo - 0)/(30-0))*(20-0))
    
    if xc> 530 and xc < 740 and yc > 260 and yc < 460 :
        if xf < xc:
            pos1 = pos_act1 - angulo1
            pos2 = pos_act2 - angulo1
            valores = [" ", " ", " ", " "]
            valores[0] = (str(pos_act0)) 
            valores[1] = (str(pos1))
            valores[2] = (str(pos2))
            valores[3] = (str(emociones))
            mot=valores[0]+","+valores[1]+","+valores[2]+","+valores[3]
            cad="mot:"+mot
            arduino.write(cad.encode('ascii'))
            #print(cad)
            cad =arduino.readline().decode('ascii').strip()
            #print(cad)
        if xf > xc: 
            pos1 = pos_act1 + angulo1
            pos2 = pos_act2 + angulo1

            valores = [" ", " ", " ", " "]
            valores[0] = (str(pos_act0)) 
            valores[1] = (str(pos1))
            valores[2] = (str(pos2))
            valores[3] = (str(emociones))
            mot=valores[0]+","+valores[1]+","+valores[2]+","+valores[3]
            cad="mot:"+mot
            arduino.write(cad.encode('ascii'))
            #print(cad)
            cad =arduino.readline().decode('ascii').strip()
            #print(cad)

#####Imita movimiento "Si"
def imitaMovimiento_Si(xc, yc, z_151, z_199, angulo):
    global pos_act0
    global pos_act1
    global pos_act2
    global emociones
    angulo1 = int(((angulo - 0)/(30-0))*(20-0))
    
    if xc> 530 and xc < 740 and yc > 260 and yc < 460 :
        if angulo < 10:
            if z_151 >  0 and z_151 < 13:
                angulo1 = int (((z_151 - 0 )/(15 - 0))*(0 - 10) + 10)
                pos1 = pos_act1 + angulo1
                anguloZ = round( ((pos1-30)/(55 - 30))* (125 - 150) + 150 )
                pos2 = anguloZ
                valores = [" ", " ", " ", " "]
                valores[0] = (str(pos_act0)) 
                valores[1] = (str(pos1))
                valores[2] = (str(pos2))
                valores[3] = (str(emociones))
                mot=valores[0]+","+valores[1]+","+valores[2]+","+valores[3]
                cad="mot:"+mot
                arduino.write(cad.encode('ascii'))
                #print(cad)
                cad =arduino.readline().decode('ascii').strip()
                #print(cad)
            if z_199 > 0 and z_199 < 20:
                angulo1 = int (((z_199 - 0 )/(20 - 0))*(10 - 0) + 0)
                pos1 = pos_act1 - angulo1
                anguloZ = round( ((pos1-30)/(55 - 30))* (125 - 150) + 150 )
                pos2 = anguloZ
                valores = [" ", " ", " ", " "]
                valores[0] = (str(pos_act0)) 
                valores[1] = (str(pos1))
                valores[2] = (str(pos2))
                valores[3] = (str(emociones))
                mot=valores[0]+","+valores[1]+","+valores[2]+","+valores[3]
                cad="mot:"+mot
                arduino.write(cad.encode('ascii'))
                #print(cad)
                cad =arduino.readline().decode('ascii').strip()
                #print(cad)
            
            



##Para inicializar los motores #######
valores = [" ", " ", " ", " "]
valores[0] = (str(pos_act0)) 
valores[1] = (str(pos_act1))
valores[2] = (str(pos_act2))
valores[3] = (str(emociones))
mot=valores[0]+","+valores[1]+","+valores[2]+","+valores[3]
cad="mot:"+mot
arduino.write(cad.encode('ascii'))
#print(cad)
cad =arduino.readline().decode('ascii').strip()
#print(cad)
########Realizamos la video captura############### 
cap = cv2.VideoCapture(0)
cap.set(3,1280) #Definimos el ancho de la ventana
cap.set(4,720) # definimos el alto de la ventana 

## Creamos nuestra funcion de dibujo
mpDibujo = mp.solutions.drawing_utils
ConfDibu = mpDibujo.DrawingSpec(thickness= 1, circle_radius = 1) #Ajustamos la configuracion de dibujo

## Creamos un objeto donde almacenamos la malla facial
mpMallaFacial = mp.solutions.face_mesh # Primero llamamos la funcion
MallaFacial = mpMallaFacial.FaceMesh(max_num_faces = 3) #Creamos el objeto(ctrl + click)


##Creamos el while principal
cantidad_rostro = 0
while True:

    ret, frame =cap.read()
    if ret == False:
            break
    frame = cv2.flip(frame,1)

    ## Correccion de color
    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    #Observamos los resultados
    resultados = MallaFacial.process(frameRGB)

    #creamos unas listas donde almacenamos los resultados 
    px = []
    py = []
    lista = []
    rostro_identificador = []
    punto_8 = []
    punto_151 = []
    punto_199 = []
    distancia_centro = []
    r = 5
    t = 3

    if resultados.multi_face_landmarks: #si detectamos algun rostro
        #primero elegimos un rostro
        for rostros in resultados.multi_face_landmarks: #Mostramos el rostro detectado
            mpDibujo.draw_landmarks(frame, rostros, mpMallaFacial.FACEMESH_CONTOURS, ConfDibu, ConfDibu)
            
            rostro_identificador.append(rostros.landmark[4])
            punto_8.append(rostros.landmark[8])
            punto_151.append(rostros.landmark[151])
            punto_199.append(rostros.landmark[199])
        
        ###para cuando hay nuevo rostros 

            
        
        #print(len(rostro_identificador))
        if len(rostro_identificador) > 1:
            for id, puntos in enumerate(rostro_identificador):
                al, an, c = frame.shape
                xc, yc = int(an/2), int(al/2)
                x, y = int(puntos.x*an), int(puntos.y*al)
                distancia = math.hypot(x- xc, y - yc)
                distancia_centro.append(distancia)
                cv2.line(frame, (x, y), (xc, yc), (0, 0, 0), t)

                if cantidad_rostro != len(rostro_identificador):
                    cv2.circle(frame, (x, y), r, (0, 0, 0), cv2.FILLED)
                    mirar_rostros(x, y)
            
            cantidad_rostro = len(rostro_identificador)
            
            menor_distancia =  min(distancia_centro)
            pos_menor_distancia = distancia_centro.index(menor_distancia)
            al, an, c = frame.shape
            xc, yc = int(rostro_identificador[pos_menor_distancia].x*an), int(rostro_identificador[pos_menor_distancia].y*al)
            xf, yf = int(punto_8[pos_menor_distancia].x*an), int(punto_8[pos_menor_distancia].y*al)
            cv2.line(frame, (xf, yf), (xc, yc), (0, 0, 0), t)
            cv2.line(frame, (xc, yf), (xc, yc), (0, 0, 0), t)
            cv2.circle(frame, (xc, yc), r, (0, 0, 0), cv2.FILLED)
            
            dx1 = xf - xc
            dy1 = yf - yc
            dx2 = xc - xc
            dy2 = yf - yc
            angle1 = math.atan2(dy1, dx1)
            angle1 = int(angle1 * 180 / math.pi)
            # print(angle1)
            angle2 = math.atan2(dy2, dx2)
            angle2 = int(angle2 * 180 / math.pi)
            # print(angle2)
            if angle1 * angle2 >= 0:
                insideAngle = abs(angle1 - angle2)
            else:
                insideAngle = abs(angle1) + abs(angle2)
                if insideAngle > 180:
                    insideAngle = 360 - insideAngle
            insideAngle = insideAngle % 180
            #enviar coordenadas de la posicion del centro al motor
            motor_centro(xc, yc)
            
            imitaMovimiento(xc, yc, xf, yf, insideAngle)
            z_151 = int (punto_151[pos_menor_distancia].z*1000)
            z_199 = int(punto_199[pos_menor_distancia].z*1000)
            print(z_151, z_199)
            print(insideAngle)

            
            
            
            
        else: 
            cantidad_rostro = len(rostro_identificador)
            al, an, c = frame.shape
            #print(rostro_identificador[0].x ," , ", rostro_identificador[0].y)
            xc, yc = int(rostro_identificador[0].x*an), int(rostro_identificador[0].y*al)
            #print(xc, " ,", yc)
            xf, yf = int(punto_8[0].x*an), int(punto_8[0].y*al)
            cv2.line(frame, (xf, yf), (xc, yc), (0, 0, 0), t)
            cv2.line(frame, (xc, yf), (xc, yc), (0, 0, 0), t)
            cv2.circle(frame, (xc, yc), r, (0, 0, 0), cv2.FILLED)
            cv2.rectangle(frame,(530,260), (740, 460), (0,255,0),1)
            cv2.circle(frame, (640, 360), r, (0, 0, 0), cv2.FILLED)

            dx1 = xf - xc
            dy1 = yf - yc
            dx2 = xc - xc
            dy2 = yf - yc
            angle1 = math.atan2(dy1, dx1)
            angle1 = int(angle1 * 180 / math.pi)
            # print(angle1)
            angle2 = math.atan2(dy2, dx2)
            angle2 = int(angle2 * 180 / math.pi)
            # print(angle2)
            if angle1 * angle2 >= 0:
                insideAngle = abs(angle1 - angle2)
            else:
                insideAngle = abs(angle1) + abs(angle2)
                if insideAngle > 180:
                    insideAngle = 360 - insideAngle
            insideAngle = insideAngle % 180
            #enviar coordenadas de la posicion del centro al motor
            motor_centro(xc, yc)
            
            imitaMovimiento(xc, yc, xf, yf, insideAngle)
            z_151 = int (punto_151[0].z*1000)
            z_199 = int(punto_199[0].z*1000)
            print(z_151, z_199)
            print(insideAngle)

            #imitaMovimiento_Si(xc, yc, z_151, z_199, insideAngle)

        ####Para identificar las emociones del rostro elegido##########

        for rostros in resultados.multi_face_landmarks: #Mostramos el rostro detectado
            mpDibujo.draw_landmarks(frame, rostros, mpMallaFacial.FACEMESH_CONTOURS, ConfDibu, ConfDibu)

            #aAhora vamos a extraer los puntos del rostro detectado 
            for id, puntos in enumerate(rostros.landmark):
                #print(puntos) ## Nos entrega una proporcion 
                al, an, c = frame.shape
                x, y = int(puntos.x*an), int(puntos.y*al)
                
                px.append(x)
                py.append(y)
                lista.append([id,x,y])
                if len(lista) == 468:
                    #ceja Derecha
                    x1, y1 = lista[65][1:]
                    x2, y2 = lista[158][1:]
                    cx, cy = (x1 + x2) // 2, (y1 + y2) // 2
                    longitud1 = math.hypot(x2 - x1, y2 - y1)
                    '''cv2.line(frame, (x1, y1), (x2, y2), (0, 0, 0), t)
                    cv2.circle(frame, (x1, y1), r, (0, 0, 0), cv2.FILLED)
                    cv2.circle(frame, (x2, y2), r, (0, 0, 0), cv2.FILLED)
                    cv2.circle(frame, (cx, cy), r, (0, 0, 0), cv2.FILLED)
                    
                    print("\nceja Derecha=",longitud1)'''

                    #Ceja Izquierda
                    x3, y3 = lista[295][1:]
                    x4, y4 = lista[385][1:]
                    cx2, cy2 = (x3 + x4) // 2, (y3 + y4) // 2 
                    longitud2 = math.hypot(x4 - x3, y4 - y3)
                    #print(longitud2)
                    '''cv2.line(frame, (x3, y3), (x4, y4), (0, 0, 0), t)
                    cv2.circle(frame, (x3, y3), r, (0, 0, 0), cv2.FILLED)
                    cv2.circle(frame, (x4, y4), r, (0, 0, 0), cv2.FILLED)
                    cv2.circle(frame, (cx2, cy2), r, (0, 0, 0), cv2.FILLED)
                    longitud1 = math.hypot(x4 - x3, y4 - y3)
                    print("\nCeja Izquierda=",longitud2)'''

                    #Boca Extremos
                    x5, y5 = lista[78][1:]
                    x6, y6 = lista[308][1:]
                    cx3, cy3 = (x5 + x6) // 2, (y5 + y6) // 2 
                    longitud3 = math.hypot(x6 - x5, y6 - y5)
                    #print(longitud3)
                    #cv2.line(frame, (x5, y5), (x6, y6), (0, 0, 0), t)
                    #cv2.circle(frame, (x5, y5), r, (0, 0, 0), cv2.FILLED)
                    #cv2.circle(frame, (x6, y6), r, (0, 0, 0), cv2.FILLED)
                    #cv2.circle(frame, (cx3, cy3), r, (0, 0, 0), cv2.FILLED)
                   #print("\nBoca Extremos=",longitud3)

                    #Boca Apertura
                    x7, y7 = lista[13][1:]
                    x8, y8 = lista[14][1:]
                    cx4, cy4 = (x7 + x8) // 2, (y7 + y8) // 2 
                    longitud4 = math.hypot(x8 - x7, y8 - y7)
                    #print(longitud4)
                    #cv2.line(frame, (x7, y7), (x8, y8), (0, 0, 0), t)
                    #cv2.circle(frame, (x7, y7), r, (0, 0, 0), cv2.FILLED)
                    #cv2.circle(frame, (x8, y8), r, (0, 0, 0), cv2.FILLED)
                    #cv2.circle(frame, (cx4, cy4), r, (0, 0, 0), cv2.FILLED)
                    #print("\nBoca Apertura=",longitud4)
                    #Clasificacion 
                    lm7=math.hypot(x7-x7, cy4 - y7)
                    lmc3=math.hypot(cx4-cx4, cy4 - cy3)
                    #print("\nApertura/2=",lm7)
                    xl, yl = lista[69][1:]
                    #feliz
                    if lmc3 > lm7*0.6 and lmc3> 6.3:
                        cv2.putText(frame, 'Feliz', (xl, yl), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        emociones = 2
                        hilo1 = threading.Thread(target=sonido, args=(emociones,))
                        hilo1.start()
                    else :
                        #Asombrado
                        if lmc3 < lm7*0.5 and lm7 > 10:
                            cv2.putText(frame, 'Asombrado', (xl, yl), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                            emociones = 3
                            hilo1 = threading.Thread(target=sonido, args=(emociones,))
                            hilo1.start()
                        else:
                            emociones = 1

                    '''
                    #Enojado
                    if longitud1 < 19 and longitud2 < 19 and longitud3 > 80 and longitud3 < 95 and longitud4 < 5:
                        cv2.putText(frame, 'persona Enojada', (480, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    #Feliz
                    elif longitud1 > 20 and longitud1 < 33 and longitud2 > 20 and longitud2 < 33 and longitud3 > 109 and longitud4 > 10 and longitud4 < 20:
                        cv2.putText(frame, 'persona Feliz', (480, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    #Asombrada
                    elif longitud1 > 35 and longitud2 > 35 and longitud3 > 80 and longitud3 < 90 and longitud4 > 20:
                        cv2.putText(frame, 'persona Asombrado', (480, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    #Triste
                    elif longitud1 > 25 and longitud1 < 35 and longitud2 > 25 and longitud2 <35 and longitud3 > 90 and longitud3 < 95 and longitud4 < 5:
                       cv2.putText(frame, 'persona Triste', (480, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                    '''
               
    cv2.imshow("Reconocimineto de emociones", frame) 
    if cv2.waitKey(1)== 27:
       break
    

cap.release()
cv2.destroyAllWindows()