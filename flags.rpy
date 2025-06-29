# flags.rpy
# Aquí pones TODOS tus default de banderas de decisión, uno por línea.
default tomo_osito = False
# (añade más flags si las necesitas, pero cada una solo aquí)
default si_cuento = False
# (añade más flags si las necesitas, pero cada una solo aquí)
default meterme = False
# (añade más flags si las necesitas, pero cada una solo aquí)


#---------------------------------------------------------------------------------------
#1
# Ejemplo Menu:
#              "¿Quieres tomar el osito?"
#              "Si":
#                  $ tomo_osito = true
#                  jump tomar_osito
#              "No":
#                  $ tomo_osito = false
#                  jump no_tomar_osito

#2 Continuar la historia con las dos decisiones y luego unir a la historia principal;
#
# label tomar_osito:
#      "Tomaste el osito"
#       jumb continuar_historia
#         
# label no_tomar_osito:
#      "Decidiste no tomar el osito"
#      jumb continuar_historia

# label continuar_historia:
        # Aqui sigue la historia en comun para ambas decisiones
#       "Ahora la historia continua"

#3
# Decisiones del jugador tengan un impacto en el futuro. Colocar en la narracion de la historia
# if tomo_osito:
#     "Veo que todavia tienes el osito contigo"
# else:
#     "Parece que no tienes el osito"
#--------------------------------------------------------------------------------------

# Para continuar la historia en cada decision ejecutar un jump y label