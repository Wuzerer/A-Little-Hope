# chapter1_male_route.rpy
# Contiene el contenido específico para la ruta masculina del Capítulo 1.

label chapter1_male_intro:
    # 1. Guardamos en la memoria la acción que está realizando.
    $ accion_inicial = "evento_cajas " # Esta variable debe ser 'default' si quieres que persista.
    # (Se puede definir en variables.rpy: default accion_inicial = None)

    stop music fadeout 2.0
    play music c1_musica3    

    # 2. Mostramos la escena correspondiente (la de las cajas).
    scene black
    with dissolve

    scene evento_muebles 1
    with eye_open_slow_effect
    "Bostezo y me estiro en la cama."
    scene evento_muebles 2
    with dissolve
    "El colchón cruje."
    "Al menos es más cómodo que el camión de mudanza."
    scene evento_muebles 3
    with dissolve
    pensando "Escucho ruidos abajo."
    pensando "¿Dónde estará papá...?"
    scene evento_muebles 4
    with dissolve
    pensando "Bah, debe estar ocupado. No me voy a amargar por eso."
    pensando "Finalmente... una nueva vida. Espero que no sea tan aburrida como la anterior."

    "Sin querer, me acomodo de lado y... me quedo dormido."
    scene black
    with eye_close_slow_effect
    "Unos minutos después... golpecitos en la puerta."

    e "Alex, cariño... ¿te dormiste otra vez?"
    scene evento_muebles 1
    with eye_open_slow_effect
    p "¿Hmm...?"
    p "Oh... sí. Perdón."
    e "Es casi mediodía, la comida está lista."
    "Me reincorporo, rascándome la cabeza."
    scene evento_muebles 5
    with dissolve
    pause 0.5
    scene evento_muebles 6
    with dissolve
    a "¡Hola hermano!"
    "Una cabecita asoma por detrás de Emily. Ana me observa con ojos brillantes."

    scene m_cuarto
    with dissolve
    show ana pijama normal at right
    with moveinleft
    show emily normal at left
    with moveinleft
    a "¡Nunca tuve un hermano antes!"
    show ana pijamada superfeliz at right
    with dissolve
    a "¿Te gustan los trenes? ¿Y los dragones?"
    a "¡Tengo libros de dragones!"
    show ana pijama normal at right
    with dissolve
    pensando "(...Vaya, energía matutina nivel 100.)"

    menu:
        "Si, me gustan mucho":
            $ si_cuento = True

        "No me gustan mucho":
            $ si_cuento =False

    if si_cuento:
        p "Eh... sí, suena interesante."
        show ana pijamada superfeliz at right
        with dissolve
        a "¡Genial! ¡Hoy te leeré uno!"
        a "¡Tengo uno que tiene muchos dibujos de dragones!"
        show emily feliz
        with dissolve
        e "Tranquila cariño, vas a sofocar a [mc_name]"

    else:
        p "Perdon Ana, pero no me gustan mucho que digamos."
        show ana pijama triste at right
        with dissolve
        a "oh..."
        a "Lo entiendo..."
        pensando "Creo que quedo como un desalmado con ella"
        pensando "Pero no me gusta mentir..."
        show emily preocupada at left
        with dissolve
        e "Cariño, quizas en algun momento le podras contar."
        a "Esta bien..."

    scene evento_muebles 7
    with dissolve
    e "Se que todo esto es nuevo para ti [mc_name]"
    a "¡Yo te mostrare la ciudad!"

    "Se escuchan pasos en el pasillo."

    scene evento_muebles 8
    with dissolve
    "Mana aparece de golpe."
    m "Bajen."

    scene m_cuarto
    with dissolve
    if si_cuento:
        show ana pijamada superfeliz at right
        with dissolve
        show emily normal at left
        with dissolve
    else:
        show ana pijama triste at right
        with dissolve
        show emily normal at left
        with dissolve
    
    show mana enojada at center
    with moveinleft
    m "No me pagan para ser niñera, y no pienso recalentar nada."
    show ana pijama normal at right
    with dissolve
    show emily preocupada at left
    with dissolve
    e "Mana, por favor..."
    m "Ya hablé. Apúrense."
    show mana enojada at salir_izquierda
    "Mana se va, rodando los ojos."
    pensando "(Bueno... esto va a ser interesante.)"
    e "Sera mejor que vayamos."
    show emily preocupada at salir_izquierda
    "Emily desaparece por el pasillo"
    show ana pijama sad at right
    with dissolve
    a "Perdon por eso [mc_name]..."
    a "Mana es buena."
    a "..."
    show ana pijama normal at salir_izquierda
    "Ana desaparece por el pasillo"
    pensando "Creo que sera mejor que baje."
    scene black
    with dissolve
    "Me toma unos minutos arreglarme para bajar"

    stop music fadeout 2.0
    play music c1_musica2

    scene evento_muebles 9
    with dissolve
    pensando "Bueno... esto se siente diferente. Pero no necesariamente mal."
    scene evento_muebles 10
    with dissolve
    pensando "Papá otra vez desaparecido... qué raro. Aunque no es que sea sorpresa."
    scene evento_muebles 11
    with dissolve
    pensando "Mientras no me jodan, puedo adaptarme."
    "Bajo por las escaleras, con las manos en los bolsillos. Hay un leve olor a comida en el aire. Algo con especias... tal vez pasta."
    scene evento_muebles 12
    with dissolve
    pensando "Emily parece bien. Ana es simpática... y Mana..."
    pensando "Bueno, Mana no me soporta. Clásico drama familiar."
    scene evento_muebles 13
    with dissolve
    pensando "A ver si esto es tan aburrido como suena, o termina poniéndose interesante."

    # Al final de esta rama específica, saltamos al punto de unión en el archivo principal.
    jump chapter1_common_part_after_intro