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
#set -o xtrace # Descomentar si desea depurar

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

# Variables Globales
main_url="https://htbmachines.github.io/bundle.js"
main_dir="/home/$USER/aaa_hackTheBoxSearch"  

# Funcion del panel de ayuda.
function help_panel () {
    echo
    info_print 'Panel de opciones disponibles:'
    echo -e "\t${events_color}-u${end_color} -> Descargar o actualizar los archivos necesarios."
    echo -e "\t${events_color}-m${end_color} -> Busca por el nombre de máquina resuelta."
    echo -e "\t${events_color}-h${end_color} -> Muestra este panel de opciones."
    echo
    tput cnorm; exit 0
}

# Funciones para opciones.
function update_files () {
    tput civis
    
    if [ ! -d "${main_dir}" ]; then
        echo
        info_print "Comprobando las dependencias."
        
        if ! which sponge >/dev/null || ! which js-beautify >/dev/null; then
            warning_print "Comprueba que SPONGE y JS-BEAUTIFY están instalados!!"
            exit 1
        fi

        info_print "Creando el directorio de trabajo hackTheBoxSearch"
        mkdir ${main_dir}
        success_print "Directorio creado correctamente."
        info_print "Obteniendo los datos..."
        curl -s -X GET ${main_url} > "${main_dir}/hackthebox_data.js"
        js-beautify ${main_dir}/hackthebox_data.js | sponge ${main_dir}/hackthebox_data.js
        success_print "Datos obtenidos correctamente."

    else
        echo
        info_print "Comprobando si existe una actualizacón de los datos..."

        if [ ! -f "${main_dir}/hackthebox_data.js" ]; then
            touch ${main_dir}/hackthebox_data.js
        fi
        
        curl -s -X GET ${main_url} > "${main_dir}/hackthebox_data_tmp.js"
        js-beautify ${main_dir}/hackthebox_data_tmp.js | sponge ${main_dir}/hackthebox_data_tmp.js

        local md5_bundle=$(md5sum ${main_dir}/hackthebox_data.js | awk '{print $1}')
        local md5_tmp=$(md5sum ${main_dir}/hackthebox_data_tmp.js | awk '{print $1}')

        if [ "$md5_bundle" == "$md5_tmp" ]; then
            rm ${main_dir}/hackthebox_data_tmp.js
            success_print "No existen actualizaciones."

        else
            rm ${main_dir}/hackthebox_data.js 
            mv ${main_dir}/hackthebox_data_tmp.js ${main_dir}/hackthebox_data.js
            success_print "Actualizado correctamente."
        fi

    fi

    tput cnorm; exit 0
}

function search_machine () {
    tput civis
    local machine_name="$1"
    echo
    success_print "$machine_name"
    info_print "Listado de propiedades:"
    
    cat ${main_dir}/hackthebox_data.js | awk "/name: \"${machine_name}\"/,/resuelta:/" | grep -vE "id:|sku:" 
    
    tput cnorm; exit 0
}

# Bloque para declarar parametros
declare -i parameter_counter=0

while getopts "hum:" arg 2>/dev/null; do
    case $arg in
        h) help_panel;;
        u) update_files; let parameter_counter+=1;;
        m) machine_name=$OPTARG; let parameter_counter+=2;;
        
        # Agrega un caso '*' en el bloque case para manejar opciones desconocidas y mostrar un mensaje de error y el panel de ayuda antes de salir.
        *) echo -e '\n'; error_print "Opción desconocida, ingrese una de las especificadas en el panel de ayuda."; tput cnorm; help_panel; exit 1;;
    esac
done

# Función principal.
main() {
    
    tput civis # Oculta el cursor.

    # La lógica de tu script aquí
    
    if [ $parameter_counter -lt 1 ]; then
        echo 
        warning_print 'Especifica las opciones.'
        help_panel
        tput cnorm; exit 1
    
    elif [ $parameter_counter -eq 2 ]; then
        search_machine $machine_name
    fi

    tput cnorm # Muestra el cursor.
}

main 


