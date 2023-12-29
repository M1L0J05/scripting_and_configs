#!/bin/bash

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
    echo
    warning_print 'Salida forzada por el usuario. Saliendo...'

	tput cnorm; exit 1
}

tput civis
trap ctrl_c SIGINT # Capturar la interrupción por ctrl+c y lanzar la función ctrl_c

for i in $(seq 1 254); do
    timeout 1 bash -c "ping -c 1 192.168.1.$i" &>/dev/null && success_print "Host 192.168.1.${i} -> Activo!" &
done

wait 
tput cnorm
exit 0