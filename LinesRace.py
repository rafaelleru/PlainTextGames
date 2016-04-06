import sys
import getch
import time
import termios

cont = [0, 0, 0]
empezar = False
tecla = ""
tope = 50

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)


def pintaAsteriscos():
    asteriscos = ""
    for i in range(tope):
        print('*')
        asteriscos = asteriscos + "*"
    print(asteriscos)

def pintaLineas(tam1, tam2, tam3):
    lineas1 = ""
    lineas2 = ""
    lineas3 = ""
    for i in range(tam1):
        lineas1 = lineas1 + "-"
    for j in range(tam2):
        lineas2=lineas2 + "-"
    for k in range(tam3):
        lineas3=lineas3 + "-"
    pintaAsteriscos()
    print(lineas1 + "\n" + lineas2 + "\n" + lineas3)

def juego():
    descartando = True
    flush_input()
    while cont[0] < tope and cont[1] < tope and cont[2] < tope:
        #sys.stdin.flush()
        '''if descartando:
            for i in range(100):
                descartar = getch.getch()
            descartando = False
        '''
        tecla = getch.getch()
        if tecla is "a":
            cont[0]+=1
        elif tecla is "l":
            cont[1]+=1
        elif tecla is "b":
            cont[2]+=1
        pintaLineas(cont[0], cont[1], cont[2])

    max = 0;
    for num in range(3):
        if cont[num] > max:
            max = num
    print("gana el " + str(max+1))

    print(str(cont[0]) + " - " + str(cont[1]) + "-" + str(cont[2]))

for i in range(3):
    print("Empieza en " + str(3-i))
    time.sleep(0.5)
    if i is 2:
        empezar = True

print("vamonos atomos")
#termios.tcflush(sys.stdin, termios.TCIOFLUSH)
if empezar:
    juego()

time.sleep(3)
