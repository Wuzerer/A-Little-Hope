################################################################################
## Inicialización
################################################################################

init offset = -1


################################################################################
## Estilos
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Pantallas internas del juego
################################################################################


## Pantalla de diálogo #########################################################
##
## La pantalla de diálogo muestra el diálogo al jugador. Acepta dos parámetros,
## 'who' y 'what', es decir, el nombre del personaje que habla y el texto que ha
## de ser mostrado respectivamente. (El parámetro 'who' puede ser 'None' si no
## se da ningún nombre.)
##
## Esta pantalla debe crear un texto visualizable con id "what" que Ren'Py usa
## para gestionar la visualización del texto. Puede crear también visualizables
## con id "who" y id "window" para aplicar propiedades de estilo.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Si hay una imagen lateral, la muestra encima del texto. No la muestra en
    ## la variante de teléfono - no hay lugar.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Permite que el 'namebox' pueda ser estilizado en el objeto 'Character'.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    # BORRA o comenta la línea de "xpos"
    # xpos gui.dialogue_xpos

    # AÑADE esta línea en su lugar
    xalign gui.dialogue_text_xalign

    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    # Y asegúrate de que también tiene esta línea para centrar el texto DENTRO del bloque
    text_align 0.5

## Pantalla de introducción de texto ###########################################
##
## Pantalla usada para visualizar 'renpy.input'. El parámetro 'prompt' se usa
## para pasar el texto presentado.
##
## Esta pantalla debe crear un displayable 'input' con id "input" para aceptar
## diversos parámetros de entrada.
##
## https://www.renpy.org/doc/html/screen_special.html#input

################################################################################
# Estilos Personalizados
################################################################################

# --- Estilos del Menú Principal (ya funcionan) ---
style main_menu_image_button:
    xsize 250
    ysize 45
style social_media_image_button:
    xsize 70
    ysize 70

# --- ¡NUEVO! Estilos para la Pantalla de Introducir Nombre ---
style input_prompt_style:
    # Estilo para la pregunta "Por favor, introduce tu nombre:"
    font gui.interface_text_font # Usa la fuente de la interfaz definida en gui.rpy
    size 45
    text_align 0.5 # Centra el texto
    xalign 0.5

style input_text_style:
    # Estilo para el texto que el jugador escribe
    font gui.text_font # Usa la fuente del diálogo normal
    size 40
    text_align 0.5 # Centra el texto
    xalign 0.5


################################################################################
# Pantallas del Juego
################################################################################

# --- Pantalla del Menú Principal (sin cambios) ---
screen main_menu():
    tag menu
    add "mainMenuMovie"
    fixed:
        #add "gui/game_logo.png" xpos 100 ypos 50
        imagebutton idle "gui/start1.png" hover "gui/start2.png" style "main_menu_image_button" pos (10, 300) action Start()
        imagebutton idle "gui/load_1.png" hover "gui/load_2.png" style "main_menu_image_button" pos (10, 360) action ShowMenu("load")
        imagebutton idle "gui/preference_1.png" hover "gui/preference_2.png" style "main_menu_image_button" pos (10, 420) action ShowMenu("preferences")
        imagebutton idle "gui/about_1.png" hover "gui/about_2.png" style "main_menu_image_button" pos (10, 480) action ShowMenu("about")
        imagebutton idle "gui/quit_1.png" hover "gui/quit_2.png" style "main_menu_image_button" pos (10, 540) action Quit(confirm=not main_menu)
        imagebutton idle "gui/discord1.png" style "social_media_image_button" align (0.98, 0.02) action OpenURL("https://discord.gg/tu_servidor")
        imagebutton idle "gui/patreon1.png" style "social_media_image_button" align (0.02, 0.98) action OpenURL("https://www.patreon.com/tu_usuario")


