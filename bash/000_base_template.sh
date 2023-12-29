#!/bin/bash

##### Codigos de colores habituales.

# |  Color   | Uso                                      |
# |:--------:| ---------------------------------------- |
# |   Rojo   | Errores y fallos                         |
# | Amarillo | Advertencias y avisos                    |
# |  Verde   | Éxitos y operaciones completadas         |
# |   Azul   | Información general                      |
# |  Morado  | Eventos y notificaciones                 |
# |   Cian   | Depuración (debugging) y trazas          |
# |   Gris   | Información secundaria o menos relevante |

#normal_colors
end_color="\033[0m\e[0m"        #Standard
success_color="\e[0;32m"        #Green
warning_color="\e[0;33m"        #Yellow
error_color="\e[0;31m"          #Red
info_color="\e[0;34m"           #Blue
debug_color="\e[0;36m"          #Cian
events_color="\e[0;35m"         #Purple
info2_color="\e[0;37m"          #Gray

#bold_colors
end_color="\033[0m\e[0m"        		 #Standard
success_b_color="\e[0;32m\033[1m"        #Green
warning_b_color="\e[0;33m\033[1m"        #Yellow
error_b_color="\e[0;31m\033[1m"           #Red
info_b_color="\e[0;34m\033[1m"           #Blue
debug_b_color="\e[0;36m\033[1m"          #Cian
events_b_color="\e[0;35m\033[1m"         #Purple
info2_b_color="\e[0;37m\033[1m"          #Gray

#Functions to print in colors
function success_print () { 
    printf "\e[0;32m[v] %s \033[0m\n" "$1"
}
function warning_print () { 
    printf "\e[0;33m[¡] %s\033[0m\n" "$1" 
}
function error_print () { 
    printf "\e[0;31m[x] %s\033[0m\n" "$1" 
}
function info_print () { 
    printf "\e[0;34m[i] %s\033[0m\n" "$1" 
}
function debug_print () { 
    printf "\e[0;36m[d] %s\033[0m\n" "$1" 
}
function event_print () { 
    printf "\e[0;35m[e] %s\033[0m\n" "$1" 
}
function other_print () { 
    printf "\e[0;37m[o] %s\033[0m\n" "$1" 
}

#Function for the ctrl_c action.
function ctrl_c(){
	echo -e "\n\n${warning_color}[!] User forced exit. Exiting...\n${end_color}"
	
	tput cnorm; exit 1
}

tput civis

echo -e "\nNormal color"
echo -e "\n${success_color}Probando los colores. ${end_color}"
echo -e "${warning_color}Probando los colores. ${end_color}"
echo -e "${error_color}Probando los colores. ${end_color}"
echo -e "${info_color}Probando los colores. ${end_color}"
echo -e "${debug_color}Probando los colores. ${end_color}"
echo -e "${events_color}Probando los colores. ${end_color}"
echo -e "${info2_color}Probando los colores. ${end_color}"

echo -e "\n${success_b_color}Probando los colores. ${end_color}"
echo -e "${warning_b_color}Probando los colores. ${end_color}"
echo -e "${error_b_color}Probando los colores. ${end_color}"
echo -e "${info_b_color}Probando los colores. ${end_color}"
echo -e "${debug_b_color}Probando los colores. ${end_color}"
echo -e "${events_b_color}Probando los colores. ${end_color}"
echo -e "${info2_b_color}Probando los colores. ${end_color}"



trap ctrl_c INT

sleep 30

tput cnorm