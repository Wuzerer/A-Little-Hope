# --- Variables de Relaciones ---

# Empezamos todas las relaciones en 0.
default emily_affection = 0
default ana_affection = 0
default mana_affection = 0
# ...añade una línea para cada personaje romanceable...

#---------------------------------------------------------------------------------------

# Dentro de una label en tu historia...

#label escena_con_lila:

#    lila "¡Hice estas galletas! ¿Quieres una?"
    
#    menu:
#        "¡Claro! Se ven deliciosas.":
            
            # Opción correcta: suma 1 punto de afecto a Lila.
#            $ lila_affection += 1
            
#            p "¡Me encantaría! Muchas gracias, Lila."
#            lila "¡De nada! Espero que te guste."

#        "No, gracias. No tengo hambre.":
            
            # Opción neutral: no cambia los puntos. No ponemos nada.
#            p "Ahora no, pero gracias."
#            lila "Oh... está bien."

#        "No me gustan las galletas con pasas.":
            
            # Opción incorrecta: resta 1 punto.
#            $ lila_affection -= 1
            
#            p "Lo siento, no soy muy fan de las pasas."
#            lila "...Ah. Ya veo."

# La historia continúa...

#---------------------------------------------------------------------------------------

# "punto de control" más adelante en el juego...

#label checkpoint_romance_lila:
    
#    p "(Me encuentro con Lila en el parque. Parece que quiere decirme algo)."

# Comprobamos si tenemos suficientes puntos de afecto.
# Por ejemplo, si se necesitan 3 puntos para la escena romántica.
#    if lila_affection >= 3:
        
# Si tienes 3 o más puntos, el juego te envía a la escena especial.
#        jump escena_romantica_lila
        
#    else:
        
# Si no, te envía a la escena de amistad normal.
#        jump escena_amistad_lila

# --- Las Ramas de la Historia ---

#label escena_romantica_lila:

#    scene cg_romance_lila # Muestras un CG especial
#    with dissolve
    
#    lila "[mc_name]... hay algo que he querido decirte durante mucho tiempo."
#    p "..."
# La historia de romance continúa...
#    return

#label escena_amistad_lila:

# No hay CG, es una escena normal
#    show lila feliz at center
    
#    lila "¡Hola, [mc_name]! ¡Qué buen día para pasear!"
#    p "¡Hola, Lila! Sí, está genial."
# La historia de amistad continúa...
#    return

#---------------------------------------------------------------------------------------

#Consejo Extra: Notificaciones para el Jugador
#Para que el jugador sepa que sus decisiones importan, puedes añadir una pequeña notificación visual o sonora cuando sus puntos de afecto suban.

#menu:
#    "¡Claro! Se ven deliciosas.":
        
#        $ lila_affection += 1
# Añades un sonido y un texto que aparece y desaparece
#        play sound "audio/efecto_positivo.ogg"
#        show screen notify("A Lila le ha gustado eso.")
        
#        p "¡Me encantaría! Muchas gracias, Lila."