# Archivo: minigame_keyboard.rpy
# Descripción: Minijuego de teclado con estilos de texto aleatorios.

# --- 1. Configuración y Variables ---
define minigame_difficulty = "medio"
# El tamaño base ya no es una constante, se definirá en una lista
define SCREEN_WIDTH = 1280
define SCREEN_HEIGHT = 720

init python:
    # Diccionario de dificultad
    difficulty_settings = {
        "facil": 2.0,
        "medio": 1.2,
        "dificil": 0.7
    }
    # Lista de caracteres que pueden aparecer.
    available_keys = "abcdefghijklmnopqrstuvwxyz1234567890"

    # --- NOVEDAD: Listas para estilos aleatorios ---
    # ¡IMPORTANTE! Asegúrate de que los archivos de fuente (.ttf) listados aquí
    # estén físicamente presentes en la carpeta 'game/' de tu proyecto.
    available_fonts = ["DejaVuSans-Bold.ttf", "CHALLXBD.TTF", "Dimbo Regular.ttf", "Fabiana.ttf", "Havana-Regular.ttf", "JdDin-2G4X.ttf", "Neuton-Bold.ttf", "Roboto-Condensed.ttf", "Santuy.otf", "VT323-Regular.ttf"] # Se eliminó "cour.ttf". Añade aquí tus fuentes.

    # Lista de colores en formato hexadecimal.
    available_colors = ["#FFFFFF", "#FF5733", "#33FF57", "#3357FF", "#F1C40F", "#9B59B6", "#3ce7d9", "#055212", "#cc2e8f", "#f31225"]

    # Lista de posibles tamaños para el texto.
    available_sizes = [90, 100, 110, 120, 130]


# --- 2. Variables del Estado del Minijuego ---
default minigame_lives = 3
default minigame_score = 0
default minigame_target_score = 20
default _minigame_bg_image = "" # Variable para el fondo

# --- 3. Pantalla de la Interfaz del Minijuego (Modificada) ---
# La pantalla ahora acepta los nuevos parámetros de estilo.
screen minigame_ui(text_x, text_y, timeout_duration, target_char, char_font, char_color, char_size):
    # Fondo de la pantalla
    add _minigame_bg_image

    # Interfaz (vidas y puntuación)
    hbox:
        xalign 0.02
        yalign 0.02
        spacing 10
        label "Vidas:"
        text "[minigame_lives]"
        label "Aciertos:"
        text "[minigame_score] / [minigame_target_score]"

    # Muestra la letra objetivo con los estilos aleatorios aplicados.
    text target_char:
        pos (text_x, text_y)
        font char_font      # Aplica la fuente aleatoria
        size char_size      # Aplica el tamaño aleatorio
        color char_color     # Aplica el color aleatorio
        outlines [(2, "#000", 0, 0)] # Mantiene un borde negro para la legibilidad

    # Temporizador
    timer timeout_duration action Return(None)

    # Captura de teclas
    key "a" action Return("a")
    key "b" action Return("b")
    key "c" action Return("c")
    key "d" action Return("d")
    key "e" action Return("e")
    key "f" action Return("f")
    key "g" action Return("g")
    key "h" action Return("h")
    key "i" action Return("i")
    key "j" action Return("j")
    key "k" action Return("k")
    key "l" action Return("l")
    key "m" action Return("m")
    key "n" action Return("n")
    key "o" action Return("o")
    key "p" action Return("p")
    key "q" action Return("q")
    key "r" action Return("r")
    key "s" action Return("s")
    key "t" action Return("t")
    key "u" action Return("u")
    key "v" action Return("v")
    key "w" action Return("w")
    key "x" action Return("x")
    key "y" action Return("y")
    key "z" action Return("z")
    key "1" action Return("1")
    key "2" action Return("2")
    key "3" action Return("3")
    key "4" action Return("4")
    key "5" action Return("5")
    key "6" action Return("6")
    key "7" action Return("7")
    key "8" action Return("8")
    key "9" action Return("9")
    key "0" action Return("0")

# --- 4. Lógica y Flujo del Minijuego (Modificado) ---
label start_minigame(bg_image, target_score=10, initial_lives=3):
    $ _minigame_bg_image = bg_image
    $ minigame_lives = initial_lives
    $ minigame_target_score = target_score
    $ minigame_score = 0
    jump minigame_loop