# --- ¡NUEVA VERSIÓN! Pantalla de Introducción de Texto (input) ---
screen input(prompt):
    # La propiedad modal evita que se pueda hacer clic fuera de esta pantalla.
    modal True

    # Añadimos un fondo oscuro semitransparente para enfocar la atención.
    add "#000000" alpha 0.75

    # Usamos un vbox para apilar y centrar la pregunta y la caja de texto.
    vbox:
        # Centramos el vbox en la pantalla.
        align (0.5, 0.5)
        spacing 20 # Espacio entre la pregunta y la caja de texto.

        # La pregunta que se muestra al jugador (ej: "Por favor, introduce tu nombre:")
        text prompt style "input_prompt_style"

        # La caja donde el jugador escribe su nombre.
        input id "input" style "input_text_style"


# --- Pantalla de Diálogo (say) - La dejamos como estaba, funcionando ---
screen say(who, what):
    # ... (Aquí va tu código de la pantalla 'say' que ya funciona bien) ...
    # ... (Es importante dejarla para que los diálogos normales se sigan viendo) ...
    window:
        id "window"
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what"


# ... (Aquí iría el resto de tus pantallas: choice, quick_menu, etc.) ...



## Pantalla de menú ############################################################
##
## Esta pantallla presenta las opciones internas al juego de la sentencia
## 'menu'. El parámetro único, 'items', es una lista de objetos, cada uno los
## campos 'caption' y 'action'.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Pantalla de menú rápido #####################################################
##
## El menú rápido se presenta en el juego para ofrecer fácil acceso a los menus
## externos al juego.

screen quick_menu():

    # Asegura que esté encima de todo
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            # textbutton _("Atrás") action Rollback()
            textbutton _("Saltar") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Historial") action ShowMenu("history")
            textbutton _("Guardar") action ShowMenu("save")
            textbutton _("Cargar") action ShowMenu("load")
            textbutton _("Opciones") action ShowMenu("preferences")
            textbutton _("Menú") action MainMenu()



## Este código asegura que la pantalla 'quick_menu' se muestra en el juego,
## mientras el jugador no haya escondido explícitamente la interfaz.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Principal y Pantalla de menu del juego.
################################################################################

## Pantalla de navegación ######################################################
##
## Esta pantalla está incluída en el menú principal y los menús del juego y
## ofrece navegación a los otros menús y al inicio del juego.

screen navigation():

    # Definimos una variable local 'lang_path' que contiene la ruta a la carpeta
    # del idioma actual. Esto hace el código más limpio.
    # Ej: "gui/buttons/spanish/" o "gui/buttons/english/"
    $ lang_path = "gui/buttons/" + persistent.language + "/"

    vbox:
        xpos 30
        ypos 100
        spacing 15

        if main_menu:
            imagebutton:
                idle (lang_path + "start1.png")
                hover (lang_path + "start2.png")
                action [play_ui_sound("sfx/click_ui.ogg"), Start()]
                hovered play_ui_sound("sfx/hover_ui.ogg")

        else:
            # Botón Historial
            imagebutton:
                idle (lang_path + "history_idle.png")
                hover (lang_path + "history_hover.png")
                action [play_ui_sound("sfx/click_ui.ogg"), ShowMenu("history")]
                hovered play_ui_sound("sfx/hover_ui.ogg")

            # Botón Guardar
            imagebutton:
                idle (lang_path + "save_idle.png")
                hover (lang_path + "save_hover.png")
                action [play_ui_sound("sfx/click_ui.ogg"), ShowMenu("save")]
                hovered play_ui_sound("sfx/hover_ui.ogg")

        # Botón Cargar
        imagebutton:
            idle (lang_path + "load_1.png")
            hover (lang_path + "load_2.png")
            action [play_ui_sound("sfx/click_ui.ogg"), ShowMenu("load")]
            hovered play_ui_sound("sfx/hover_ui.ogg")

        # Botón Preferencias
        imagebutton:
            idle (lang_path + "preference_1.png")
            hover (lang_path + "preference_2.png")
            action [play_ui_sound("sfx/click_ui.ogg"), ShowMenu("preferences")]
            hovered play_ui_sound("sfx/hover_ui.ogg")

        if _in_replay:
            # Botón Repetición
            imagebutton:
                idle (lang_path + "replay_idle.png")
                hover (lang_path + "replay_hover.png")
                action [play_ui_sound("sfx/click_ui.ogg"), EndReplay(confirm=True)]
                hovered play_ui_sound("sfx/hover_ui.ogg")

        elif not main_menu:
            # Botón Menú Principal
            imagebutton:
                idle (lang_path + "mainmenu_idle.png")
                hover (lang_path + "mainmenu_hover.png")
                action [play_ui_sound("sfx/click_ui.ogg"), MainMenu()]
                hovered play_ui_sound("sfx/hover_ui.ogg")

        # Botón Acerca de
        imagebutton:
            idle (lang_path + "about_1.png")
            hover (lang_path + "about_2.png")
            action [play_ui_sound("sfx/click_ui.ogg"), ShowMenu("about")]
            hovered play_ui_sound("sfx/hover_ui.ogg")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            # Botón Ayuda
            imagebutton:
                idle (lang_path + "help_idle.png")
                hover (lang_path + "help_hover.png")
                action [play_ui_sound("sfx/click_ui.ogg"), ShowMenu("help")]
                hovered play_ui_sound("sfx/hover_ui.ogg")

        if renpy.variant("pc"):
            # Botón Salir
            imagebutton:
                idle (lang_path + "quit_1.png")
                hover (lang_path + "quit_2.png")
                action [play_ui_sound("sfx/click_ui.ogg"), Quit(confirm=not main_menu)]
                hovered play_ui_sound("sfx/hover_ui.ogg")
                xpos 1150
                ypos 650


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


