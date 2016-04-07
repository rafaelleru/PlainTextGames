import getch
import sys
import time
import termios

cont = [0, 0]

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def calculaAsterisco(cont1, cont2, positionAsterisco):
    #print(str(cont1) + " -- " + str(cont2) + "======" + str(positionAsterisco))
    if cont1 is 1:
        positionAsterisco -= 1
    elif cont2 is 1:
        positionAsterisco += 1
    return positionAsterisco

def win():
    if positionAsterisco is 1:
        print("win player 1")
        return True
    elif positionAsterisco is tamCuerda-1:
        print("win player 2")
        return True
    else:
        return False

def pintar(positionAsterisco, tamCuerda):
    cuerda = ""
    espacio = ""
    for i in range(50):
        print('*')
    for i in range(tamCuerda):
        if i is not positionAsterisco:
            cuerda += "-"
        else:
            cuerda += "*"

    print(cuerda)

def leerTeclado():
    tecla = getch.getch()
    if tecla is "a":
        cont[0] = 1
        cont[1]= 0
    elif tecla is "l":
        cont[1]=1
        cont[0] = 0
positionAsterisco = 15
tamCuerda = 32
flush_input()
pintar(positionAsterisco, tamCuerda)

while not win():
    leerTeclado()
    positionAsterisco = calculaAsterisco(cont[0], cont[1], positionAsterisco)
    pintar(positionAsterisco, tamCuerda)