label minigame_loop:
    if minigame_score >= minigame_target_score:
        return "win"
    if minigame_lives <= 0:
        return "lose"

    # Elige una letra aleatoria
    $ random_char = renpy.random.choice(available_keys)

    # --- NOVEDAD: Elige propiedades de texto aleatorias ---
    $ random_font = renpy.random.choice(available_fonts)
    $ random_color = renpy.random.choice(available_colors)
    $ random_size = renpy.random.choice(available_sizes)

    # Calcula una posición aleatoria
    # Ajustamos el cálculo de max_x/y para que dependa del tamaño actual de la letra.
    $ max_x = SCREEN_WIDTH - random_size
    $ max_y = SCREEN_HEIGHT - random_size
    $ rand_x = renpy.random.randint(0, max_x)
    $ rand_y = renpy.random.randint(0, max_y)
    $ timeout_value = difficulty_settings[minigame_difficulty]

    # Llama a la pantalla del minijuego con las nuevas propiedades.
    call screen minigame_ui(
        rand_x,
        rand_y,
        timeout_value,
        target_char=random_char,
        char_font=random_font,
        char_color=random_color,
        char_size=random_size
    )

    # Comprueba si la tecla presionada es la correcta
    if _return == random_char:
        $ minigame_score += 1
    else: # Fallo (tecla incorrecta o tiempo agotado)
        $ minigame_lives -= 1
        with Dissolve(0.1, alpha=True)

    jump minigame_loop

#------------------------------------------------------------------------------

# Archivo: chapter1_male_route.rpy
# Descripción: Ejemplo de cómo llamar al minijuego de teclado desde una escena.

# Variable para contar las derrotas consecutivas y ofrecer saltar la pelea.
#default minigame_consecutive_losses = 0

#label chapter1_male_intro:
#    scene bg callejon_oscuro
    # Puedes añadir la imagen de fondo que desees aquí.
    # Por ejemplo: add "images/backgrounds/callejon_oscuro.jpg"

#    "Unos matones me cortan el paso."
#    "Matón" "Oye, tú. Danos todo lo que tengas."

    # --- 1. LLAMADA AL MINIJUEGO ---
    # Usamos 'call' para iniciar la etiqueta 'start_minigame' del otro archivo.
    # Le pasamos el fondo de pantalla que debe usar el minijuego.
    # Puedes ajustar 'target_score' y 'initial_lives' si quieres.
#    call start_minigame(
#        bg_image="images/backgrounds/callejon_oscuro.jpg",
#        target_score=10,
#        initial_lives=3
#    )

    # --- 2. COMPROBACIÓN DEL RESULTADO ---
    # Cuando el minijuego termina (con 'return "win"' o 'return "lose"'),
    # el valor se guarda en la variable especial '_return'.
    # Ahora comprobamos qué valor tiene.
#    if _return == "win":
        
        # --- RAMA DE VICTORIA ---
        # Si el jugador ganó, se ejecuta este bloque.
        
        # Reiniciamos el contador de derrotas, ya que ha ganado.
#        $ minigame_consecutive_losses = 0
        
#        "Consigo defenderme y los matones huyen."
#        "p" "Eso ha sido más fácil de lo que pensaba."
        
        # Saltamos a la continuación normal de la historia.
#        jump continua_la_historia_masculina
        
#    else: # Esto se ejecuta si _return es "lose"
        
        # --- RAMA DE DERROTA ---
        # Si el jugador perdió, se ejecuta este bloque.
        
        # Incrementamos el contador de derrotas consecutivas.
#        $ minigame_consecutive_losses += 1
        
        # Muestra una imagen o describe la derrota.
        # scene cg_derrota_matones
#        "Me dan una paliza y se llevan mi cartera..."
        
        # Ofrecemos un menú para reintentar o saltar la pelea.
        # Si ha perdido varias veces, le damos la opción de saltar.
#        if minigame_consecutive_losses >= 2:
#            menu:
#                "Parece que esta pelea te está costando. ¿Qué quieres hacer?"
#                "Reintentar":
                    # Si quiere reintentar, volvemos al inicio de la escena.
#                    jump chapter1_male_intro
#                "Saltarse la pelea (Continuar historia)":
                    # Si elige saltar, reiniciamos el contador y lo tratamos como una victoria
                    # a efectos de la historia, llevándolo a la continuación.
#                    $ minigame_consecutive_losses = 0
#                    jump continua_la_historia_masculina
#                "Cargar partida":
#                    call screen load
                    # Después de cargar, es buena idea volver al punto de control.
#                    jump chapter1_male_intro
#        else:
#            menu:
#                "¿Quieres intentarlo de nuevo?"
#                "Sí, reintentar":
#                    jump chapter1_male_intro
#                "No, cargar partida":
#                    call screen load
#                    jump chapter1_male_intro

# --- El resto de la historia ---
# El juego llega aquí después de ganar la pelea (o de elegir saltársela).
#label continua_la_historia_masculina:
#    scene bg parque
    # scene bg parque with fade
#    "p" "Después de ese encuentro, decidí que necesitaba despejarme un poco..."
    # ...la historia continúa...
#    return

#------------------------------------------------------------------------------
