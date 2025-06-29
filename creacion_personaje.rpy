# Archivo: creacion_personaje.rpy

# Define la música de la creacion de personaje en una variable (opcional pero recomendado)
define cp_musica = "audio/cp_music.mp3" # <--- Asegurate de que esta ruta y nombre sean correctos

# Contiene todo el flujo para iniciar una partida y crear al personaje.

# Declaración MANUAL para la imagen de la pantalla de confirmación.
image escena confirmacion = ConditionSwitch(
    "mc_tag == 'mc_m'", "images/gui/seleccion_hover_m.png",
    "mc_tag == 'mc_f'", "images/gui/seleccion_hover_f.png"
)

# El juego empieza aquí y salta a la primera parte de la creación.

# Etiqueta para la selección de género.

label seleccion_genero:
    stop music fadeout 2.0
    play music cp_musica # <--- Empieza a reproducir la música de la creacion de personaje
    scene black
    with fade
    # Llamamos a nuestra nueva pantalla de imagemap.
    call screen pantalla_seleccion_imagemap
    with dissolve
    
    # El juego se pausará aquí. Cuando el jugador haga clic en un hotspot,
    # la acción Jump() nos llevará a la pantalla de confirmación.

# Etiqueta para la pantalla de confirmación.
label pantalla_confirmacion:
    scene escena confirmacion
    with dissolve
    menu:
        "¿Estás seguro de tu elección?"
        "Sí, continuar.":
            jump pedir_nombre
        "No, quiero volver a elegir.":
            jump seleccion_genero

# Etiqueta para pedir el nombre (Versión Mejorada)
label pedir_nombre:
    python:
        # 1. Primero, revisamos la etiqueta de género que ya guardamos.
        if mc_tag == 'mc_m':
            # Si es masculino, el nombre por defecto será "Ren".
            nombre_por_defecto = "Ren"
        else:
            # Si no (es decir, si es femenino), el nombre por defecto será otro.
            # ¡Puedes poner aquí el nombre femenino que más te guste!
            nombre_por_defecto = "Yuna" 

        # 2. Ahora, le pedimos el nombre al jugador.
        mc_name = renpy.input("Por favor, introduce tu nombre:")
        
        # 3. Y si no escribe nada, usamos el nombre por defecto que elegimos arriba.
        mc_name = mc_name.strip() or nombre_por_defecto
    
    # El resto del código sigue igual, salta a la historia.
    jump comienza_la_historia