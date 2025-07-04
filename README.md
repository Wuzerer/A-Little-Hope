🎮 Game Design Doc: A Little Hope
🚀 Visión General
Elevator Pitch: "A Little Hope" es una novela visual dramática y emotiva donde te pones en la piel de un joven que debe adaptarse a una nueva vida con su nueva familia. Cada decisión, desde las conversaciones más triviales hasta los conflictos más intensos, moldea tus relaciones y define tu camino hacia la aceptación y, quizás, el amor.
Género: Novela Visual, Drama, Slice of Life, Romance.
Plataformas: PC (Windows, Mac, Linux).
Público Objetivo: Jugadores que disfrutan de historias profundas, con personajes complejos, bifurcaciones narrativas significativas y un alto grado de rejugabilidad.
Temas Principales: La familia ensamblada, la adaptación al cambio, la búsqueda de la esperanza, el duelo, y el peso de las decisiones pasadas.
📖 Historia y Narrativa
Sinopsis: Tras un evento que cambia su vida, el/la protagonista se muda a una nueva casa con su padre y su nueva familia: su madrastra, Emily, y sus dos hijas, Mana y Ana. El jugador deberá navegar las complejas dinámicas familiares, forjar nuevos lazos, enfrentar hostilidades y descubrir si este nuevo lugar puede convertirse en un verdadero hogar.

Estructura Narrativa:

Introducción Meta-Narrativa: El juego arranca con una introducción única que rompe la cuarta pared. Un personaje secundario se dirige directamente al jugador, y su diálogo cambia en la segunda, tercera y posteriores partidas, reconociendo la rejugabilidad.
Capítulo 1 - "Un Nuevo Comienzo": Se centra en el primer día en la casa nueva. Establece el tono, presenta a los personajes principales y sus conflictos centrales, y culmina en la primera cena familiar.
(Futuros Capítulos): La historia continuará explorando la adaptación del protagonista y la evolución de sus relaciones.
Bifurcaciones y Consecuencias:

> Ruta de Género: La decisión más importante del juego. Al inicio, el jugador elige entre un protagonista masculino o femenino.
Esto no es solo un cambio de avatar; desbloquea escenas, diálogos y eventos completamente diferentes (chapter1_male_route vs chapter1_female_route).
Las interacciones iniciales y los conflictos menores varían drásticamente (ej. la decisión del osito para la ruta femenina vs. la de los libros de dragones para la masculina).
> Sistema de Afecto:
Las decisiones en los diálogos impactan directamente los puntos de afecto con Emily, Ana y Mana.
Estos puntos (emily_affection, ana_affection, etc.) se acumulan positiva o negativamente.
Alcanzar ciertos umbrales de afecto desbloqueará rutas de romance o consolidará rutas de amistad, llevando a escenas y CGs exclusivos.
> Sistema de Banderas (Flags):
Pequeñas decisiones se registran en variables (tomo_osito, si_cuento, meterme).
Estas banderas provocan cambios sutiles pero visibles más adelante. Por ejemplo, si el jugador toma el osito de Ana, el sprite de Ana cambiará en escenas futuras para no tenerlo, y las escenas de fondo también se adaptarán (escena_conosito_ vs escena_sinosito_).
🎭 Personajes
(Esto es ideal para una base de datos en Notion)

Protagonista (MC)
Nombre: Personalizable (Por defecto: "Ren" [M], "Yuna" [F]).
Rol: El avatar del jugador. Su personalidad se forja a través de las elecciones, pudiendo ser conciliador, rebelde, amable o distante.
Emily
Rol: La madrastra. Es la figura maternal, cariñosa y mediadora del grupo. Su principal objetivo es que el/la protagonista se sienta parte de la familia.
Color de Diálogo: #E8A8B7 (Rosa).
Ana
Rol: La hermanastra menor. Inocente, curiosa y llena de energía. Es la primera en intentar conectar con el/la protagonista de forma genuina.
Color de Diálogo: #3183c7 (Azul).
Mana
Rol: La hermanastra mayor. Actúa como la antagonista inicial. Es hostil, sarcástica y ve al protagonista como un intruso que ha venido a romper la paz familiar.
Color de Diálogo: #703543 (Rojo oscuro).
🎮 Mecánicas de Juego
> Creación de Personaje:

