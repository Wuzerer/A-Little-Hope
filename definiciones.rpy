# --- 1. Definición del 'warp' de tiempo para la disolución ---
# Este bloque 'init python' asegura que la función se define antes de que Ren'Py
# necesite usarla para las transiciones.
init python:
    # La función eyewarp ajusta la velocidad de la transición.
    # Un valor de x**1.33 significa que el inicio es más lento y acelera,
    # lo cual es natural para una apertura de ojo.
    def eyewarp(x):
        return x**1.33

# --- 2. Definición de las transiciones personalizadas ImageDissolve ---
# Coloca estas definiciones al inicio de tu script o en un archivo de definiciones.

# Efecto de apertura de ojo LENTO
# Utiliza gui/eye.png como mapa de disolución.
# La disolución procede desde las áreas más blancas (centro) hacia las más negras (bordes).
# 'reverse=False' significa que la imagen revelará la escena.
# Hemos aumentado la duración a 2.0 segundos para un efecto más lento.
define eye_open_slow_effect = ImageDissolve("gui/eye.png", 2.0, ramplen=128, reverse=False, time_warp=eyewarp)

# Efecto de cierre de ojo LENTO
# Utiliza la misma imagen, pero en modo 'reverse=True'.
# Esto hará que la disolución proceda desde las áreas más negras hacia las más blancas,
# cubriendo la pantalla con el color de la escena anterior o negro.
# Hemos aumentado la duración a 2.0 segundos para un efecto más lento.
define eye_close_slow_effect = ImageDissolve("gui/eye.png", 2.0, ramplen=128, reverse=True, time_warp=eyewarp)

# --- Imágenes auxiliares para el ejemplo (ya las tenías) ---
image black:
    Solid("#000")
image white:
    Solid("#FFF")

# NUEVA VARIABLE: Guardará la primera acción del personaje.
# La dejamos vacía al principio.
default accion_inicial = ""

# En definitions.rpy
define pensando = Character(None,
                            what_italic=True,
                            what_color="#cccccc",
                            what_prefix='"',
                            what_suffix='"')

# Define un efecto de flash rojo que se usará cuando el jugador falle en el minijuego.
define redflash = Fade(0.1, 0.1, 0.5, color="#a30000")

default last_fight_result = "none"


# Le decimos a Ren'Py que el nombre "emily normal" ahora se refiere a nuestro nuevo archivo.
image emily normal = "images/sprites/emily/normal.png"
image emily triste = "images/sprites/emily/triste.png"
image emily enojada = "images/sprites/emily/enojada.png"
image emily preocupada = "images/sprites/emily/preocupada.png"
image emily feliz = "images/sprites/emily/feliz.png"

image mana normal = "images/sprites/mana/normal.png"
image mana triste = "images/sprites/mana/triste.png"
image mana enojada = "images/sprites/mana/enojada.png"
image mana preocupada = "images/sprites/mana/preocupada.png"

image ana normal = "images/sprites/ana/normal.png"
image ana enojada = "images/sprites/ana/enojada.png"
image ana preocupada = "images/sprites/ana/normal.png"
image ana feliz = "images/sprites/ana/normal.png"
image ana pijamada1 = "images/sprites/ana/pijama_nerviosa.png"
image ana pijamada dando = "images/sprites/ana/pijamada1.png"
image ana pijamada normal = "images/sprites/ana/pijamada2.png"
image ana pijamada superfeliz = "images/sprites/ana/pijama_super_feliz.png"
image ana pijamada tristeosito = "images/sprites/ana/pjama_ositotriste.png"
image ana pijama normal = "images/sprites/ana/evento/ana_sinosito_normal.png"
image ana pijama triste = "images/sprites/ana/pajama_sad.png"
image ana pijama sad = "images/sprites/ana/evento/ana_sinosito_triste2.png"

#-----------------------------------------------------------------------------------------
# 1
# Definí dos rutas base de nombre de sprite al principio de la historia (después de la decisión del osito):
init python:
    # Estos nombres deben coincidir con los que usás para las imágenes definidas en imágenes.rpy o donde sea que declares tus sprites
    ANA_CON_OSITO = "ana_conosito_"
    ANA_SIN_OSITO = "ana_sinosito_"

# 2
# Después de la decisión, guardás en una variable cuál va a ser la "base" del sprite de Ana:

# 3
# label continuar_f_route1:
#   if tomo_osito:
#       $ ana_sprite_base = ANA_SIN_OSITO
#   else:
#       $ ana_sprite_base = ANA_CON_OSITO

# 3
# Y luego, cada vez que quieras mostrar a Ana con una expresión, hacés algo así:

#    show expression ana_sprite_base + "feliz" at right

# -------------------------------------------------------------------------------------

# Le decimos a Ren'Py que el nombre del "Fondo" ahora se refiere a nuestro nuevo archivo.

image bg f_cuarto = "images/backgrounds/f_cuarto.png"
image bg m_cuarto = "images/backgrounds/m_cuarto.png"

#--------------------------------------------------------------------------------------

#Primera escena con o sin osito de ana:
init python:
    ESCENA_CON_OSITO = "escena_conosito_"
    ESCENA_SIN_OSITO = "escena_sinosito_"

# 2 
#Después de la decisión, guardás en una variable cuál va a ser la "base" del sprite de Ana:

# 3
# Y luego, cada vez que quieras mostrar la escena con la decision tomada, hacés algo así:
# scene expression escena_base + "1"



#--------------------------------------------------------------------------------------

transform salir_izquierda:
    linear 0.5 xalign -1.0

#--------------------------------------------------------------------------------------
# Función auxiliar opcional
init python:
    def mostrar_ana(expresion, posicion="right", transicion="dissolve"):
        for nombre in ["feliz", "normal", "triste", "triste2"]:
            renpy.hide(ana_sprite_base + nombre)
        renpy.show(ana_sprite_base + expresion, at_list=[posicion], tag="ana_sprite")
        renpy.with_statement(transicion)

# $ mostrar_ana("triste2")

# Para salir de escena
# $ mostrar_ana("triste2", "salir_izquierda", "moveoutleft")
#---------------------------------------------------------------------------------------
