import sys
import getch
import time
import random

random.seed()

def flush_input():
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)

def pintaTerrenoDuelo():
    print("********** A **********")
    for i in range(5):
        print("\n")
    print("-----------------------")
    for i in range(5):
        print("\n")
    print("********** B **********")

def leeDisparo():
    flush_input()
    espera = random.randint(1, 5)
    time.sleep(espera)
    contA = 1
    contB = 1
    print("PUM")
    tecla = getch.getch()
    if tecla is "s":
        print("B is dead")
    elif tecla is "k":
        print("A is dead")

pintaTerrenoDuelo()
for i in range(3):
    campana = random.randint(0, 3)
    time.sleep(0.1)
    print(3-i)
leeDisparo()