El jugador es recibido con una pantalla de selección de género totalmente personalizada (pantalla_seleccion_imagemap) con imágenes dinámicas.
Posteriormente, introduce su nombre a través de una pantalla de input también personalizada.
> Minijuego de Reflejos con Teclado:

Contexto: Se activa en momentos de alta tensión o acción, como una pelea o una situación que requiere rapidez mental.
Objetivo: Pulsar la tecla correcta que aparece en pantalla antes de que una barra de tiempo se agote.
Características Únicas:
Estilo Aleatorio: Para aumentar el desafío, la letra a pulsar cambia aleatoriamente de fuente, color, tamaño y posición en cada turno, obligando al jugador a adaptarse visualmente.
Dificultad Ajustable: El tiempo para reaccionar depende de la dificultad seleccionada (facil, medio, dificil).
Vidas y Puntuación: El jugador cuenta con un número limitado de vidas y debe alcanzar una puntuación objetivo para ganar.
Impacto Narrativo: El resultado del minijuego (win o lose) tiene consecuencias directas en la historia. Ganar puede significar salir airoso de un conflicto, mientras que perder puede resultar en consecuencias negativas para el protagonista.
> Interfaz y Experiencia de Usuario (UI/UX):

UI Personalizada: Todos los menús (principal, pausa, guardado, opciones) tienen un diseño y estilo visual cohesivo y único.
Sonidos de Interfaz: Las interacciones con los botones tienen efectos de sonido (play_ui_sound), que pueden ser activados o desactivados por el jugador en el menú de opciones.
Soporte Multilenguaje: El juego está estructurado para soportar múltiples idiomas, con un selector funcional (Español/Inglés) en el menú principal.
Transiciones Cinematográficas: Se utilizan efectos de transición personalizados como eye_open_slow_effect para crear una inmersión mayor en momentos clave.
🎨 Arte y Sonido
> Estilo Visual:

Sprites de Personajes: Expresiones faciales y poses variadas para cada personaje, que cambian según la situación.
Fondos (BGs): Escenarios detallados que establecen la atmósfera de la historia.
CGs (Ilustraciones Especiales): Imágenes de alta calidad para momentos importantes. El sistema está preparado para mostrar CGs neutrales, así como CGs específicos de eventos de género (evento_cajas, evento_muebles).
Interfaz Gráfica (GUI): Un diseño visual único y profesional para todos los elementos de la interfaz.
> Diseño de Sonido:

Banda Sonora (BGM): Pistas musicales específicas para el menú principal, la creación de personaje y diferentes ambientes dentro del Capítulo 1 (c1_musica, c1_musica2, etc.).
Efectos de Sonido (SFX): Sonidos para la UI, notificaciones de decisiones y eventos clave para mejorar la retroalimentación al jugador.
🗺️ Hoja de Ruta (Roadmap)
Estado Actual: Alpha 0.01

> Contenido Implementado:

[x] Sistema de introducción meta-narrativa con 5+ variantes.
[x] Flujo de creación de personaje completo (género y nombre).
[x] Capítulo 1 completo con dos rutas principales (masculina/femenina) y múltiples decisiones.
[x] Sistemas de afecto y banderas 100% funcionales.
[x] Minijuego de teclado con estilo aleatorio integrado en la narrativa.
[x] UI y menús personalizados.
[x] Soporte para Español e Inglés.
> Próximos Pasos:

[ ] Galería de CGs: Implementar la pantalla de galería (actualmente muestra un aviso de "WIP").
[ ] Capítulo 2: Desarrollo de la continuación de la historia, explorando las consecuencias de las decisiones del Capítulo 1.
[ ] Expandir Rutas de Romance: Añadir más escenas clave y CGs para los personajes con los que se puede tener un romance.
[ ] Actuación de Voz: El juego está preparado (config.has_voice = True) para una futura implementación de voces.
