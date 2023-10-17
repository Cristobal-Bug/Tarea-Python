import pygame 
import time
import threading
import time
import sys

pygame.init()

matriz = []
for i in range(50):
   vector = []
   for j in range(30):
      vector.append('.')
   matriz.append(vector)

pila = []
for i in range(150):
   datos = []
   datos.append(-1)     
   datos.append(-1)     
   datos.append('x')    
   pila.append(datos)
   

posPila = 0;
wait = 0.5  

pantalla = pygame.display.set_mode((1920,1080))


ColorNegro = (0,0,0)
ColorBlanco = (255,255,255)

ColorVerde = (0,255,0)
ColorAzul = (0,0,255)
ColorRojo = (255,0,0)

ColorPared = ColorBlanco

def arriba(x,y):
   global matriz
   global wait
   global pila
   global posPila
      
   i = y
   while (i >= 0) and (matriz[x][i] == '.'):
      matriz[x][i] = '-'
      time.sleep(wait)
      pygame.draw.rect(pantalla,[255,255,255],( (x*10 + 150,i*10 + 150,10,10) ))
      pygame.display.update()
      
      if (x > 0) and (matriz[x - 1][i] == '.'):       
         pila[posPila][0] = x - 1
         pila[posPila][1] = i
         pila[posPila][2] = 'Izquierda'
         posPila = posPila + 1
      if (x < 49) and (matriz[x + 1][i] == '.'):       
         pila[posPila][0] = x + 1
         pila[posPila][1] = i
         pila[posPila][2] = 'Derecha'
         posPila = posPila + 1

      i -= 1
   if i >= 0 and matriz[x][i] == 'V':
      print('Ventana encontrada en la matriz, posicion: (',x,',',y,')')
      exit

def abajo(x,y):
   global matriz
   global wait
   global pila
   global posPila
    
   i = y
   while (i <= 29) and (matriz[x][i] == '.'):
      matriz[x][i] = '-'
      time.sleep(wait)
      pygame.draw.rect(pantalla,[255,255,255],( (x*10 + 150,i*10 + 150,10,10) ))
      pygame.display.update()
      
      if (x > 0) and (matriz[x - 1][i] == '.'):
         pila[posPila][0] = x - 1
         pila[posPila][1] = i
         pila[posPila][2] = 'Izquierda'
         posPila = posPila+1
      if (x < 49) and (matriz[x+1][i] == '.'):
         pila[posPila][0] = x + 1
         pila[posPila][1] = i
         pila[posPila][2] = 'Derecha'
         posPila = posPila+1
      i += 1
   if i < 30 and matriz[x][i]== 'V':
      print('Ventana encontrada en la matriz, posicion: (',x,',',y,')')
      exit

def izquierda(x,y):
   global matriz
   global wait
   global pila
   global posPila
  
   i = x
   while (i >= 0) and (matriz[i][y] == '.'):
      matriz[i][y] = '-'
      time.sleep(wait)
      pygame.draw.rect(pantalla,[255,255,255],( (i*10 + 150,y*10 + 150,10,10) ))
      pygame.display.update()
      
      if (y > 0) and (matriz[i][y - 1] == '.'):
         pila[posPila][0] = i
         pila[posPila][1] = y - 1
         pila[posPila][2] = 'Arriba'
         posPila = posPila+1
      if (y < 29) and (matriz[i][y + 1] == '.'):
         pila[posPila][0] = i
         pila[posPila][1] = y + 1
         pila[posPila][2] = 'Abajo'
         posPila = posPila+1
      i -= 1
   if i >=0 and matriz[i][y]== 'V':
      print('Ventana encontrada en la matriz, posicion:(',x,',',y,')')
      exit

def derecha(x,y):
   global matriz
   global wait
   global pila
   global posPila

   i = x
   while (i <= 49) and (matriz[i][y] == '.'):
      matriz[i][y] = '-'
      time.sleep(wait)
      pygame.draw.rect(pantalla,[255,255,255],( (i*10 + 150,y*10 + 150,10,10) ))
      pygame.display.update()
      
      if (y > 0) and (matriz[i][y - 1] == '.'):
         pila[posPila][0] = i
         pila[posPila][1] = y - 1
         pila[posPila][2] = 'Arriba'
         posPila = posPila + 1
      if (y < 29) and (matriz[i][y + 1] == '.'):
         pila[posPila][0] = i
         pila[posPila][1] = y + 1
         pila[posPila][2] = 'Abajo'
         posPila = posPila + 1

      i += 1
   if i < 50 and matriz[i][y] == 'V':
      print('Ventana encontrada en la matriz, posicion: (',x,',',y,')')
      exit

pygame.draw.rect(pantalla,ColorAzul,( (150,150,500,300)))

archivo = open("C:/Users/crist/Desktop/Tarea Python/Laberinto.txt","r")
datos = archivo.readlines()
for dato in datos:
   posicion = dato.split(',')
   PosicionY = (int(posicion[0]))*10 + 150
   PosicionX = (int(posicion[1]))*10 +150
 
   if (posicion[2] == "V\n"):
      pygame.draw.rect(pantalla,ColorVerde,( (PosicionX,PosicionY,10,10) ))
      matriz[int(posicion[1])][int(posicion[0])] = 'V'
   else:
      pygame.draw.rect(pantalla,ColorRojo,( (PosicionX,PosicionY,10,10) ))
      matriz[int(posicion[1])][int(posicion[0])] = 'X'
      

pygame.display.update()

abajo(0,0)  

while posPila > 0:
   posPila = posPila-1
   columna = pila[posPila][1]
   fila = pila[posPila][0]  
   accion = pila[posPila][2]
   match accion:
      case 'Arriba':
         arriba(fila,columna)
      case 'Abajo':
         abajo(fila,columna)
      case 'Izquierda':
         izquierda(fila,columna)
      case 'Derecha':
         derecha(fila,columna)           

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()    
