#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
susurrador.py
Herramienta para usar Whiper de OpenAI en local.
"""

### IMPORTS STANDARDS ###
import os
import sys 
import time
import signal

### IMPORTS DE TERCEROS ###
import whisper
import ffmpeg
from whisper.utils import WriteTXT

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

### Definicion de Constantes
AUDIOS_DIRECTORY = '/home/susurro/Escritorio/AUDIOS/'


### Funcion de captura de Ctrl+c ###
def sig_handler(sig, frame):
    warning_1("\n\n[!] Saliendo del programa ...\n")
    print('\033[?25h', end='')
    return sys.exit(1) 



### Funcion para visualizar el logo
def banner():
    succes_1('\n\n'+"""  @@@@@@   @@@@@@@   @@@@@@@@   @@@@@@           @@@@@@@    @@@ """)
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
    succes_1("""  :   : :   :   : :  : :: ::    :   : :          :: : :      :: """ + '\n\n')
    time.sleep(0.05)

    succes_1('#'*63)
    time.sleep(0.05)
    succes_1('###'+' '*57+'###')
    time.sleep(0.05)
    succes_1('###'+' '*18+'>>> EL SUSURRADOR <<<'+' '*18+'###')
    time.sleep(0.05)
    succes_1('###'+' '*57+'###')
    time.sleep(0.05)
    succes_1('#'*63+'\n')
    time.sleep(1)
    

def check_one_file(audios_directory):
    files = os.listdir(audios_directory)

    if len(files) != 1:
        warning_1('#'*63)
        time.sleep(0.05)
        warning_1('###'+' '*57+'###')
        time.sleep(0.05)
        warning_1('###'+' '*14+'COMPRUEBE LA CARPETA "AUDIOS"'+' '*14+'###')
        time.sleep(0.05)
        warning_1('###'+' '*57+'###')
        time.sleep(0.05)
        warning_1('###'+' '*11+'Está vacia o tiene más de 1 archivo'+' '*11+'###')
        time.sleep(0.05)
        warning_1('###'+' '*57+'###')
        time.sleep(0.05)
        warning_1('#'*63+'\n')
        time.sleep(0.05)

        return sys.exit(1)
    
    else: 
        audio_file = AUDIOS_DIRECTORY + files[0]
    
        return audio_file


def not_directory_audio():
    error_1('#'*63)
    time.sleep(0.05)
    error_1('###'+' '*57+'###')
    time.sleep(0.05)
    error_1('###'+' '*15+'NO EXISTE CARPETA DE AUDIOS'+' '*15+'###')
    time.sleep(0.05)
    error_1('###'+' '*57+'###')
    time.sleep(0.05)
    error_1('#'*63+'\n')
    time.sleep(0.05)

    return sys.exit(1)


def file_not_valid():
    error_1('#'*63)
    time.sleep(0.05)
    error_1('###'+' '*57+'###')
    time.sleep(0.05)
    error_1('###'+' '*13+'EL ARCHIVO CARGADO NO ES VALIDO'+' '*13+'###')
    time.sleep(0.05)
    error_1('###'+' '*57+'###')
    time.sleep(0.05)
    error_1('#'*63+'\n')
    time.sleep(0.05)

    return sys.exit(1)


def language_selection():
    info_1('>>> ¿En que idioma está el audio?:\n>>> 1 - Español\n>>> 2 - Inglés\n>>> 3 - Euskera\n')
    
    languages = {
        1:'Español', 
        2:'Inglés', 
        3:'Euskera'
    }

    while True:
        language_selected = input("\033[34m{}\033[0m".format('>>> Introduzca el nº elegido y pulse intro:\t'))
        try:
            language_selected = int(language_selected)
            if  language_selected > 0 and language_selected < 4:
                
                succes_1('>>> El idioma elegido es: '+languages[language_selected]+'\n')
                
                return language_selected
            
            else:
                warning_1('\n[!] Introduce un valor correcto.\n')
                
        except:
            warning_1('\n[!] Introduce un valor correcto.\n')
    

def task_selection():
    info_1('>>> ¿Cómo quiere el texto de la transcripción?\n>>> 1 - Original\n>>> 2 - Inglés\n')
    while True:
        task_selected = input("\033[34m{}\033[0m".format('>>> Introduzca el nº elegido y pulse intro:\t'))
        try:
            task_selected = int(task_selected)
            if task_selected > 0 and task_selected < 3:
                
                if task_selected == 1:
                    succes_1('>>> El archivo de texto se escribira en el idioma original.\n')
                    task = 'transcribe'
                elif task_selected == 2:
                    succes_1('>>> El archivo de texto se escribira en inglés.\n')
                    task = 'translate'

                return task
        
        except:
            warning_1('\n[!] Introduce un valor correcto.\n')
            
                
def audio_process(language_selected, audio_file, task):
    language_transcriptions = {
        1:'Spanish',
        2:'English',
        3:'Basque'
    }
    
    ia_models = {
        1:'tiny',
        2:'base',
        3:'small',
        4:'medium',
        5:'large'
    }

    info_1('>>> Cargando el modelo entrenado en memoria...')
    model = whisper.load_model(ia_models[3])
    succes_1('>>> Modelo cargado en memoria...\n')

    info_1('>>> Procesando archivo de audio...')

    transcription = whisper.transcribe(
        audio = audio_file,
        model = model,
        fp16 = False,
        language = language_transcriptions[language_selected],
        task = task,
        verbose = True
    )

    return transcription


def write_txt(output_directory, result_transcribe, ):
    info_1('\n>>> Creando el archivo de texto...')
    output_file = output_directory + 'transcripcion.txt'    
    txt = open(output_file, 'w')
    WriteTXT(output_dir='').write_result(result=result_transcribe, file=txt, options='')
    txt.close()
    time.sleep(1)
    succes_1('>>> Archivo de texto creado correctamente.\n')


# Función principal
def main():
    """
    Función principal del script.
    """
    
    signal.signal(signal.SIGINT, sig_handler)
    print('\033[?25l', end='')
    
    banner()
    
    try:
        audio_file = check_one_file(AUDIOS_DIRECTORY)
    except FileNotFoundError as e:
        not_directory_audio()

    language = language_selection()
    task = task_selection()
    
    try:
        result = audio_process(language_selected=language, audio_file=audio_file, task=task)
    except RuntimeError as error:
        file_not_valid()

    write_txt(AUDIOS_DIRECTORY, result)

    print('\033[?25h', end='')

    succes_1('\n>>> Proceso terminado con exito.\n\n')

    return sys.exit(0)



# Verifica si el script es el punto de entrada principal
if __name__ == "__main__":
    main()
