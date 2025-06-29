# chapter1_female_route.rpy
# Contiene el contenido específico para la ruta femenina del Capítulo 1.

label chapter1_female_intro:
    # 1. Guardamos la otra acción en la memoria.
    $ accion_inicial = "evento_muebles " # Esta variable debe ser 'default' si quieres que persista.
    
    stop music fadeout 2.0
    play music c1_musica3

    # 2. Mostramos la otra escena (la de los muebles).
    scene black
    with dissolve
    "La luz del sol de la mañana atraviesa las cortinas a medio cerrar."
    "El canto de los pájaros apenas se oye por la ventana abierta. La nueva casa huele a polvo, cartón, y algo que intenta ser hogar."
    
    scene evento_muebles 1
    with eye_open_slow_effect
    pensando "mmm..."
    pensando "Que... hora es?..."
    pensando "No... pasara nada si duermo un rato mas..."

    scene black
    with eye_close_slow_effect
    pensando "Pero que estoy diciendo..."

    scene evento_muebles 2
    with eye_open_slow_effect
    pensando "Sera mejor que me despierte..."
    scene evento_muebles 4
    with dissolve
    pause 0.5
    scene evento_muebles 5
    with dissolve
    pause 0.5
    scene evento_muebles 6
    with dissolve
    pensando "Todo esto es nuevo."
    pensando "Todo esto es… raro."
    scene evento_muebles 7
    with dissolve
    "..."
    pensando "Creo que alguien viene"
    "Golpean la puerta de la habitacion"
    e "¿Puedo pasar, [mc_name]?"
    pensando "Emily…"
    p "Si..."
    scene evento_muebles 8
    with dissolve
    e "¿Cómo estás, cielo?"
    scene evento_muebles 9
    with dissolve
    p "No lo sé…"
    p "Supongo que…"
    scene evento_muebles 10
    with dissolve
    p "confundida. Triste."
    scene evento_muebles 11
    with dissolve
    e "Es normal. No estás sola, ¿de acuerdo?"
    scene evento_muebles 12
    with dissolve
    e "Estamos aquí contigo."

    scene bg f_cuarto with dissolve

    show emily normal at left
    with moveinleft
    show ana pijamada1 at right
    with moveinright
    with dissolve
    a "¿Quieres a Teddy?"
    show ana pijamada dando at right
    with dissolve
    a "Siempre me ayuda cuando me siento triste."
    
    menu:
        "¿Agarrar al osito?"
        "Si, agarrar el osito":
            $ tomo_osito = True

        "No agarrar el osito":
            $ tomo_osito = False

    if tomo_osito:
        "Agarro el osito de Ana"
        show ana pijamada normal at right
        with dissolve
        p "gracias ana, es muy hermoso"
        show ana pijamada superfeliz at right
        with dissolve
        show emily feliz at left
        with dissolve
        e "Es muy hermoso ese gesto que hiciste querida"
        a "Gracias mami"
        show ana pijamada normal at right
        with dissolve
        a "Puedes contarle todo..."

    else:
        p "Creo que se sentira mal, si se aleja de ti"
        show ana pijamada tristeosito at right
        with dissolve
        a "Esta bien..."
        show emily preocupada at left
        with dissolve
        e "No te preocupes, querida"
        e "[mc_name] todavia no necesite los consejos de el"
        e "Estara guardando su turno"
        with dissolve
        show ana pijamada1 at right
        with dissolve
        a "Oki"
        pensando "Al menos no quede como una desalmada"


    if tomo_osito:
        $ ana_sprite_base = ANA_SIN_OSITO      # Ana ya NO tiene el osito
        $ escena_base = ESCENA_SIN_OSITO
    else:
        $ ana_sprite_base = ANA_CON_OSITO      # Ana TODAVÍA lo tiene
        $ escena_base = ESCENA_CON_OSITO
    
    show expression ana_sprite_base + "feliz" at right
    with dissolve
    show emily normal at left
    with dissolve
    pensando "No me acostumbro a tener una hermanita tan tierna."
    scene expression escena_base + "1"
    with dissolve
    e "No te preocupes cariño, todo saldra bien"
    e "Se ve que estas pensando mucho en..."
    scene expression escena_base + "2"
    with dissolve
    "Se escuchan otros pasos en el pasillo"
    scene expression escena_base + "3"
    with slow_dissolve
    pensando "Que raro... sin humor otro dia mas."
    scene expression escena_base + "4"
    with slow_dissolve
    m "La comida está lista."

    scene bg f_cuarto with dissolve
    show emily normal at left 
    with moveinleft
    hide expression ana_sprite_base + "feliz" at right
    show expression ana_sprite_base + "normal" at right
    with moveinright
    show mana enojada at center
    with moveinleft
    m "Si bajan tarde, no esperen que sirva dos veces..."
    show emily preocupada at left
    with dissolve
    e "¡Mana, no es momento para eso!"
    m "Pues tal vez *alguien* debería haber pensado eso..."
    m "antes de venir a arruinarnos la rutina."
    pensando "Algo me dice que no le caigo bien."
    hide expression ana_sprite_base + "normal" at right
    show expression ana_sprite_base + "triste" at right
    with dissolve
    m "..."
    show mana enojada at salir_izquierda  # ya estaba mostrada, pero se repite solo para activar la transición
    "Mana desaparece por el pasillo."
    pensando "Definitivamente no le agrado"
    e "Sera mejor que vayamos."
    show emily preocupada at salir_izquierda
    "Emily desaparece por el pasillo"
    show expression ana_sprite_base + "triste2" at right
    with dissolve
    a "Perdon por eso [mc_name]..."
    a "Mana es buena."
    hide expression ana_sprite_base + "triste" at right
    show expression ana_sprite_base + "triste2" at salir_izquierda
    "Ana desaparece por el pasillo"
    pensando "Creo que sera mejor que baje."
    scene black
    with dissolve
    "Me toma unos minutos..."

    stop music fadeout 2.0
    play music c1_musica2

    scene evento_muebles 13
    with dissolve
    pensando "Es tan raro todo esto..."
    scene evento_muebles 14
    with dissolve
    pensando "Una casa nueva. Personas nuevas. Y papá..."
    scene evento_muebles 15
    with dissolve
    pensando "¿Dónde estás, papá? Dijiste que llegarías temprano..."
    pensando "¿De verdad no pudiste venir siquiera a instalarme? ¿O simplemente no quisiste?"
    scene evento_muebles 16
    with dissolve
    "Llego a las escaleras..."
    "Siento un nudo subir desde el estómago. A veces quisiera poder apagar mi cabeza."
    scene evento_muebles 17
    with dissolve
    "Bajo cada peldaño con cautela, como si temiera resbalar..."
    scene evento_muebles 18
    with dissolve
    "...O despertar de una ilusión..."

    # Al final de esta rama específica, saltamos al punto de unión en el archivo principal.
    jump chapter1_common_part_after_intro
    