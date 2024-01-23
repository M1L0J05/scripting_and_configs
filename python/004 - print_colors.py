

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
def info_2(text, bold=False): print(color_text(text, COLOR_CYAN, bold=bold))       ###--- CYAN ---###
def succes(text, bold=False): print(color_text(text, COLOR_GREEN, bold=bold))    ###--- VERDE ---###
def warning(text, bold=False): print(color_text(text, COLOR_YELLOW, bold=bold))  ###--- AMARILLO ---###
def debug(text, bold=False): print(color_text(text, COLOR_PURPLE, bold=bold))    ###--- PURPURA ---###
def debug_2(text, bold=False): print(color_text(text, COLOR_GRAY, bold=bold))      ###--- GRIS ---###
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


# Uso de clases para su mejor importacion desde un modulo externo.
class ColorPrint:
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

    def __init__(self, color_code, bold=False):
        self.color_code = color_code
        self.bold_code = '1;' if bold else ''

    def color_text(self, text):
        return f"\033[{self.bold_code}{self.color_code}m{text}\033[0m"

    def print_message(self, text):
        print(self.color_text(text))


# Crear instancias para cada color
red_printer = ColorPrint(ColorPrint.COLOR_RED, bold=True)
blue_printer = ColorPrint(ColorPrint.COLOR_BLUE)
cyan_printer = ColorPrint(ColorPrint.COLOR_CYAN)
green_printer = ColorPrint(ColorPrint.COLOR_GREEN, bold=True)
yellow_printer = ColorPrint(ColorPrint.COLOR_YELLOW, bold=True)
gray_printer = ColorPrint(ColorPrint.COLOR_GRAY, bold=True)
purple_printer = ColorPrint(ColorPrint.COLOR_PURPLE, bold=True)
black_printer = ColorPrint(ColorPrint.COLOR_BLACK, bold=True)
white_printer = ColorPrint(ColorPrint.COLOR_WHITE, bold=True)

# Ejemplo de uso
red_printer.print_message('[ERROR] Algo salió mal en rojo.')
blue_printer.print_message('[INFO] Esta es una información en azul.')
cyan_printer.print_message('[INFO] Esta es una información en cyan.')
green_printer.print_message('[ÉXITO] Operación completada con éxito en verde.')
yellow_printer.print_message('[ADVERTENCIA] Tenga cuidado en amarillo.')
gray_printer.print_message('[DEBUG] Este es un mensaje de depuración en gris.')
purple_printer.print_message('[DEBUG] Este es un mensaje de depuración en purpura.')
black_printer.print_message('[OTRO] Otro mensaje en negro.')
white_printer.print_message('[ESTÁNDAR] Este es un mensaje estándar en blanco.')
