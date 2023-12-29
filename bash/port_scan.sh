#!/bin/bash

# Common color codes.

# |  Color   | Uso                                      |
# |:--------:| ---------------------------------------- |
# |   Rojo   | Errores y fallos                         |
# | Amarillo | Advertencias y avisos                    |
# |  Verde   | Éxitos y operaciones completadas         |
# |   Azul   | Información general                      |
# |  Morado  | Eventos y notificaciones                 |
# |   Cian   | Depuración (debugging) y trazas          |
# |   Gris   | Información secundaria o menos relevante |

# Conjunto de variables para texto en color

# Colores normales
end_color="\033[0m\e[0m"        #Standard
success_color="\e[0;32m"        #Verde
warning_color="\e[0;33m"        #Amarillo
error_color="\e[0;31m"          #Rojo
info_color="\e[0;34m"           #Azúl
debug_color="\e[0;36m"          #Cian
events_color="\e[0;35m"         #Morado
info2_color="\e[0;37m"          #Gris

# Colores en negrita
success_b_color="\e[0;32m\033[1m"        #Verde
warning_b_color="\e[0;33m\033[1m"        #Amarillo
error_b_color="\e[0;31m\033[1m"          #Rojo
info_b_color="\e[0;34m\033[1m"           #Azúl
debug_b_color="\e[0;36m\033[1m"          #Cian
events_b_color="\e[0;35m\033[1m"         #Morado
info2_b_color="\e[0;37m\033[1m"          #Gris

set -o errexit  # Finaliza el script si un comando falla
set -o pipefail # Finaliza el script si un comando falla en una tubería (pipe)
set -o nounset  # Finaliza el script si se usa una variable no declarada
# set -o xtrace # Descomentar si desea depurar

# Funciones para imprimir en colores
function print_color () {
    local color="$1"
    local symbol="$2"
    local message="$3"
    printf "\e[0;%sm[%s] %s\033[0m\n" "$color" "$symbol" "$message"
}

function success_print () { print_color "32" "v" "$1"; }
function warning_print () { print_color "33" "¡" "$1"; }
function error_print   () { print_color "31" "x" "$1"; }
function info_print    () { print_color "34" "i" "$1"; }
function debug_print   () { print_color "36" "d" "$1"; }
function event_print   () { print_color "35" "e" "$1"; }
function other_print   () { print_color "37" "o" "$1"; }

# Función para la acción de ctrl_c.
function ctrl_c () {
    echo -e "\n"
    warning_print 'Salida forzada por el usuario. Saliendo...'

	tput cnorm; exit 1
}

trap ctrl_c SIGINT # Capturar la interrupción por ctrl+c y lanzar la función ctrl_c

# Funcion del panel de ayuda.
function help_panel () {
    echo
    print_color '34' '+' 'Este es el panel de ayuda:'
    warning_print "Especifica la IP -> ${0} -i <ip_addres>"
    tput cnorm; exit 0
}

declare -a ports=( $(seq 1 65535) )

# Funciones para opciones.
function check_ports () {
    tput civis

    local ip=$1
    local port=$2

    (exec 3<> /dev/tcp/$ip/$port) 2>/dev/null
    
    if [ $? -eq 0 ]; then
        success_print "HOST ${ip} - PORT ${port} -> Abierto!"    
    fi
}

# Función para las opciones.
declare -i parameter_counter=0

while getopts "i:h" arg 2>/dev/null; do
    case $arg in
        h) help_panel;;
        i) ip="$OPTARG"; let parameter_counter+=1;;

        # Agrega un caso '*' en el bloque case para manejar opciones desconocidas y mostrar un mensaje de error y el panel de ayuda antes de salir.
        *) echo; error_print "Opción desconocida, ingrese una de las especificadas en el panel de ayuda."; tput cnorm; help_panel; exit 1;;
    esac
done

# Función principal.
main() {
    tput civis # Oculta el cursor.

    if [ $parameter_counter -lt 1 ]; then
        help_panel
        tput cnorm; exit 1
    
    fi
    
    for port in ${ports[@]}; do
        check_ports ${ip} $port &
    done

    exec 3<&-
    exec 3>&-

    tput cnorm # Muestra el cursor.
    exit 0
}

main 
