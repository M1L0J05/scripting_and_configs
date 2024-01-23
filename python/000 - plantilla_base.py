#!/usr/bin/python3

### IMPORTS STANDARDS ###
import sys, time, signal

### IMPORTS DE TERCEROS ###

### IMPORTS LOCALES ###


# Colores y estilos
COLOR_RED = '91'
COLOR_BLUE = '34'
COLOR_CYAN = '96'
COLOR_GREEN = '32'
COLOR_YELLOW = '33'
COLOR_GRAY = '90'
COLOR_PURPLE = '95'
COLOR_BLACK = '30'
COLOR_WHITE = '37'

# Funcion generica para imprimir en color
def color_text(text, color_code, bold=False):
    bold_code = '1;' if bold else ''    
    return f"\033[{bold_code}{color_code}m{text}\033[0m"

# Funciones de impresión
def error(text, bold=False): print(color_text(text, COLOR_RED, bold=bold))       ###--- ROJO ---###
def info(text, bold=False): print(color_text(text, COLOR_BLUE, bold=bold))       ###--- AZUL ---###
def info_2(text, bold=False): print(color_text(text, COLOR_CYAN, bold=bold))     ###--- CYAN ---###
def succes(text, bold=False): print(color_text(text, COLOR_GREEN, bold=bold))    ###--- VERDE ---###
def warning(text, bold=False): print(color_text(text, COLOR_YELLOW, bold=bold))  ###--- AMARILLO ---###
def debug(text, bold=False): print(color_text(text, COLOR_PURPLE, bold=bold))    ###--- PURPURA ---###
def debug_2(text, bold=False): print(color_text(text, COLOR_GRAY, bold=bold))    ###--- GRIS ---###
def others(text, bold=False): print(color_text(text, COLOR_BLACK, bold=bold))    ###--- NEGRO ---###
def standard(text, bold=False): print(color_text(text, COLOR_WHITE, bold=bold))  ###--- BLANCO ---###

# Ejemplo de uso
# Funciones prediseñadas
info('[INFO] Esta es una información en azul.', bold=True)
info_2('[INFO] Esta es una información en cyan.')
error('[ERROR] Algo salió mal en rojo.')
succes('[ÉXITO] Operación completada con éxito en verde.')
warning('[ADVERTENCIA] Tenga cuidado en amarillo.')
debug('[DEBUG] Este es un mensaje de depuración en purpura.')
debug_2('[DEBUG] Este es un mensaje de depuración en gris.')
others('[OTRO] Otro mensaje en negro.')
standard('[ESTÁNDAR] Este es un mensaje estándar en blanco.')

# Funcion generica
print(color_text('[+] Probando la funcion generica', COLOR_BLUE, bold=True))


### Funcion de captura de Ctrl+c ###
def sig_handler(sig, frame):
    warning("\n\n[!] Ejecucion cancelada por el usuario ...\n")
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
