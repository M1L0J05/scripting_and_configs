#!/usr/bin/python3

### IMPORTS STANDARDS ###
import sys, time, signal

### IMPORTS DE TERCEROS ###

### IMPORTS LOCALES ###


### Paleta de colores ###
### FUNCIONES PREDEFINIDAS PARA IMPRIMIR EN COLORES ###
def error_1(skk): print("\033[91m{}\033[0m" .format(skk))       ###--- ROJO 1 ---###
def error_2(skk): print("\033[1;91m{}\033[0m" .format(skk))     ###--- ROJO 2 ---###
def info_1(skk): print("\033[34m{}\033[0m" .format(skk))        ###--- AZUL 1 ---###
def info_2(skk): print("\033[1;34m{}\033[0m" .format(skk))      ###--- AZUL 2 ---###
def info_3(skk): print("\033[96m{}\033[0m" .format(skk))        ###--- CYAN 1 ---###
def info_4(skk): print("\033[1;96m{}\033[0m" .format(skk))      ###--- CYAN 2 ---###
def succes_1(skk): print("\033[32m{}\033[0m" .format(skk))      ###--- VERDE 1 ---###
def succes_2(skk): print("\033[1;32m{}\033[0m" .format(skk))    ###--- VERDE 2 ---###
def warning_1(skk): print("\033[33m{}\033[0m" .format(skk))     ###--- AMARILLO 1 ---###
def warning_2(skk): print("\033[1;33m{}\033[0m" .format(skk))   ###--- AMARILLO 2 ---###
def debug_1(skk): print("\033[90m{}\033[0m" .format(skk))       ###--- GRIS 1 ---###
def debug_2(skk): print("\033[1;90m{}\033[0m" .format(skk))     ###--- GRIS 2 ---###
def debug_3(skk): print("\033[95m{}\033[0m" .format(skk))       ###--- PURPURA 1 ---###
def debug_4(skk): print("\033[1;95m{}\033[0m" .format(skk))     ###--- PURPURA 2 ---###
def others_1(skk): print("\033[30m{}\033[0m" .format(skk))      ###--- NEGRO 1 ---###
def standard_1(skk): print("\033[37m{}\033[0m" .format(skk))    ###--- BLANCO 1 ---###
def standard_2(skk): print("\033[1;37m{}\033[0m" .format(skk))  ###--- BLANCO 2 ---###


### Funcion de captura de Ctrl+c ###
def sig_handler(sig, frame):
    info_1("\n\n[!] Saliendo del programa ...\n")
    sys.exit(1) 

signal.signal(signal.SIGINT, sig_handler)


def banner():
    succes_1("""                                                                """)
    time.sleep(0.05)
    succes_1("""                                                                """)
    time.sleep(0.05)
    succes_1("""  @@@@@@   @@@@@@@   @@@@@@@@   @@@@@@           @@@@@@@    @@@ """)
    time.sleep(0.05)
    succes_1(""" @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@          @@@@@@@   @@@@ """)
    time.sleep(0.05)
    succes_1(""" @@!  @@@  @@!  @@@  @@!       @@!  @@@          !@@      @@@!! """)
    time.sleep(0.05)
    succes_1(""" !@!  @!@  !@!  @!@  !@!       !@!  @!@          !@!        !@! """)
    time.sleep(0.05)
    succes_1(""" @!@!@!@!  @!@!!@!   @!!!:!    @!@!@!@!          !!@@!!     @!@ """)
    time.sleep(0.05)
    succes_1(""" !!!@!!!!  !!@!@!    !!!!!:    !!!@!!!!          @!!@!!!    !@! """)
    time.sleep(0.05)
    succes_1(""" !!:  !!!  !!: :!!   !!:       !!:  !!!              !:!    !!: """)
    time.sleep(0.05)
    succes_1(""" :!:  !:!  :!:  !:!  :!:       :!:  !:!              !:!    :!: """)
    time.sleep(0.05)
    succes_1(""" ::   :::  ::   :::   :: ::::  ::   :::          :::: ::    ::: """)
    time.sleep(0.05)
    succes_1("""  :   : :   :   : :  : :: ::    :   : :          :: : :      :: """)
    time.sleep(0.05)
    succes_1("""                                                                """)
    time.sleep(0.05)
    succes_1("""                                                                """)
    time.sleep(0.05)
    info_1('###############################################################')
    time.sleep(0.05)
    info_1('###############################################################')
    time.sleep(0.05)
    info_1('##                                                           ##')
    time.sleep(0.05)
    info_1('##                      SPIDER-NET MENU                      ##')
    time.sleep(0.05)
    info_1('##                                                           ##')
    time.sleep(0.05)
    info_1('###############################################################')
    time.sleep(0.05)
    info_1('###############################################################')
    time.sleep(0.05)

def tituloApp():
    info_1('###############################################################')
    time.sleep(0.05)
    info_1('###############################################################')
    time.sleep(0.05)
    info_1('##                                                           ##')
    time.sleep(0.05)
    info_1('##                      SPIDER-NET MENU                      ##')
    time.sleep(0.05)
    info_1('##                                                           ##')
    time.sleep(0.05)
    info_1('###############################################################')
    time.sleep(0.05)
    info_1('###############################################################')
    time.sleep(0.05)