################################################################################
# Estilos Personalizados para el Menú Principal
################################################################################

style main_menu_image_button:
    # Define el tamaño exacto para los botones de navegación.
    # ¡Ajusta estos valores si es necesario!
    xsize 250
    ysize 45

style social_media_image_button:
    # Estilo para los botones de redes sociales, si quieres un tamaño diferente.
    xsize 70
    ysize 70


################################################################################
# Pantalla del Menú Principal (main_menu)
################################################################################

################################################################################
## Inicialización
################################################################################

init offset = -1

transform transparent75:
    alpha 0.75

################################################################################
## Pantallas del Juego
################################################################################

init python:
    if persistent.language is None:
        persistent.language = "spanish"

screen language_selector():
    zorder 101

    hbox:
        # Posición cambiada a la parte inferior central
        xpos 1100
        ypos 650
        spacing 10

        imagebutton:
            idle "gui/buttons/language/spanish_idle.png"
            hover "gui/buttons/language/spanish_hover.png"
            action [
                Language("spanish"),
                SetVariable("persistent.language", "spanish"),
                renpy.restart_interaction
            ]
            sensitive (persistent.language != "spanish")

        imagebutton:
            idle "gui/buttons/language/english_idle.png"
            hover "gui/buttons/language/english_hover.png"
            action [
                Language("english"),
                SetVariable("persistent.language", "english"),
                renpy.restart_interaction
            ]
            sensitive (persistent.language != "english")

