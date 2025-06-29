# Archivo: screens_personalizadas.rpy (Versión final con el título añadido)

# PASO 1: AÑADIMOS EL ESTILO PARA EL TÍTULO AQUÍ ARRIBA
style seleccion_titulo_texto:
    # Tamaño de la fuente
    size 45
    # Color del texto (blanco)
    color "#ffffff"
    # Borde para que se lea mejor (borde negro de 3 píxeles)
    outlines [(3, "#000000", 0, 0)]
    
    # Posición en la pantalla
    xalign 0.5  # Centrado horizontalmente
    yalign 0.2  # 20% desde la parte de arriba (puedes ajustar este valor)


# La variable para el hover se queda igual
default hover_tag = None


# La pantalla ahora contiene el texto
screen pantalla_seleccion_imagemap():

    # 1. EL FONDO DINÁMICO (Esto se dibuja primero, como capa base)
    if hover_tag == 'f':
        add "images/gui/seleccion_hover_f.png"
    elif hover_tag == 'm':
        add "images/gui/seleccion_hover_m.png"
    else:
        add "images/gui/seleccion_base.png"

    # 2. EL TEXTO DEL TÍTULO (Se dibuja encima del fondo)
    text "Por favor, elige un género":
        style "seleccion_titulo_texto"

    # 3. EL IMAGEMAP (Se dibuja al final, como la capa superior invisible e interactiva)
    imagemap:
        ground "images/gui/transparente_1280x720.png"
        alpha False
        
        hotspot (0, 0, 640, 720):
            action [SetVariable("mc_tag", "mc_f"), Jump("pantalla_confirmacion")]
            hovered SetVariable("hover_tag", 'f')
            unhovered SetVariable("hover_tag", None)

        hotspot (640, 0, 640, 720):
            action [SetVariable("mc_tag", "mc_m"), Jump("pantalla_confirmacion")]
            hovered SetVariable("hover_tag", 'm')
            unhovered SetVariable("hover_tag", None)
            