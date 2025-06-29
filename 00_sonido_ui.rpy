
# Variable de configuración del jugador
default interfaz_sonido = True

# Función de sonido condicional dentro de init python (evaluada correctamente)
init python:
    def play_ui_sound(path):
        if interfaz_sonido:
            return Play("sound", path)
        else:
            return NullAction()