screen main_menu():
    tag menu

    # 1. Dibuja el fondo PRIMERO para que quede detrás de todo.
    add "images/menu_fondo.png"
    #add "menu_background_video"
    # 2. Dibuja el logo DESPUÉS para que aparezca encima del fondo.
    add "gui/menu_logo.png" pos (250, -50) anchor (0.5, 0.0) zoom 0.5

    # El selector de idioma, que también debe ir encima del fondo.
    use language_selector()

    # Título del juego centrado arriba
    #text "A LITTLE":
    #    style "main_menu_title"
    #    xpos 420 ypos 80 xanchor 0.5

    #text "HOPE":
    #    style "main_menu_title_big"
    #    xpos 850 ypos 80 xanchor 0.5

    fixed:
        imagebutton idle ("gui/buttons/" + persistent.language + "/start1.png") hover ("gui/buttons/" + persistent.language + "/start2.png"):
            style "main_menu_image_button"
            xpos 75
            ypos 550
            action Start()

        imagebutton idle ("gui/buttons/" + persistent.language + "/load_1.png") hover ("gui/buttons/" + persistent.language + "/load_2.png"):
            style "main_menu_image_button"
            xpos 300
            ypos 550
            action ShowMenu("load")

        imagebutton idle ("gui/buttons/" + persistent.language + "/preference_1.png") hover ("gui/buttons/" + persistent.language + "/preference_2.png"):
            style "main_menu_image_button"
            xpos 475
            ypos 550
            action ShowMenu("preferences")

        imagebutton idle ("gui/buttons/" + persistent.language + "/about_1.png") hover ("gui/buttons/" + persistent.language + "/about_2.png"):
            style "main_menu_image_button"
            xpos 695
            ypos 550
            action ShowMenu("about")

        imagebutton idle ("gui/buttons/" + persistent.language + "/gallery_1.png") hover ("gui/buttons/" + persistent.language + "/gallery_2.png"):
            style "main_menu_image_button"
            xpos 875
            ypos 550
            # En lugar de ShowMenu, usamos Show para mostrar nuestra pantalla de notificación.
            action Show('wip_notification')        

        imagebutton idle ("gui/buttons/" + persistent.language + "/quit_1.png") hover ("gui/buttons/" + persistent.language + "/quit_2.png"):
            style "main_menu_image_button"
            xpos 1075
            ypos 550
            action Quit(confirm=not main_menu)

        imagebutton idle "gui/discord1.png":
            style "social_media_image_button"
            xpos 100
            ypos 650
            action OpenURL("[https://discord.gg/tu_servidor](https://discord.gg/tu_servidor)")

        imagebutton idle "gui/patreon1.png":
            style "social_media_image_button"
            xpos 10
            ypos 640
            action OpenURL("[https://www.patreon.com/tu_usuario](https://www.patreon.com/tu_usuario)")

style main_menu_image_button:
    xsize 250
    ysize 45

style social_media_image_button:
    xsize 70
    ysize 70

style main_menu_title_big is main_menu_title

style main_menu_title_big:
    size 120    # Sólo cambias el tamaño; hereda todo lo demás

style main_menu_title:
    font "fonts/perfume-brush-regular.otf"
    size 120
    color "#ffffffff"
    outlines [(2, "#000000", 0, 0)]
    text_align 0.5
    xalign 0.5
    drop_shadow (2, 2)

    #underline True           # activa el subrayado
    # (no existe underline_color: el subrayado toma el mismo color que 'color')

screen say(who, what):
    window:
        id "window"
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what"
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


# ... (puedes seguir pegando las otras pantallas de tu screen.txt aquí si quieres)...



## Pantalla del menú del juego #################################################
##
## Esto distribuye la estructura de base del menú del juego. Es llamado con el
## título de la pantalla y presenta el fondo, el título y la navegación.
##
## El parámetro 'scroll' puede ser 'None', "viewport" o "vpgrid". Se usa esta
## pantalla con uno o más elementos, que son transcluídos (situados) en su
## interior.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Sección lateral: navegación
            frame:
                style "game_menu_navigation_frame"
                has vbox
                use navigation

            ## Sección de contenido principal
            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True

                        vbox:
                            spacing spacing
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        spacing spacing

                        transclude

                else:
                    transclude

    ## Botón volver
    imagebutton:
        idle "gui/btn_volver_idle.png"
        hover "gui/btn_volver_hover.png"
        action [play_ui_sound("sfx/click_ui.ogg"), Return()]
        hovered play_ui_sound("sfx/hover_ui.ogg")
        xpos 30
        ypos 650

    ## Título personalizado — lo puedes mover, cambiar estilo, etc.
    frame:
        style "menu_title_frame"
        xpos 0.5
        xanchor 0.5
        ypos 30
        text title style "menu_title_label"

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style menu_title_frame:
    xfill True
    ysize 100

style menu_title_label:
    xalign 0.5
    yalign 0.5
    text_align 0.5
    color "#ffffff"
    size 50
    outlines [ (2, "#000000", 0, 0) ]
    font "fonts/PerfumeSans-3Bold.otf"  # Cambia por tu archivo de fuente si lo tienes



style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30


