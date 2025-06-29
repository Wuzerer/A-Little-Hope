# Archivo: capitulo1.rpy

# Define la música del capitulo 1 en una variable (opcional pero recomendado)
define c1_musica = "audio/c1_music.mp3" # <--- Asegurate de que esta ruta y nombre sean correctos
#
define c1_musica2 = "audio/c1_music2.mp3"
#
define c1_musica3 = "audio/c1_music3.mp3"
################################################################################
# Sección 4: La Historia Principal
################################################################################

# Ren'Py encontrará esta etiqueta después del "jump" en tu archivo de creación de personaje.
# script_chapter1.rpy

label comienza_la_historia:
    stop music fadeout 2.0
    play music c1_musica # Asegúrate de que c1_musica esté definida.

    # Usamos un "if" para dividir la historia en dos ramas.
    if mc_tag == 'mc_m':
        # Salta a la etiqueta de la rama masculina en otro archivo.
        jump chapter1_male_intro
    else:
        # Salta a la etiqueta de la rama femenina en otro archivo.
        jump chapter1_female_intro

# === Puntos de Unión de las Ramas ===

# Esta etiqueta es el punto donde ambas ramas (masculina y femenina) se unen.
label chapter1_common_part_after_intro:
    
    stop music fadeout 2.0
    play musicc c1_musica

    scene black
    with dissolve

    scene cg_cocina 1
    with dissolve
    "El olor a comida caliente me golpea apenas entro en la cocina."
    "Es acogedor, pero no lo suficiente como para hacer desaparecer la incomodidad."

    scene cg_cocina 2
    with dissolve
    if mc_tag == 'mc_f':
        e "Ahí estás, [mc_name]."
        e "Justo a tiempo, serví tu plato favorito..."
        e "o bueno, eso creo. No estaba segura."
    else:
        e "[mc_name], justo a tiempo."
        e "Espero que tengas hambre, hice lasaña con verduras."    

    scene cg_cocina 3
    with dissolve
    if mc_tag == 'mc_f':
        a "¡Ven, siéntate aquí!"
        a "¡Te guardamos el lugar!"
    else:
        a "¡Está riquísima!"
        a "Aunque creo que exageró con la zanahoria..."

    scene cg_cocina 4
    with dissolve
    if mc_tag == 'mc_f':
        m "(murmurando) Ah, la invitada de honor llega por fin..."
        pensando "¿Siempre será así?"
    else:
        m "¿Se supone que esto es una cena familiar..."
        m "...o un episodio piloto de un programa barato?"
        pensando "Creo que esto sera divertido"

    scene escena 1
    with dissolve
    pensando "Quizás debería ayudar..."
    scene escena 2
    a "Sé que estás pensando [mc_name]"
    a "A mamá no le gusta que toquemos la cocina cuando está ella."
    scene cg_cocina 5
    with dissolve
    a "Dice que solo haríamos desastre y ella se estresa más."
    scene cg_cocina 6
    with dissolve
    if mc_tag == 'mc_f':
        m "Lo único molesto aquí eres tú y la nueva invitada."
    else:
        m "Lo único molesto aquí eres tú y el nuevo invitado."
    e "Mana!"
    scene cg_cocina 7
    with dissolve
    m "(Murmurando) Si es verdad..."
    pensando "Definitivamente no le agrado..."
    scene cg_cocina 8
    with dissolve
    a "Tu eres la única molesta y gruñona..."
    scene cg_cocina 9
    with dissolve 
    pause 
    scene cg_cocina 10
    with dissolve
    m "Que madura eres, Ana."
    
    menu:
        pensando "¿Debería meterme?"
        "Creo que debería meterme":
            $ meterme = True

        "Creo que será mejor que no":
            $ meterme = False

    if meterme:
        pensando "Será que si."
        scene escena 3
        with dissolve
        if mc_tag == 'mc_f':
            p "Chicas, creo que sería mejor no estar peleando al menos tan temprano."
            scene escena 4
            with dissolve
            m "Mira quien decidió entrar en la conversación ajena."
        else:
            p "Que lindo que estés peleando con alguien más pequeña que tú, hermana."
            scene escena 4
            with dissolve
            m "Y tú quien te crees para burlarte."
            p "Creo que es obvio que ahora pertenezco a la familia, ¿no?"

    else:
        scene cg_cocina 11
        with dissolve
        pensando "Será mejor que me mantenga al margen."
        e "Chicas!"
        e "Ya basta de pelear, al menos háganlo después de comer algo."
        
    
    


        


    
    



    # ... más historia ...
    return # O jump a otro capítulo, etc.