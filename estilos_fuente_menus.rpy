# Estilos personalizados solo para los textos dentro de los menús
# Asegúrate de tener las fuentes en game/fonts/

# Cambiar texto general dentro de los menús (como "Veloc. texto", "Acerca de", etc.)
style pref_label_text:
    font "fonts/PerfumeSans-3Bold.otf"
    size 28
    color "#ffffff"
    outlines [(1, "#000000", 0, 0)]

# Cambiar texto de botones tipo "Silenciar todo", "Prueba", etc.
style slider_button_text:
    font "fonts/PerfumeSans-3Bold.otf"
    size 24
    color "#ffffff"
    outlines [(1, "#000000", 0, 0)]

# Texto explicativo en pantalla "Acerca de"
style help_text:
    font "fonts/PerfumeSans-3Bold.otf"
    size 24
    color "#dddddd"

# Texto de encabezados como "Pantalla", "Saltar", etc.
style radio_label_text:
    font "fonts/PerfumeSans-3Bold.otf"
    size 26
    color "#ff4444"

style check_label_text:
    font "fonts/PerfumeSans-3Bold.otf"
    size 26
    color "#ff4444"

# Opcional: cambiar la fuente del número de página en pantalla de cargar/guardar
style page_label_text:
    font "fonts/PerfumeSans-3Bold.otf"
    size 26
    color "#ff4444"
    outlines [(1, "#000000", 0, 0)]
    xalign 0.5