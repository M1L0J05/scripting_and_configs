#!/usr/bin/python3

import  sys, time, signal

### Paleta de colores ###
def prRed(skk): print("\033[91m{}\033[0m" .format(skk))
def prBlue(skk): print("\033[34m{}\033[0m" .format(skk))
def prGreen(skk): print("\033[32m{}\033[0m" .format(skk))
def prYellow(skk): print("\033[93m{}\033[0m" .format(skk))
def prPurple(skk): print("\033[95m{}\033[0m" .format(skk))
def prCyan(skk): print("\033[96m{}\033[0m" .format(skk))
def prGray(skk): print("\033[90m{}\033[0m" .format(skk))
def prBlack(skk): print("\033[30m{}\033[0m" .format(skk))
def prWhite(skk): print("\033[37m{}\033[0m" .format(skk))


### Funcion de captura de Ctrl+c ###
def sig_handler(sig, frame):
    prBlue("\n\n[*] Saliendo del programa ...\n")
    sys.exit(0) 

signal.signal(signal.SIGINT, sig_handler)

prBlue("""                                                        ,----,.           """)
prBlue("""                                                     ,'   ,'  |           """)
prBlue("""    ,---,                                           ,'   .'   |     ,---, """)
prBlue("""   '  .' \                                        ,----.'    .'  ,`--.' | """)
prBlue("""  /  ;    '.      __  ,-.                         |    |   .'   /    /  : """)
prBlue(""" :  :       \   ,' ,'/ /|                         :    :  |--, :    |.' ' """)
prBlue(""" :  |   /\   \  '  | |' | ,---.     ,--.--.       :    |  ;.' \`----':  | """)
prBlue(""" |  :  ' ;.   : |  |   ,'/     \   /       \      |    |      |   '   ' ; """)
prBlue(""" |  |  ;/  \   ;'  :  / /    /  | .--.  .-. |     `----'.'\   ;   |   | | """)
prBlue(""" '  :  | \  \ ,'|  | ' .    ' / |  \__\/: . .       __  \  .  |   '   : ; """)
prBlue(""" |  |  '  '--'  ;  : | '   ;   /|  ," .--.; |     /   /\/  /  :   |   | ' """)
prBlue(""" |  :  :        |  , ; '   |  / | /  /  ,.  |    / ,,/  ',-   .   '   : | """)
prBlue(""" |  | ,'         ---'  |   :    |;  :   .'   \   \ ''\       ;    ;   |.' """)
prBlue(""" `--''                  \   \  / |  ,     .-./    \   \    .'     '---'   """)
prBlue("""                         `----'   `--`---'         `--`-,-'               """)
                                                                              

prBlue("""   _____                          .____________ """)
prBlue("""  /  _  \_______   ____ _____     |   ____/_   |""")
prBlue(""" /  /_\  \_  __ \_/ __ \\\__  \    |____  \ |   |""")
prBlue("""/    |    \  | \/\  ___/ / __ \_  /       \|   |""")
prBlue("""\____|__  /__|    \___  >____  / /______  /|___|""")
prBlue("""        \/            \/     \/         \/      """)
prBlue("""                                                """)

                                                              
prBlue("""  @@@@@@   @@@@@@@   @@@@@@@@   @@@@@@      @@@@@@@    @@@ """)
prBlue(""" @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@     @@@@@@@   @@@@ """)
prBlue(""" @@!  @@@  @@!  @@@  @@!       @@!  @@@     !@@      @@@!! """)
prBlue(""" !@!  @!@  !@!  @!@  !@!       !@!  @!@     !@!        !@! """)
prBlue(""" @!@!@!@!  @!@!!@!   @!!!:!    @!@!@!@!     !!@@!!     @!@ """)
prBlue(""" !!!@!!!!  !!@!@!    !!!!!:    !!!@!!!!     @!!@!!!    !@! """)
prBlue(""" !!:  !!!  !!: :!!   !!:       !!:  !!!         !:!    !!: """)
prBlue(""" :!:  !:!  :!:  !:!  :!:       :!:  !:!         !:!    :!: """)
prBlue(""" ::   :::  ::   :::   :: ::::  ::   :::     :::: ::    ::: """)
prBlue("""  :   : :   :   : :  : :: ::    :   : :     :: : :      :: """)
                                                              



while True:
    cmd = input("$~ ")
    print(cmd)