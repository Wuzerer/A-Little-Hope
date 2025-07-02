# Archivo: intro.rpy

# --- 1. Definimos una variable persistente ---
# Esta variable contará cuántas veces se ha completado la intro.
# 0 = nunca, 1 = una vez, 2 = dos veces, etc.
default persistent.intro_play_count = 0

# --- 2. Código para declarar tus imágenes de la intro (sin cambios) ---
define intro_musica = "audio/intro_music.mp3"
define TOTAL_ESCENAS_INTRO = 100

init python:
    for i in range(1, TOTAL_ESCENAS_INTRO + 1):
        tag_imagen = "intro " + str(i)
        ruta_imagen = "images/intro/intro_{}.png".format(i)
        renpy.image(tag_imagen, ruta_imagen)
    
    for i in range(1, TOTAL_ESCENAS_INTRO + 1):
        tag2_imagen = "intro2 " + str(i)
        ruta2_imagen = "images/intro/intro2/intro2_{}.png".format(i)
        renpy.image(tag2_imagen, ruta2_imagen)

    # Añadimos la declaración para las imágenes de la tercera intro.
    # ¡Recuerda crear estas imágenes en "game/images/intro/intro3/"!
    for i in range(1, 10):
        tag3_imagen = "intro3 " + str(i)
        ruta3_imagen = "images/intro/intro3/intro3_{}.png".format(i)
        renpy.image(tag3_imagen, ruta3_imagen)

    # Declaración para las imágenes de la cuarta intro.
    # ¡Recuerda crear estas imágenes en "game/images/intro/intro4/"!
    for i in range(1, 10):
        tag4_imagen = "intro4 " + str(i)
        ruta4_imagen = "images/intro/intro4/intro4_{}.png".format(i)
        renpy.image(tag4_imagen, ruta4_imagen)

    # Declaración para las imágenes de la quinta intro (y siguientes).
    for i in range(1, 10):
        tag5_imagen = "intro5 " + str(i)
        ruta5_imagen = "images/intro/intro5/intro5_{}.png".format(i)
        renpy.image(tag5_imagen, ruta5_imagen)


