# Este archivo contiene todas las definiciones de personajes.

default mc_name = "Protagonista" # mc_name también debería estar en un archivo de variables o en default
default mc_tag = ""              # mc_tag también.

define p = Character("[mc_name]", dynamic=True)
define e = Character("Emily", color="#E8A8B7") # Un color rosa, por ejemplo
define m = Character("Mana", color="#703543") 
define a = Character("Ana", color="#3183c7") 
# ... otros personajes que tengas ...