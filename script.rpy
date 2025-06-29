# Archivo: script.rpy (La versión final y limpia)

# ... (parte superior del archivo) ...

# Archivo: script.rpy (La versión final y limpia)

# Declara el video del menú como una imagen reproducible.
# El nombre "mainMenuMovie" es el que tu juego antiguo buscaba.
image menu_background_video = Movie(play="videos/menu_loop.webm", loop=True)
#image mainMenuMovie = Movie(play="videos/menu_loop.webm", loop=True)
# ...

################################################################################
# Sección 1: Configuración y Creación Automática de Imágenes
################################################################################

define TOTAL_ESCENAS = 500 # Esto es una variable global, no usada directamente en los bucles de imágenes.
#
define TOTAL_ESCENAS_NEUTRALES = 100

init python:
    # --- Para las escenas generales de la historia (ESTO ESTÁ BIEN) ---
    TOTAL_ESCENAS_GENERALES = 500 # Por ejemplo, si tienes hasta 'escena 5'
    for i in range(1, TOTAL_ESCENAS_GENERALES + 1):
        tag_imagen = "escena " + str(i)
        ruta_m = "images/story/mc_m_{}.png".format(i)
        ruta_f = "images/story/mc_f_{}.png".format(i)
        renpy.image(tag_imagen, ConditionSwitch(
            "mc_tag == 'mc_m'", ruta_m,
            "mc_tag == 'mc_f'", ruta_f
        ))

        # --- Motor 2: ¡NUEVO! Para las escenas neutrales (CGs) ---
    for i in range(1, TOTAL_ESCENAS_NEUTRALES + 1):
        # La etiqueta ahora será "cg" para diferenciarla.
        tag_imagen = "cg_cocina " + str(i)
        # La ruta apunta a la nueva carpeta y al nuevo formato de nombre.
        ruta_imagen = "images/story/cap1/cg_cocina_{}.png".format(i)
        
        renpy.image(tag_imagen, ruta_imagen)
    # --- CAMBIO AQUÍ: Para la SERIE de imágenes del EVENTOS ---
    # Si "evento_cajas" tiene múltiples imágenes (ej. _1, _2, _3)
    TOTAL_EVENTO_CAJAS_IMAGENES = 500 # <--- ¡AJUSTA ESTO AL NÚMERO TOTAL DE IMÁGENES EN LA SECUENCIA DE CAJAS!
    for i in range(1, TOTAL_EVENTO_CAJAS_IMAGENES + 1):
        tag_imagen_cajas = "evento_cajas " + str(i) # Tag será "evento_cajas 1", "evento_cajas 2", etc.
        ruta_m_cajas = "images/events_male/mc_m_cajas_evento_{}.png".format(i)
        ruta_f_cajas = "images/events_female/mc_f_cajas_evento_{}.png".format(i) # Aunque no se use, debe estar definido
        renpy.image(tag_imagen_cajas, ConditionSwitch(
            "mc_tag == 'mc_m'", ruta_m_cajas,
            "mc_tag == 'mc_f'", ruta_f_cajas
        ))

    # --- CAMBIO AQUÍ: Para la SERIE de imágenes del EVENTO "MUEBLES" ---
    # Si "evento_muebles" tiene múltiples imágenes (ej. _1, _2, _3)
    TOTAL_EVENTO_MUEBLES_IMAGENES = 500 # <--- ¡AJUSTA ESTO AL NÚMERO TOTAL DE IMÁGENES EN LA SECUENCIA DE MUEBLES!
    for i in range(1, TOTAL_EVENTO_MUEBLES_IMAGENES + 1):
        tag_imagen_muebles = "evento_muebles " + str(i) # Tag será "evento_muebles 1", "evento_muebles 2", etc.
        ruta_m_muebles = "images/events_male/mc_m_muebles_evento_{}.png".format(i) # Aunque no se use, debe estar definido
        ruta_f_muebles = "images/events_female/mc_f_muebles_evento_{}.png".format(i)
        renpy.image(tag_imagen_muebles, ConditionSwitch(
            "mc_tag == 'mc_m'", ruta_m_muebles,
            "mc_tag == 'mc_f'", ruta_f_muebles
        ))
    
    # ... (Añade más bucles para otros eventos si tienen series de imágenes) ...

################################################################################
# Sección 2: Variables y Personajes
################################################################################

# ... (resto de tu script) ...

define slow_dissolve = Dissolve(1.0)
define flash = Fade(0.1, 0.1, 0.1, color="#ffffff")

#-----
screen wip_notification():
    # El "modal True" evita que el jugador pueda hacer clic en otros botones
    # mientras el aviso está en pantalla.
    modal True

    # Un frame para contener el texto y el botón.
    # Puedes darle un estilo que ya tengas definido.
    frame:
        style "main_menu_frame"
        xalign 0.5
        yalign 0.5
        padding (40, 40) # Espaciado interno

        # Un vbox para apilar el texto y el botón verticalmente.
        vbox:
            spacing 20 # Espacio entre el texto y el botón
            xalign 0.5

            text "Esta función estará disponible en las próximas actualizaciones." xalign 0.5
            textbutton "Aceptar" action Hide('wip_notification') xalign 0.5

#------------------------------------------------------------------------------------------

# En tu archivo de historia...

# 1. Muestras la escena como siempre.
# Tu sistema automático se encarga de mostrar la imagen correcta (mc_m_5.png o mc_f_5.png).
#scene escena 5
#with dissolve

# 2. Ahora, compruebas el género para el diálogo.
#if mc_tag == 'mc_m':

    # --- Diálogos para el Personaje Masculino ---
    # Este bloque SÓLO se ejecuta si el jugador eligió ser hombre.
#    p "Vaya... este lugar me da mala espina."
#    pensando "No debería entrar solo, pero la curiosidad me puede."
#    p "Será mejor que sea cauteloso."

#else: # Si la condición de arriba no se cumple, entonces es la personaje femenina.

    # --- Diálogos para el Personaje Femenino ---
    # Este bloque SÓLO se ejecuta si el jugador eligió ser mujer.
#    p "Qué lugar tan fascinante..."
#    pensando "Siento una extraña energía aquí dentro. Tengo que ver qué es."
#    p "No hay tiempo que perder."


# 3. La historia se vuelve a unir aquí.
# Este diálogo se muestra para AMBOS géneros, después de sus pensamientos.
#"Con decisión, das el primer paso hacia la oscuridad de la cueva."

# La historia continúa...
#------------------------------------------------------------------------------------------------
init:
    transform bg_zoom:
        # Escala la imagen hasta que su ancho sea igual al de la pantalla (1280px)
        # y el alto se ajuste automáticamente para mantener la proporción.
        xsize 1280
        ysize 720
        # Alternativamente, puedes usar 'ysize 720' si prefieres que el alto sea la referencia.
        # O para asegurarte de que la imagen llene toda la pantalla sin espacios vacíos
        # (recortando lo que sobre), puedes usar:
        # size (1280, 720)

    # Muestra tu imagen de alta resolución usando la transformación 'bg_zoom'
    #scene tu_imagen_de_fondo at bg_zoom

    # También puedes usarlo con 'show' si no quieres limpiar la pantalla
    #show otra_imagen at bg_zoom