# --- 3. El inicio del juego, ahora con un "detector" de partidas ---
label start:

    stop music fadeout 2.0
    play music intro_musica

    # ¡AQUÍ ESTÁ LA MAGIA!
    # Comprobamos cuántas veces ha visto el jugador la intro.

    if persistent.intro_play_count == 1:

        # --- INTRO PARA LA SEGUNDA VEZ ---
        # Si ya la ha visto una vez, le mostramos un mensaje rápido y diferente.
        scene black
        with dissolve

        # El personaje que habla en la intro te regaña por querer verla de nuevo.
        scene intro2 1
        with dissolve
        pause 1.0
        scene intro2 2
        with dissolve
        pause 1.0
        scene intro2 3
        with dissolve
        "¿Mmm...?"
        scene intro2 4
        with dissolve
        "Ah, mira quién volvió."
        scene intro2 5 at bg_zoom
        with dissolve
        "Directo al grano, ¿eh? Me gusta tu estilo."
        "Aunque pensé que ya te sabías la historia de memoria."
        "No es que me moleste, ¿eh? Es solo que..."
        scene intro2 6
        with dissolve
        "Mi transporte ya viene. En serio, tengo... una vida, ¿sabes?"
        "Citas, dramas, ¡cosas de personaje de relleno!"
        scene intro2 7
        with dissolve
        "Por lo tanto... te dejo."
        "Que disfrutes de esta 'segunda vez'. O tercera, o cuarta..."
        "Ya sabes cómo va, ¿verdad? ¡Nos vemos!"
        scene intro2 2
        with dissolve
        pause 1.0
        scene intro2 1
        with dissolve
        pause 1.0

        # ¡IMPORTANTE! Incrementamos el contador para la próxima vez.
        $ persistent.intro_play_count += 1

        # Y lo saltamos directamente a la selección de género.
        jump seleccion_genero

    elif persistent.intro_play_count == 2:

        # --- INTRO PARA LA TERCERA VEZ ---
        scene black
        with dissolve

        scene intro3 1
        with dissolve
        pause 0.5
        
        scene intro3 2
        with dissolve
        "¿Otra vez por aquí? Ya eres como de la familia."
        scene intro3 3
        with dissolve
        "Me caes bien. Te voy a contar un secreto..."
        scene intro3 4
        with dissolve
        "O eso te dije la última vez... ¡Te engañé!"
        scene intro3 1
        with dissolve
        "¡Aprecio tu dedicación! Venga, al lío."
        pause 2.0

        # Incrementamos para que la próxima vez sea la cuarta.
        $ persistent.intro_play_count += 1
        jump seleccion_genero

    elif persistent.intro_play_count == 3:

        # --- INTRO PARA LA CUARTA VEZ ---
        scene black
        with dissolve

        # ¡Recuerda crear las imágenes en "game/images/intro/intro4/"!
        scene intro4 1
        with dissolve
        pause 0.5

        scene intro4 2
        with dissolve
        "Vale, esto ya es personal."
        scene intro4 3
        with dissolve
        "¿Estás buscando algún easter egg? ¿Un código secreto?"
        scene intro4 4
        with dissolve
        "No sé... ¿El teléfono de la desarrolladora?"
        scene intro4 5
        with dissolve
        "Te aseguro que no hay nada de eso. Pero tu persistencia es admirable."
        scene intro4 6
        with dissolve
        "Disfruta del juego, ¡otra vez!"
        scene intro4 1
        with dissolve
        pause 2.0

        # Incrementamos para que la próxima vez sea la quinta.
        $ persistent.intro_play_count += 1
        jump seleccion_genero

    elif persistent.intro_play_count >= 4:

        # --- INTRO PARA LA QUINTA VEZ (Y SIGUIENTES) ---
        scene black
        with dissolve

        # ¡Recuerda crear las imágenes en "game/images/intro/intro5/"!
        scene intro5 1
        with dissolve
        "..."
        "Sin palabras. Has ganado. Eres el fan número uno."
        "Ya no hay más intros. Esta es la definitiva. Lo juro."
        "Ahora, por favor, ¡a jugar!"
        pause 2.0

        # No incrementamos más el contador, siempre verá esta intro a partir de ahora.

        # Y lo saltamos directamente a la selección de género.
        jump seleccion_genero


    # --- INTRO COMPLETA (SOLO PARA LA PRIMERA VEZ) ---
    # Si 'persistent.intro_play_count' es 0, el código de arriba se ignora
    # y el juego ejecuta esta secuencia completa.

    scene black
    with dissolve

    scene intro 1
    with dissolve
    pause 1
    scene intro 2
    with dissolve
    "…¿Hola? ¿Funciona esto?..."
    scene intro 3
    with dissolve
    "¿Ya cargó? ¿Sí? ¿No?"
    scene intro 4
    with dissolve
    pause 1
    scene intro 5
    with dissolve
    pause 1
    scene intro 6
    with dissolve
    pause 1
    scene intro 7
    with dissolve
    pause 1
    scene intro 8
    with dissolve
    pause 1
    scene intro 9
    with dissolve
    pause 1
    scene intro 10
    with dissolve
    "(Suspiro)"
    scene intro 11
    with dissolve
    "Bueno… parece que sí."
    scene intro 12
    with dissolve
    scene intro 13
    with dissolve
    pause 1
    scene intro 14
    with dissolve
    pause 1
    scene intro 15
    with dissolve
    "Si estas observando esto, lo siento..."
    scene intro 16
    with dissolve
    "Sí, lo sé, la otra versión quedó colgada."
    "Pero tranqui, no estás solo. ¡Yo también me sentí abandonado!"
    scene intro 19
    with dissolve
    "Literalmente… estaba atrapado en esta pantalla por meses."
    scene intro 18
    with dissolve
    "Pero bueno, ¡no estamos aquí para llorar sobre píxeles derramados!"
    scene intro 17
    with dissolve
    "¡ESTA es la nueva versión!"
    scene intro 21
    with dissolve
    "Más historia. Más drama. Más... presupuesto ficticio."
    scene intro 19
    with dissolve
    pause 1
    scene intro 28
    with dissolve
    "Vamos a ver... ¿Qué trae esta versión?"
    scene intro 29
    with dissolve
    "Diálogos más afilados..."
    scene intro 30
    with dissolve
    "Un botón de *Saltar texto* que igual nadie usará..."
    "Probaran nuevos scripts..."
    "¿Y por qué no? ¡Un poco de romance también!"
    scene intro 31
    pause 1
    with dissolve
    scene intro 23
    with dissolve
    "Pero, seamos honestos…"
    scene intro 21
    with dissolve
    "Estoy aquí para darte una experiencia increíble."
    scene intro 22
    with dissolve
    "Y para eso, tengo que hacer algo importante…"
    scene intro 32
    with dissolve
    pause 1
    scene intro 33
    with dissolve
    pause 1
    scene intro 34
    with dissolve
    "Perdón... De verdad..."
    "Quizas hubo algunas personas que conoceran mi otra version…"
    "No se preocupen, la guardamos en el fondo del cajón de los recuerdos."
    scene intro 22
    with dissolve
    "(También conocido como carpeta *proyectos inconclusos*)"
    scene intro 20
    with dissolve
    "Pero esta vez…"
    "Vengo con todo. Con toda la energía, ideas y café necesarios."
    scene intro 15
    with dissolve
    "¡Y tú, sí tú! Vas a ser parte de esto."
    "Así que ajusta el volumen y relájate."
    scene intro 35
    with dissolve
    "Porque esta historia apenas comienza…"
    "Y créeme:"
    "Va. A. Valer. La. Pena."
    scene intro 24
    with dissolve
    "¿Listo?"
    "Pues acompáñame."
    scene intro 25
    with dissolve
    "Hay decisiones que tomar, y más de un plot twist."
    scene intro 26
    with dissolve
    "Y no olvides guardar tu progreso…"
    scene intro 27
    with dissolve
    "Que no pienso volver a repetir todo esto, ¿ok?"

    # ¡LA PARTE CLAVE!
    # Después de que el jugador vea la intro completa por primera vez,
    # incrementamos el contador. Ahora valdrá 1.
    $ persistent.intro_play_count += 1

    stop music fadeout 2.0
    scene black
    with fade
    pause 0.5

    scene intro 36
    with dissolve
    "Espera…"
    "¿Ya vas a empezar así nomás?"
    scene intro 38
    with dissolve
    pause 1
    scene intro 37
    "Necesito que me ayudes con esto…"
    "¿Que eres realmente…?"
    scene black
    with fade
    pause 1

    # Finalmente, después de la intro, saltamos a la selección de género.
    jump seleccion_genero