## Pantalla 'acerca de' ########################################################
##
## Esta pantalla da información sobre los créditos y el copyright del juego y de
## Ren'Py.
##
## No hay nada especial en esta pantalla y por tanto sirve también como ejemplo
## de cómo hacer una pantalla personalizada.

screen about():

    tag menu

    ## Esta sentencia 'use' incluye la pantalla 'game_menu' dentro de esta. El
    ## elemento 'vbox' se incluye entonces dentro del 'viewport' al interno de
    ## la pantalla 'game_menu'.
    use game_menu(_("Acerca de"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Versión [config.version!t]\n")

            ## 'gui.about' se ajusta habitualmente en 'options.rpy'.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Hecho con {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Pantallas de carga y grabación ##############################################
##
## Estas pantallas permiten al jugador grabar el juego y cargarlo de nuevo. Como
## comparten casi todos los elementos, ambas están implementadas en una tercera
## pantalla: 'file_slots'.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Guardar"))


screen load():

    tag menu

    use file_slots(_("Cargar"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Página {}"), auto=_("Grabación automática"), quick=_("Grabación rápida"))

    use game_menu(title):

        fixed:

            ## Esto asegura que 'input' recibe el evento 'enter' antes que otros
            ## botones.
            order_reverse True

            ## El nombre de la pagina, se puede editar haciendo clic en el
            ## botón.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## La cuadrícula de huecos de guardado.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %d de %B %Y, %H:%M"), empty=_("vacío")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Botones de acceso a otras páginas
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}R") action FilePage("quick")

                    ## range(1, 10) da los números del 1 al 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Subir Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Descargar Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 50
    ypadding 3

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Pantalla de preferencias ####################################################
##
## La pantalla de preferencias permite al jugador configurar el juego a su
## gusto.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

# Limpiar estilos automáticos para que no interfieran
init python:
    style.button.activate_sound = None
    style.image_button.activate_sound = None
    style.main_menu_image_button.activate_sound = None
    style.social_media_image_button.activate_sound = None

# Screen de preferencias extendido con opción de sonido de botones
screen preferences():

    tag menu

    use game_menu(_("Opciones"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc") or renpy.variant("web"):

                    vbox:
                        style_prefix "radio"
                        label _("Pantalla")
                        textbutton _("Ventana") action [play_ui_sound("sfx/click_ui.ogg"), Preference("display", "window")] hovered play_ui_sound("sfx/hover_ui.ogg")
                        textbutton _("Pantalla completa") action [play_ui_sound("sfx/click_ui.ogg"), Preference("display", "fullscreen")] hovered play_ui_sound("sfx/hover_ui.ogg")

                vbox:
                    style_prefix "check"
                    label _("Saltar")
                    textbutton _("Texto no visto") action [play_ui_sound("sfx/click_ui.ogg"), Preference("skip", "toggle")] hovered play_ui_sound("sfx/hover_ui.ogg")
                    textbutton _("Tras elecciones") action [play_ui_sound("sfx/click_ui.ogg"), Preference("after choices", "toggle")] hovered play_ui_sound("sfx/hover_ui.ogg")
                    textbutton _("Transiciones") action [play_ui_sound("sfx/click_ui.ogg"), InvertSelected(Preference("transitions", "toggle"))] hovered play_ui_sound("sfx/hover_ui.ogg")

                vbox:
                    style_prefix "check"
                    label _("Interfaz")
                    textbutton ("Sonido de botones: " + ("Activado" if interfaz_sonido else "Desactivado")):
                        action [play_ui_sound("sfx/click_ui.ogg"), ToggleVariable("interfaz_sonido")]
                        hovered play_ui_sound("sfx/hover_ui.ogg")

            null height (4 * gui.pref_spacing)

            hbox:
                style_prefix "slider"
                box_wrap True

                vbox:
                    label _("Veloc. texto")
                    bar value Preference("text speed")

                    label _("Veloc. autoavance")
                    bar value Preference("auto-forward time")

                vbox:

                    if config.has_music:
                        label _("Volumen música")
                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:
                        label _("Volumen sonido")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Prueba") action [play_ui_sound("sfx/click_ui.ogg"), Play("sound", config.sample_sound)] hovered play_ui_sound("sfx/hover_ui.ogg")


                    if config.has_voice:
                        label _("Volumen voz")
                        hbox:
                            bar value Preference("voice volume")
                            if config.sample_voice:
                                textbutton _("Prueba") action [play_ui_sound("sfx/click_ui.ogg"), Play("sound", config.sample_sound)] hovered play_ui_sound("sfx/hover_ui.ogg")


                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing
                        textbutton _("Silenciar todo"):
                            action [play_ui_sound("sfx/click_ui.ogg"), Preference("all mute", "toggle")]
                            hovered play_ui_sound("sfx/hover_ui.ogg")
                            style "mute_all_button"




style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 450


## Pantalla de historial #######################################################
##
## Esta pantalla presenta el historial de diálogo al jugador, almacenado en
## '_history_list'.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Evita la predicción de esta pantalla, que podría ser demasiado grande.
    predict False

    use game_menu(_("Historial"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Esto distribuye los elementos apropiadamente si
                ## 'history_height' es 'None'.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Toma el color del texto 'who' de 'Character', si ha
                        ## sido establecido.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("El historial está vacío.")


## Esto determina qué etiquetas se permiten en la pantalla de historial.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Pantalla de ayuda ###########################################################
##
## Una pantalla que da información sobre el uso del teclado y el ratón. Usa
## otras pantallas con el contenido de la ayuda ('keyboard_help', 'mouse_help',
## y 'gamepad_help').

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Ayuda"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 15

            hbox:
                textbutton _("Teclado") action [play_ui_sound("sfx/click_ui.ogg"), SetScreenVariable("device", "keyboard")] hovered play_ui_sound("sfx/hover_ui.ogg")
                textbutton _("Ratón") action [play_ui_sound("sfx/click_ui.ogg"), SetScreenVariable("device", "mouse")] hovered play_ui_sound("sfx/hover_ui.ogg")

                if GamepadExists():
                    textbutton _("Mando") action [play_ui_sound("sfx/click_ui.ogg"), SetScreenVariable("device", "gamepad")] hovered play_ui_sound("sfx/hover_ui.ogg")


            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Intro")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Espacio")
        text _("Avanza el diálogo sin seleccionar opciones.")

    hbox:
        label _("Teclas de flecha")
        text _("Navega la interfaz.")

    hbox:
        label _("Escape")
        text _("Accede al menú del juego.")

    hbox:
        label _("Ctrl")
        text _("Salta el diálogo mientras se presiona.")

    hbox:
        label _("Tabulador")
        text _("Activa/desactiva el salto de diálogo.")

    hbox:
        label _("Av. pág.")
        text _("Retrocede al diálogo anterior.")

    hbox:
        label _("Re. pág.")
        text _("Avanza hacia el diálogo siguiente.")

    hbox:
        label "H"
        text _("Oculta la interfaz.")

    hbox:
        label "S"
        text _("Captura la pantalla.")

    hbox:
        label "V"
        text _("Activa/desactiva la asistencia por {a=https://www.renpy.org/l/voicing}voz-automática{/a}.")

    hbox:
        label "Shift+A"
        text _("Abre el menú de accesibilidad.")


screen mouse_help():

    hbox:
        label _("Clic izquierdo")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Clic medio")
        text _("Oculta la interfaz.")

    hbox:
        label _("Clic derecho")
        text _("Accede al menú del juego.")

    hbox:
        label _("Rueda del ratón arriba")
        text _("Retrocede al diálogo anterior.")

    hbox:
        label _("Rueda del ratón abajo")
        text _("Avanza hacia el diálogo siguiente.")


screen gamepad_help():

    hbox:
        label _("Gatillo derecho\nA/Botón inferior")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Gatillo izquierdo\nBotón sup. frontal izq.")
        text _("Retrocede al diálogo anterior.")

    hbox:
        label _("Botón sup. frontal der.")
        text _("Avanza hacia el diálogo siguiente.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navega la interfaz.")

    hbox:
        label _("Inicio, Guía, B/Botón Derecho")
        text _("Accede al menú del juego.")

    hbox:
        label _("Y/Botón superior")
        text _("Oculta la interfaz.")

    textbutton _("Calibrar") action [play_ui_sound("sfx/click_ui.ogg"), GamepadCalibrate()] hovered play_ui_sound("sfx/hover_ui.ogg")


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 8

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 250
    right_padding 20

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Pantallas adicionales
################################################################################


## Pantalla de confirmación ####################################################
##
## Ren'Py llama la pantalla de confirmación para presentar al jugador preguntas
## de sí o no.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

#██▓▒░ PANTALLA DE CONFIRMACIÓN (YES/NO) PERSONALIZADA ░▒▓██
screen yesno_prompt(message, yes_action, no_action):
    modal True

    # Esta acción reproduce un sonido cuando aparece la ventana.
    on "show" action Play("sound", "sfx/alert.wav")

    # 1. Definimos una variable local que construye la ruta a la carpeta del idioma.
    #    Ejemplo: si el idioma es "spanish", la ruta será "gui/spanish/yesno/"
    $ lang_path = "gui/" + persistent.language + "/yesno/"

    imagemap:
        # 2. Usamos la variable 'lang_path' para cargar las imágenes de fondo correctas.
        #    Ren'Py buscará 'ground.png' dentro de 'gui/spanish/yesno/' o 'gui/english/yesno/'.
        ground (lang_path + 'ground.png')
        idle (lang_path + 'idle.png')
        hover (lang_path + 'hover.png')

        # Las coordenadas de los botones no cambian, ya que son relativas a las imágenes de arriba.
        hotspot (334, 461, 289, 90) action yes_action hover_sound "sfx/click.wav"
        hotspot (658, 461, 289, 90) action no_action hover_sound "sfx/click.wav"

    # 3. Hacemos lo mismo para las imágenes que contienen el texto de la pregunta.
    #    Ren'Py buscará 'are_you_sure.png' en la carpeta del idioma correspondiente.
    if message == layout.ARE_YOU_SURE:
        add (lang_path + "are_you_sure.png")
    elif message == layout.DELETE_SAVE:
        add (lang_path + "delete_save.png")
    elif message == layout.OVERWRITE_SAVE:
        add (lang_path + "overwrite_save.png")
    elif message == layout.LOADING:
        add (lang_path + "loading.png")
    elif message == layout.QUIT:
        add (lang_path + "quit.png")
    elif message == layout.MAIN_MENU:
        add (lang_path + "main_menu.png")


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Pantalla del indicador de salto #############################################
##
## La pantalla de indicador de salto se muestra para indicar que se está
## realizando el salto.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Saltando")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Esta transformación provoca el parpadeo de las flechas una tras otra.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Es necesario usar un tipo de letra que contenga el glifo BLACK RIGHT-
    ## POINTING SMALL TRIANGLE.
    font "DejaVuSans.ttf"


## Pantalla de notificación ####################################################
##
## La pantalla de notificación muestra al jugador un mensaje. (Por ejemplo, con
## un guardado rápido o una captura de pantalla.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Pantalla NVL ################################################################
##
## Esta pantalla se usa para el diálogo y los menús en modo NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Presenta el diálogo en una 'vpgrid' o una 'vbox'.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Presenta el menú, si lo hay. El menú puede ser presentado
        ## incorrectamente si 'config.narrator_menu' está ajustado a 'True'.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Esto controla el número máximo de entradas en modo NVL que pueden ser
## mostradas de una vez.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Pantalla de globos ##########################################################
##
## La pantalla de burbujas se utiliza para mostrar el diálogo al jugador cuando
## se utilizan burbujas de diálogo. La pantalla de burbujas toma los mismos
## parámetros que la pantalla "say", debe crear un visualizable con el id de
## "what", y puede crear visualizables con los ids "namebox", "who", y "window".
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Variantes móviles
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Ya que puede carecer de ratón, se reempleza el menú rápido con una versión
## con menos botones y más grandes, más fáciles de tocar.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            # textbutton _("Atrás") action Rollback()
            textbutton _("Saltar") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menú") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 600
