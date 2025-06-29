
# Este transform aplica una entrada animada con desvanecimiento y desplazamiento suave
transform boton_entrada(delay=0.0):
    alpha 0.0
    ypos 300
    pause delay
    linear 0.5 alpha 1.0 ypos 300

transform boton_load(delay=0.0):
    alpha 0.0
    ypos 380
    pause delay
    linear 0.5 alpha 1.0 ypos 380

transform boton_preference(delay=0.0):
    alpha 0.0
    ypos 460
    pause delay
    linear 0.5 alpha 1.0 ypos 460

transform boton_about(delay=0.0):
    alpha 0.0
    ypos 540
    pause delay
    linear 0.5 alpha 1.0 ypos 540

transform boton_quit(delay=0.0):
    alpha 0.0
    ypos 650
    pause delay
    linear 0.5 alpha 1.0 ypos 650

transform boton_discord(delay=0.0):
    alpha 0.0
    ypos 0
    pause delay
    linear 0.5 alpha 1.0 ypos 0

transform boton_patreon(delay=0.0):
    alpha 0.0
    ypos 0
    pause delay
    linear 0.5 alpha 1.0 ypos 0

# Ejemplo de uso en un botón del menú principal:
# imagebutton idle "boton_idle.png" hover "boton_hover.png":
#     at boton_entrada(delay=0.2)
#     action Start()

