#!/usr/bin/python3

import  sys

### Paleta de colores ###
#count=0
#while count < 110:
#    print("{} -- \033[{}m{}\033[0m" .format(count, count, "pruebas"))
#    count+=1

### FUNCIONES PREDEFINIDAS PARA IMPRIMIR EN COLORES ###
def error_1(skk): print("\033[91m{}\033[0m" .format(skk))       ###--- ROJO 1 ---###
def error_2(skk): print("\033[1;91m{}\033[0m" .format(skk))     ###--- ROJO 2 ---###

def info_1(skk): print("\033[34m{}\033[0m" .format(skk))        ###--- AZUL 1 ---###
def info_2(skk): print("\033[1;34m{}\033[0m" .format(skk))      ###--- AZUL 2 ---###

def info_3(skk): print("\033[96m{}\033[0m" .format(skk))        ###--- CYAN 1 ---###
def info_4(skk): print("\033[1;96m{}\033[0m" .format(skk))      ###--- CYAN 2 ---###

def succes_1(skk): print("\033[32m{}\033[0m" .format(skk))      ###--- VERDE 1 ---###
def succes_2(skk): print("\033[1;32m{}\033[0m" .format(skk))    ###--- VERDE 2 ---###

def warning_1(skk): print("\033[93m{}\033[0m" .format(skk))     ###--- AMARILLO 1 ---###
def warning_2(skk): print("\033[1;93m{}\033[0m" .format(skk))   ###--- AMARILLO 2 ---###

def debug_1(skk): print("\033[90m{}\033[0m" .format(skk))       ###--- GRIS 1 ---###
def debug_2(skk): print("\033[1;90m{}\033[0m" .format(skk))     ###--- GRIS 2 ---###

def debug_3(skk): print("\033[95m{}\033[0m" .format(skk))       ###--- PURPURA 1 ---###
def debug_4(skk): print("\033[1;95m{}\033[0m" .format(skk))     ###--- PURPURA 2 ---###

def others_1(skk): print("\033[30m{}\033[0m" .format(skk))      ###--- NEGRO 1 ---###

def standard_1(skk): print("\033[37m{}\033[0m" .format(skk))    ###--- BLANCO 1 ---###
def standard_2(skk): print("\033[1;37m{}\033[0m" .format(skk))  ###--- BLANCO 2 ---###


error_1("--> ERROR_1")
error_2("--> ERROR_2\n")
info_1("--> INFO_1")
info_2("--> INFO_2\n")
info_3("--> INFO_3")
info_4("--> INFO_4\n")
succes_1("--> SUCCESS_1")
succes_2("--> SUCCESS_2\n")
warning_1("--> WARNING_1")
warning_2("--> WARNING_2\n")
debug_1("--> DEBUG_1")
debug_2("--> DEBUG_2\n")
debug_3("--> DEBUG_3")
debug_4("--> DEBUG_4\n")
others_1("--> OTHER_1\n")
standard_1("--> STANDARD_1")
standard_2("--> STANDARD_2\n")

sys.exit(0)
