"""
data/entrenamiento.py — Planes de entrenamiento individuales
Armas reales del juego, fases largas y detalladas
"""

PLANES_INDIVIDUALES = {
    "anderson1": {
        "nombre": "Anderson (IGL) — Roster Principal",
        "rol": "IGL",
        "fase_actual": 1,
        "fases": {
            1: {
                "titulo": "Fundamentos del IGL — Lectura de Mapa y Comunicación",
                "meta": "Dar callouts precisos en el 100% de las rondas y que el equipo entienda la estrategia antes de ejecutar",
                "ejercicios": [
                    {"nombre": "Callouts de posición", "descripcion": "Cada ronda, nombrar en voz alta la zona exacta de cada enemigo visible. Ej: 'Rival en Sentry Camp, MP7, mirando norte'", "duracion": "15 min", "dias": "Lunes, Miércoles, Viernes"},
                    {"nombre": "Decisión en 3 segundos", "descripcion": "Antes de cada ronda tienes 3 segundos para decir en voz alta: ruta de push, utilidad a usar, objetivo. Entrenarlo en training mode primero", "duracion": "10 min", "dias": "Martes, Jueves"},
                    {"nombre": "Estudio de replays propios", "descripcion": "Ver 2 replays de partidas propias por semana. Identificar 3 decisiones que pudiste hacer mejor como IGL", "duracion": "20 min", "dias": "Sábado"},
                    {"nombre": "Warm-up con M4A1", "descripcion": "15 minutos de training mode con M4A1 — centering a nivel de cabeza, 3 objetivos distintos por minuto", "duracion": "15 min", "dias": "Diario"},
                    {"nombre": "Estudio de mapa: Valle Abandonado", "descripcion": "Memorizar todas las zonas y rutas de Valle Abandonado (The Valley). Dibujar el mapa de memoria y nombrar zonas clave", "duracion": "10 min", "dias": "Lunes, Jueves"},
                ],
            },
            2: {
                "titulo": "Toma de Decisiones Bajo Presión",
                "meta": "Tomar decisiones correctas en los últimos 30 segundos de cada ronda sin entrar en pánico",
                "ejercicios": [
                    {"nombre": "Simulación de 1v3", "descripcion": "Entrar a situaciones de desventaja numérica en training mode. Decidir: ¿rush, hold, o rotar? Comunicar la decisión antes de ejecutar", "duracion": "20 min", "dias": "Lunes, Miércoles"},
                    {"nombre": "Rotaciones avanzadas", "descripcion": "En mapa de Playa Cielo (Skyline Beach): practicar 5 rutas de rotación distintas desde Skyline City. Cronometrar cada una", "duracion": "15 min", "dias": "Martes, Viernes"},
                    {"nombre": "Economia en TCT", "descripcion": "Estudiar el sistema económico del parche 10/02/2026 — nueva reforma económica. Practicar decisiones de compra óptimas según el dinero disponible", "duracion": "15 min", "dias": "Jueves"},
                    {"nombre": "Comunicación táctica avanzada", "descripcion": "Dar briefing pre-ronda completo en 10 palabras o menos. Practicar síntesis: 'Rush Prisión, humo izquierda, Flash entrada'", "duracion": "10 min", "dias": "Diario en scrims"},
                    {"nombre": "Análisis del sistema Wildcard", "descripcion": "Estudiar el nuevo sistema Wildcard del parche 10/02/2026. Identificar cuáles Wildcards benefician más al IGL y al equipo en distintas situaciones", "duracion": "15 min", "dias": "Sábado"},
                ],
            },
            3: {
                "titulo": "IGL Avanzado — Adaptación y Liderazgo en Torneos",
                "meta": "Ganar más rondas por adaptación táctica que por mecánicas puras. Ser el IGL que lee al rival en tiempo real",
                "ejercicios": [
                    {"nombre": "Scouting de rivales", "descripcion": "Antes de cada torneo o scrim, analizar el estilo de juego del equipo rival. ¿Rushean siempre? ¿Holdean? ¿Qué Strikers usan?", "duracion": "30 min", "dias": "Pre-torneo"},
                    {"nombre": "Mid-game adaptation", "descripcion": "Regla: si pierdes 2 rondas seguidas con la misma estrategia, debes cambiarla. Practicar tener 3 planes alternativos preparados por mapa", "duracion": "20 min", "dias": "Martes, Viernes"},
                    {"nombre": "Comunicación de liderazgo", "descripcion": "Trabajar el tono de voz del IGL: firme y claro bajo presión, nunca agresivo ni pánico. Grabar y escuchar tu propia voz en scrims", "duracion": "15 min", "dias": "Scrims"},
                    {"nombre": "Mastery de Strikers de info", "descripcion": "Aprender a sacarle máximo provecho a NOVA (escaneo) y ETHAN (rastreo). Practicar timing perfecto de habilidades para dar info útil al equipo", "duracion": "20 min", "dias": "Lunes, Jueves"},
                    {"nombre": "Post-match review completo", "descripcion": "Después de cada torneo: analizar las 3 rondas más importantes ganadas y perdidas. ¿Qué decidió el resultado?", "duracion": "30 min", "dias": "Post-torneo"},
                ],
            },
        },
    },

    "jose": {
        "nombre": "Jose (Fragger) — Roster Principal",
        "rol": "Fragger",
        "fase_actual": 1,
        "fases": {
            1: {
                "titulo": "Mecánicas Base del Fragger — Aim y Movimiento",
                "meta": "Ganar el 60% de los duelos 1v1 en corta distancia con MP5 o MP7",
                "ejercicios": [
                    {"nombre": "Training mode: Centering con MP5", "descripcion": "30 minutos de training mode con MP5. Mantener la mira a nivel de cabeza constantemente — nunca al suelo. 3 series de 10 minutos", "duracion": "30 min", "dias": "Diario"},
                    {"nombre": "Jiggle peek básico", "descripcion": "Practicar jiggle peek en esquinas del training mode. Salir por la derecha, disparar, volver. Luego por la izquierda. 100 repeticiones cada sesión", "duracion": "20 min", "dias": "Lunes, Miércoles, Viernes"},
                    {"nombre": "Flash + Entry", "descripcion": "Lanzar Flash correctamente antes de entrar a cada cuarto. Practicar el timing: Flash sale → esperar 1 segundo → entrar con MP5. Repetir en cada zona de Isla Siniestra", "duracion": "15 min", "dias": "Martes, Jueves"},
                    {"nombre": "Hiperfuego con MP7", "descripcion": "Usar MP7 con el nuevo buff. 15 minutos de duelos en modo hiperfuego disparando desde la cadera — practicar la nueva precisión sin apuntar que trae el buff", "duracion": "15 min", "dias": "Miércoles, Sábado"},
                    {"nombre": "Sensibilidad fija", "descripcion": "Mantener sensibilidad (X)(Y) igual todos los días. Resistir cambiarla. La consistencia de sensi es parte del entrenamiento", "duracion": "N/A", "dias": "Regla permanente"},
                ],
            },
            2: {
                "titulo": "Fragger Intermedio — Rush Coordinado y Utilidades",
                "meta": "Coordinar el rush con el IGL y usar Flash correctamente en el 80% de los entries",
                "ejercicios": [
                    {"nombre": "Entry con HK416", "descripcion": "Practicar el HK416 nuevo con Culata BAS Tipo C. El accesorio elimina el retraso al salir del sprint — practicar sprint → stop → disparar en training mode. 200 repeticiones", "duracion": "25 min", "dias": "Lunes, Jueves"},
                    {"nombre": "Rush coordinado con IGL", "descripcion": "En scrims: Jose nunca entra sin la orden del IGL. Cuando Anderson diga 'rush', Jose tiene 1 segundo para Flash + entrar. Practicar esta coordinación en modo sala", "duracion": "30 min", "dias": "Scrims"},
                    {"nombre": "Swap de arma", "descripcion": "Practicar el swap (MP5 → pistola) cuando la principal se vacía en duelo activo. Es más rápido que recargar. 5 series de 20 swaps cada sesión", "duracion": "15 min", "dias": "Martes, Viernes"},
                    {"nombre": "Pre-fire de posiciones", "descripcion": "Memorizar las 5 posiciones más comunes de los rivales en cada mapa. Practicar disparar hacia esas posiciones antes de verlos — pre-fire correcto", "duracion": "20 min", "dias": "Lunes, Miércoles"},
                    {"nombre": "Dominar Isla Siniestra", "descripcion": "Prisión → Puerto → Sala de Calderas: memorizar cada ángulo de Shutter Island. Sin loot, solo movimiento y posicionamiento 10 minutos en cada zona", "duracion": "30 min", "dias": "Sábado"},
                ],
            },
            3: {
                "titulo": "Fragger Elite — Lectura de Duelo y Decisiones Tácticas",
                "meta": "Ganar el 75% de duelos 1v1 y tomar la decisión correcta entre rush y hold en tiempo real",
                "ejercicios": [
                    {"nombre": "Replay analysis de duelos perdidos", "descripcion": "Ver cada duelo perdido en replay. ¿Fue sensi? ¿Centering? ¿Timing? ¿Posición? Identificar el error específico, no solo 'me mataron'", "duracion": "20 min", "dias": "Miércoles, Sábado"},
                    {"nombre": "Mastery del HK416 + BAS", "descripcion": "El HK416 es el nuevo meta (feb 2026). Dominar completamente su curva de recoil y el timing de la Culata BAS. Comparar con MP7 — ¿cuál funciona mejor en tu estilo?", "duracion": "25 min", "dias": "Lunes, Jueves"},
                    {"nombre": "Juego de info", "descripcion": "Como fragger, dar info de posición al IGL después de CADA duelo. No solo matar — reportar dónde estaba el rival, qué arma tenía, si había más atrás", "duracion": "N/A", "dias": "Regla en todos los scrims"},
                    {"nombre": "Situaciones de 1v2", "descripcion": "Entrenar situaciones 1v2: ¿rush o esperar? Regla: si tienes ventaja de posición, esperar. Si no, crear confusión con Flash y salir. 20 situaciones por sesión", "duracion": "25 min", "dias": "Martes, Viernes"},
                    {"nombre": "Striker para fragger", "descripcion": "Practicar con RAN (velocidad) y KRAKEN (gancho) — los dos Strikers ideales para fragger. Aprender cuándo activar cada habilidad en partida real", "duracion": "20 min", "dias": "Jueves, Sábado"},
                ],
            },
        },
    },

    "xavier": {
        "nombre": "Xavier (Ancla) — Roster Principal",
        "rol": "Ancla",
        "fase_actual": 1,
        "fases": {
            1: {
                "titulo": "Ancla Base — Posicionamiento y Hold de Zona",
                "meta": "Mantener la zona asignada durante 5 rondas seguidas sin perderla por decisiones propias",
                "ejercicios": [
                    {"nombre": "Hold en Skyline City", "descripcion": "Practicar hold en Skyline City (Playa Cielo) cubriendo los 4 ángulos de entrada. Identificar el ángulo principal y los dos secundarios. 15 minutos de hold solo en modo sala", "duracion": "15 min", "dias": "Lunes, Miércoles"},
                    {"nombre": "Molotov de defensa", "descripcion": "Practicar lanzamiento de Molotov exacto en las 3 entradas principales de cada mapa. El Molotov debe caer justo en la entrada — ni antes ni después", "duracion": "15 min", "dias": "Martes, Jueves"},
                    {"nombre": "Hold con M4A1 y FN2000", "descripcion": "20 minutos alternando M4A1 y FN2000 en posición de hold de media distancia. FN2000 post-buff (enero 2026) tiene +1 daño en cabeza — ideal para ancla que espera el duelo", "duracion": "20 min", "dias": "Diario"},
                    {"nombre": "Comunicación de flanco", "descripcion": "Cada vez que escuches pasos en el flanco, reportarlo al IGL ANTES de ir a verificar. Nunca moverse sin avisar. Regla de oro del ancla", "duracion": "N/A", "dias": "Regla en scrims"},
                    {"nombre": "Granada Adhesiva táctica", "descripcion": "Practicar colocación de Granada Adhesiva en los 3 corners más frecuentados de cada zona. Memorizar los puntos de pegado óptimos", "duracion": "10 min", "dias": "Viernes"},
                ],
            },
            2: {
                "titulo": "Ancla Avanzado — Hold Agresivo y Adaptación",
                "meta": "Decidir correctamente entre hold pasivo y hold agresivo según la situación. Ganar el 70% de duelos defensivos",
                "ejercicios": [
                    {"nombre": "Hold agresivo vs pasivo", "descripcion": "En modo sala: practicar hold agresivo (salir a buscar) vs pasivo (esperar en ángulo). Regla: agresivo solo si tienes info confirmada de posición del rival. 20 situaciones por sesión", "duracion": "20 min", "dias": "Lunes, Jueves"},
                    {"nombre": "Dominar Prisión en Isla Siniestra", "descripcion": "Memorizan todos los ángulos de Prisión (Shutter Island). El Ancla que domina Prisión domina el mapa completo. 15 minutos de posicionamiento solo en Prisión", "duracion": "15 min", "dias": "Martes, Sábado"},
                    {"nombre": "VOLT como Striker", "descripcion": "Aprender a usar VOLT correctamente — el escudo frontal ideal para el ancla. Practicar timing de activación: cuando el rival ya está disparando, no antes", "duracion": "15 min", "dias": "Miércoles, Viernes"},
                    {"nombre": "Multiangle coverage", "descripcion": "Practicar cubrir 2 ángulos desde una sola posición usando movimiento de peek. El ancla que cubre más ángulos desde menos posiciones da menos info al rival", "duracion": "20 min", "dias": "Martes, Jueves"},
                    {"nombre": "Replay de holds perdidos", "descripcion": "Ver replays de rondas donde perdiste tu zona. ¿Saliste cuando no debías? ¿Estabas en el ángulo equivocado? ¿No usaste Molotov a tiempo?", "duracion": "15 min", "dias": "Sábado"},
                ],
            },
            3: {
                "titulo": "Ancla Elite — Lectura de Rush y Control Total de Zona",
                "meta": "Anticipar el rush rival antes de que llegue y tener el counter listo. Nunca perder zona por sorpresa",
                "ejercicios": [
                    {"nombre": "Leer el rush antes de que llegue", "descripcion": "Estudiar los 3 patrones de rush más comunes de los rivales habituales. ¿Siempre por el mismo lado? ¿A qué tiempo de ronda? Preparar el Molotov o Flash antes de que lleguen", "duracion": "20 min", "dias": "Pre-scrim"},
                    {"nombre": "SPIKE + VOLT combo", "descripcion": "Practicar la combinación SPIKE (barrera en entrada) + VOLT (escudo personal). La barrera ralentiza, el escudo aguanta el daño restante. Activar en secuencia correcta", "duracion": "15 min", "dias": "Lunes, Viernes"},
                    {"nombre": "Hold con HK416", "descripcion": "El HK416 nuevo es también excelente para ancla de corta-media. Practicar su uso desde posición defensiva — el BAS elimina el retraso al salir del sprint si el rival te sorprende", "duracion": "20 min", "dias": "Miércoles, Sábado"},
                    {"nombre": "Rotación táctica del ancla", "descripcion": "Practicar el único caso en que el ancla debe rotar: cuando el IGL lo ordena. Practicar la rotación más rápida entre Skyline City y Lighthouse en Playa Cielo", "duracion": "15 min", "dias": "Martes, Jueves"},
                    {"nombre": "Liderazgo defensivo", "descripcion": "El ancla elite no solo holdea — organiza la defensa. Practicar dar instrucciones defensivas al soporte cuando el IGL está ocupado atacando", "duracion": "N/A", "dias": "Scrims"},
                ],
            },
        },
    },

    "alejandro": {
        "nombre": "Alejandro (Soporte M+L) — Roster Principal",
        "rol": "Soporte Media y Larga",
        "fase_actual": 1,
        "fases": {
            1: {
                "titulo": "Soporte Base — Dominar el AR97 y VSS Post-Buff",
                "meta": "Usar correctamente el AR97 buffed y el VSS en media-larga distancia. Dar info al IGL en el 100% de las rondas",
                "ejercicios": [
                    {"nombre": "AR97 post-buff — control de recoil", "descripcion": "El AR97 tuvo BUFF DOBLE en enero 2026 (mayor cadencia + retroceso muy reducido). Practicar su nueva curva de recoil en training mode. 20 minutos con mira 4x en objetivos a 30-50 metros", "duracion": "20 min", "dias": "Lunes, Miércoles, Viernes"},
                    {"nombre": "VSS — cargador y posicionamiento", "descripcion": "El VSS recibió +10 balas en todos los cargadores (enero 2026). Practicar el VSS en media distancia con su nuevo cargador. La semi-silenciosidad da ventaja de info — el rival no sabe exactamente desde dónde disparas", "duracion": "15 min", "dias": "Martes, Jueves"},
                    {"nombre": "Centering avanzado para soporte", "descripcion": "El soporte de media debe tener centering perfecto porque tiene mira — no hay excusa de ajuste lento. 20 minutos de training mode con AR97 4x: la mira debe ir DIRECTO a la cabeza sin ajuste visible", "duracion": "20 min", "dias": "Diario"},
                    {"nombre": "Callouts de soporte", "descripcion": "Cada ronda, Alejandro debe dar al menos 2 callouts de posición de rivales al IGL. Practicar el formato: 'Rival en [zona], [arma], [dirección que mira]'", "duracion": "N/A", "dias": "Regla en scrims"},
                    {"nombre": "Manejo de Humo", "descripcion": "El soporte maneja los humos del equipo. Practicar colocación de humo correcta: entre el equipo y el ángulo peligroso, nunca entre el equipo y su objetivo", "duracion": "10 min", "dias": "Viernes"},
                ],
            },
            2: {
                "titulo": "Soporte Avanzado — Cobertura de Larga Distancia y Kar98k",
                "meta": "Hacer al menos 1 eliminación de larga distancia por ronda cubriendo el rush del equipo",
                "ejercicios": [
                    {"nombre": "Introducción al Kar98k", "descripcion": "El soporte larga debe aprender el Kar98k para Valle Abandonado y Playa Cielo. Empezar con M700 (más fácil) y migrar al Kar. 25 minutos de training mode, solo disparos a cabeza", "duracion": "25 min", "dias": "Lunes, Jueves"},
                    {"nombre": "Cobertura de rush", "descripcion": "Ejercicio de equipo: Jose rushea, Alejandro cubre desde posición elevada con AR97 o Kar98k. El soporte elimina a quien intente cortar el rush. Practicar en Valle Abandonado", "duracion": "20 min", "dias": "Martes, Viernes"},
                    {"nombre": "Posicionamiento en Lighthouse", "descripcion": "En Playa Cielo (Skyline Beach): dominar completamente Lighthouse. Memorizar las líneas de visión a Skyline City y Cultural Center. 10 minutos de posicionamiento solo", "duracion": "10 min", "dias": "Miércoles"},
                    {"nombre": "M82 en TCT", "descripcion": "El M82 es ahora arma de suelo en TCT (parche 10/02/2026). Practicar recogerlo y usarlo en Valle Abandonado cuando aparece. Daño masivo pero cadencia muy baja — una oportunidad", "duracion": "15 min", "dias": "Jueves, Sábado"},
                    {"nombre": "NOVA como Striker", "descripcion": "NOVA es el Striker ideal para soporte — su escaneo de área da info que complementa perfectamente la posición elevada del soporte. Practicar timing del escaneo antes de cada push del equipo", "duracion": "15 min", "dias": "Sábado"},
                ],
            },
            3: {
                "titulo": "Soporte Elite — Dictador de Ritmo desde la Distancia",
                "meta": "Controlar el ritmo del mapa desde posición de soporte. El rival debe siempre pensar en Alejandro aunque no lo vea",
                "ejercicios": [
                    {"nombre": "Presencia psicológica", "descripcion": "El soporte elite hace que el rival siempre tenga que cubrir su posición. Practicar disparar ocasionalmente para revelar presencia — el rival pierde atención dividida. Con VSS es más difícil de ubicar", "duracion": "N/A", "dias": "Concepto a aplicar en scrims"},
                    {"nombre": "Mastery del Kar98k", "descripcion": "El Kar98k debe ser arma secundaria dominada. 30 minutos de training mode solo con Kar98k: 80% de headshots mínimo antes de llevarlo a scrims", "duracion": "30 min", "dias": "Lunes, Viernes"},
                    {"nombre": "Adaptación de loadout por mapa", "descripcion": "Valle Abandonado: Kar98k. Playa Cielo: AR97 + VSS. Isla Siniestra: AR97 + MP7 (no hay larga distancia). Practicar cada loadout en su mapa", "duracion": "20 min", "dias": "Martes, Sábado"},
                    {"nombre": "Soporte de curación con EMMA", "descripcion": "EMMA como Striker alternativo para Alejandro — su curación de área sostiene al equipo en hold prolongados. Combinar con AR97 para soporte total", "duracion": "15 min", "dias": "Jueves"},
                    {"nombre": "Liderazgo táctico desde atrás", "descripcion": "El soporte con visión amplia debe dar info que el IGL no tiene. Practicar ser la 'segunda cámara' del IGL: ve lo que él no ve y comunícalo antes de que lo necesite", "duracion": "N/A", "dias": "Scrims"},
                ],
            },
        },
    },

    "antonio": {
        "nombre": "Antonio (Fragger Entry) — Roster Secundario",
        "rol": "Fragger",
        "fase_actual": 1,
        "fases": {
            1: {
                "titulo": "Entry Agresivo — Fundamentos de Rush y Duelo",
                "meta": "Entrar primero en cada round y ganar al menos el primer duelo con el 65% de consistencia",
                "ejercicios": [
                    {"nombre": "MP5 mastery CQB", "descripcion": "40 minutos diarios de training mode solo con MP5. Antonio es entry fragger — el MP5 debe ser una extensión de su mano. Meta: headshot en el 50% de los disparos a corta distancia", "duracion": "40 min", "dias": "Diario"},
                    {"nombre": "Flash de entry perfecto", "descripcion": "El entry fragger nunca entra sin Flash. Practicar el lanzamiento correcto: Flash hacia el techo de la entrada para que caiga dentro y ciegue. 50 repeticiones por sesión", "duracion": "15 min", "dias": "Lunes, Miércoles, Viernes"},
                    {"nombre": "Velocidad de movimiento", "descripcion": "Antonio debe ser el más rápido en llegar a Puerto (Isla Siniestra) y Missile Basement (Valle Abandonado). Cronometrar y reducir tiempo de llegada cada sesión", "duracion": "10 min", "dias": "Martes, Jueves"},
                    {"nombre": "KRAKEN — gancho de entry", "descripcion": "Aprender a usar KRAKEN como Striker. El gancho permite llegar a posiciones de entrada en menos tiempo que corriendo. Practicar el timing del gancho + disparo inmediato", "duracion": "15 min", "dias": "Miércoles, Sábado"},
                    {"nombre": "HK416 BAS entry rush", "descripcion": "El HK416 con Culata BAS Tipo C es perfecto para Antonio — sprint → stop → disparo sin retraso. 20 minutos de training mode: sprint a un objetivo, parar y disparar en menos de 0.5 segundos", "duracion": "20 min", "dias": "Martes, Viernes"},
                ],
            },
            2: {
                "titulo": "Entry Coordinado — Rush de Equipo y Adaptación",
                "meta": "Coordinar el entry con el IGL del roster secundario. Ganar el 70% de los primeros duelos",
                "ejercicios": [
                    {"nombre": "Timing de entry con IGL", "descripcion": "Practicar sincronización: cuando el IGL dice 'entra', Antonio tiene exactamente 0.5 segundos para Flash + entrada. Demasiado lento = Flash se gasta antes de cegar. Practicar en sala", "duracion": "20 min", "dias": "Scrims"},
                    {"nombre": "Counter al anti-rush", "descripcion": "Cuando el rival tiene Molotov en la entrada: practicar saltar la zona de fuego o tomar ruta alternativa. 15 situaciones de entrada con obstáculo por sesión", "duracion": "15 min", "dias": "Lunes, Jueves"},
                    {"nombre": "Bizon (PP-19) como alternativa", "descripcion": "El Bizon es la alternativa al MP5 para rushes largos. Su cargador enorme permite supresión continua sin recargar. 20 minutos con Bizon en Isla Siniestra", "duracion": "20 min", "dias": "Martes, Sábado"},
                    {"nombre": "Comunicación post-entry", "descripcion": "Después de entrar, dar info: '2 eliminados, 1 vivo en Prisión esquina derecha, yo bajo en vida'. La info post-entry vale tanto como el entry mismo", "duracion": "N/A", "dias": "Regla en scrims"},
                    {"nombre": "RAN — velocidad de entrada", "descripcion": "RAN Striker: el dash de velocidad permite llegar antes que cualquier rival a puntos clave. Practicar el dash justo antes de la entrada para ganar la fracción de segundo", "duracion": "15 min", "dias": "Miércoles, Viernes"},
                ],
            },
            3: {
                "titulo": "Entry Elite — Dominio Psicológico y Lectura de Rivales",
                "meta": "El rival ya sabe cómo juegas. Ahora debes ser impredecible sin perder efectividad",
                "ejercicios": [
                    {"nombre": "Variar rutas de entry", "descripcion": "Nunca usar la misma ruta de entrada dos rondas seguidas. Alternar rutas en Isla Siniestra: Puerto → Planta de Agua → Área Residencial en rotación impredecible", "duracion": "N/A", "dias": "Concepto para torneos"},
                    {"nombre": "Fake entry", "descripcion": "Practicar el fake: lanzar Flash hacia una entrada pero NO entrar — esperar que el rival salga a checkear, y entonces eliminarlo. 10 fakes exitosos por sesión", "duracion": "20 min", "dias": "Lunes, Jueves"},
                    {"nombre": "Mastery HK416 avanzado", "descripcion": "El HK416 para Antonio en nivel elite: dominar el full-auto en corta Y el burst en media. El accesorio BAS lo hace polivalente para el entry en cualquier mapa", "duracion": "25 min", "dias": "Martes, Viernes"},
                    {"nombre": "KRAKEN + LUCIAN combo", "descripcion": "KRAKEN entra con gancho, LUCIAN dispara en movimiento con mayor precisión. Practicar activar habilidad de LUCIAN durante el entry para mejorar precisión bajo estrés", "duracion": "20 min", "dias": "Miércoles, Sábado"},
                    {"nombre": "Análisis de muertes en entry", "descripcion": "Cada muerte en entry: analizar en replay. ¿Fue el Flash? ¿El timing? ¿El rival ya esperaba? Identificar si fue error de mecánica o de lectura", "duracion": "15 min", "dias": "Post-scrim"},
                ],
            },
        },
    },

    "anderson2": {
        "nombre": "Anderson 2 (Todo Rango) — Roster Secundario",
        "rol": "Fragger",
        "fase_actual": 1,
        "fases": {
            1: {
                "titulo": "Definir Rol y Fundamentos",
                "meta": "Identificar en qué distancia y rol eres más efectivo. Elegir arma principal y dominarla",
                "ejercicios": [
                    {"nombre": "Test de distancias", "descripcion": "Una semana usando MP5/MP7 (corta), una semana usando M4A1 (media), una semana usando AR97 (media-larga). Anotar en cuál te sientes más cómodo y obtienes más eliminaciones", "duracion": "30 min", "dias": "Diario — rotando por semana"},
                    {"nombre": "Sensi estable", "descripcion": "Mantener la misma sensibilidad (X)(Y) durante el mes completo de prueba de roles. No cambiarla. La consistencia de sensi es prerequisito para cualquier rol", "duracion": "N/A", "dias": "Regla permanente"},
                    {"nombre": "Warm-up diario básico", "descripcion": "15 minutos de training mode con el arma que estés probando esa semana. Centering a nivel de cabeza siempre", "duracion": "15 min", "dias": "Diario"},
                    {"nombre": "Jugar todas las posiciones en sala", "descripcion": "En modo sala: una ronda como entry, una como ancla, una como soporte. Identificar dónde rindes más naturalmente", "duracion": "30 min", "dias": "Miércoles, Sábado"},
                    {"nombre": "Aprender los mapas", "descripcion": "Memorizan las zonas clave de los 3 mapas: Valle Abandonado, Playa Cielo e Isla Siniestra. Saber cómo se llama cada zona es prerequisito para comunicar", "duracion": "10 min", "dias": "Lunes, Jueves"},
                ],
            },
            2: {
                "titulo": "Especialización y Desarrollo Acelerado",
                "meta": "Definir rol definitivo y empezar plan de entrenamiento específico",
                "ejercicios": [
                    {"nombre": "Arma principal fija", "descripcion": "Con el rol definido, elegir arma principal y secundaria. No cambiar por 30 días. La consistencia de arma = acumulación de muscle memory", "duracion": "N/A", "dias": "Regla permanente"},
                    {"nombre": "Entrenamiento de rol específico", "descripcion": "Seguir los ejercicios del rol elegido (Fragger → fase 1 de Jose, Ancla → fase 1 de Xavier, Soporte → fase 1 de Alejandro)", "duracion": "30 min", "dias": "Diario"},
                    {"nombre": "Scrim participation activa", "descripcion": "En scrims del roster secundario: comunicar al IGL después de cada ronda qué funcionó y qué no desde su perspectiva. El jugador que mejora más rápido es el que más reflexiona", "duracion": "N/A", "dias": "Scrims"},
                    {"nombre": "Striker de prueba", "descripcion": "Probar 3 Strikers distintos en una semana cada uno. RAN (velocidad), EMMA (curación), ZERO (anti-habilidad). Notar cuál cambia más tu estilo de juego positivamente", "duracion": "20 min", "dias": "Jueves, Sábado"},
                ],
            },
        },
    },

    "maximiliano": {
        "nombre": "Maximiliano (Soporte M+L) — Roster Secundario",
        "rol": "Soporte Media y Larga",
        "fase_actual": 1,
        "fases": {
            1: {
                "titulo": "Fundamentos desde Cero — Base Técnica Sólida",
                "meta": "Entender los roles del juego, dominar los controles básicos y empezar con el M4A1",
                "ejercicios": [
                    {"nombre": "Training mode diario con M4A1", "descripcion": "El M4A1 es el arma más perdona del juego — perfecta para aprender. 20 minutos diarios en training mode. Objetivo: disparar solo cuando la mira está en el cuerpo del objetivo, no disparar al azar", "duracion": "20 min", "dias": "Diario"},
                    {"nombre": "Aprender los controles avanzados", "descripcion": "Practicar: jiggle peek básico, prone (tirarse), cambio rápido de arma, uso de utilidades. Un control nuevo por sesión hasta dominar todos", "duracion": "15 min", "dias": "Lunes, Miércoles, Viernes"},
                    {"nombre": "Mapas — conocer zonas", "descripcion": "Memorizar los nombres de todas las zonas de los 3 mapas del juego. Shutter Island (Isla Siniestra), Skyline Beach (Playa Cielo), The Valley (Valle Abandonado). Sin mapa conocido no hay comunicación posible", "duracion": "10 min", "dias": "Martes, Jueves"},
                    {"nombre": "Uso correcto del Humo", "descripcion": "El Humo es la utilidad más importante del soporte. Practicar lanzarlo correctamente: entre tú y el peligro, no entre tú y tu equipo. 20 lanzamientos por sesión en cada mapa", "duracion": "10 min", "dias": "Martes, Sábado"},
                    {"nombre": "Ver replays de jugadores pro", "descripcion": "Ver 2 partidas por semana de jugadores de soporte en Blood Strike. Observar: ¿dónde se posicionan? ¿qué utilidades usan? ¿cómo comunican?", "duracion": "20 min", "dias": "Sábado"},
                ],
            },
            2: {
                "titulo": "Desarrollo Intermedio — AR97 y Posicionamiento",
                "meta": "Dominar el AR97 buffed y ocupar posiciones de soporte correctas en el 70% de las rondas",
                "ejercicios": [
                    {"nombre": "Transición M4A1 → AR97", "descripcion": "El AR97 con buff (enero 2026) es el arma de soporte más versátil. Practicar el control del nuevo recoil reducido. 25 minutos de training mode con mira 3x", "duracion": "25 min", "dias": "Lunes, Miércoles, Viernes"},
                    {"nombre": "Posicionamiento de soporte", "descripcion": "El soporte NUNCA va adelante del fragger. Siempre a 5-10 metros atrás, en posición elevada si es posible. Practicar encontrar las mejores posiciones de soporte en cada zona de los 3 mapas", "duracion": "15 min", "dias": "Martes, Jueves"},
                    {"nombre": "Callouts básicos de posición", "descripcion": "Dar al menos 1 callout de posición rival por ronda. Formato: 'Uno en Sala de Calderas mirando hacia Puerto'. Empezar con callouts simples e ir añadiendo detalle", "duracion": "N/A", "dias": "Regla en scrims"},
                    {"nombre": "VSS post-buff", "descripcion": "El VSS recibió +10 balas en todos los cargadores (enero 2026). Probar el VSS en media distancia — su semi-silenciosidad es ventaja para el soporte que no quiere revelar posición", "duracion": "15 min", "dias": "Jueves, Sábado"},
                    {"nombre": "NOVA Striker para soporte", "descripcion": "NOVA es el Striker ideal para Maximiliano — el escaneo de área da info que complementa el rol de soporte. Practicar activar el escaneo antes de cada push del equipo para dar info útil", "duracion": "10 min", "dias": "Sábado"},
                ],
            },
            3: {
                "titulo": "Soporte Sólido — Integración al Roster Principal",
                "meta": "Poder sustituir a Alejandro en el roster principal sin bajar el nivel del equipo",
                "ejercicios": [
                    {"nombre": "AR97 con mira 4x — media-larga", "descripcion": "El objetivo final del soporte es dominar el AR97 a media-larga distancia. 30 minutos de training mode con mira 4x: todos los disparos deben ser al pecho o cabeza, mínimo 70% precisión", "duracion": "30 min", "dias": "Lunes, Jueves"},
                    {"nombre": "Introducción al Kar98k", "descripcion": "Cuando el AR97 esté dominado, empezar con M700 (más fácil que Kar). Meta: ganar 3 duelos de larga distancia por sesión antes de pasar al Kar98k", "duracion": "20 min", "dias": "Martes, Viernes"},
                    {"nombre": "Scrim en roster principal", "descripcion": "Participar en al menos 2 scrims del roster principal por semana. Aplicar exactamente el mismo sistema de comunicación y posicionamiento que Alejandro", "duracion": "N/A", "dias": "Cuando el coach lo autorice"},
                    {"nombre": "Posición en Lighthouse y Airforce", "descripcion": "Dominar las posiciones de soporte larga en Playa Cielo (Lighthouse) y Valle Abandonado (Airforce Base). Memorizar líneas de visión y puntos ciegos", "duracion": "20 min", "dias": "Miércoles, Sábado"},
                    {"nombre": "Review de progreso con coach", "descripcion": "Sesión semanal de review con el coach: ¿en qué mejoró? ¿qué sigue pendiente? ¿está listo para scrims del roster principal?", "duracion": "30 min", "dias": "Domingo"},
                ],
            },
        },
    },
}

RUTINA_EQUIPO = {
    "titulo": "Rutina de Equipo BloodStrike Elite",
    "frecuencia": "4-5 veces por semana | Duración total: 90 minutos",
    "estructura": [
        {
            "bloque": "🔥 Warm-up Individual",
            "duracion": "15 minutos",
            "descripcion": "Cada jugador en training mode con su arma principal. Anderson y Jose: MP5/MP7 — centering a nivel de cabeza. Xavier: M4A1 — hold de ángulos. Alejandro: AR97 con mira 4x — precisión a distancia. Todos: 0 comunicación, solo aim.",
        },
        {
            "bloque": "💣 Warm-up de Utilidades",
            "duracion": "10 minutos",
            "descripcion": "En sala privada: cada jugador practica sus 2 utilidades principales. Flash: timing correcto de lanzamiento para entry. Molotov: colocación exacta en entradas clave de cada mapa. Humo: posición correcta para cortar ángulos. Granada Adhesiva: puntos de pegado en corners.",
        },
        {
            "bloque": "📋 Briefing Táctico del Día",
            "duracion": "10 minutos",
            "descripcion": "Anderson (IGL) presenta la táctica del día: qué mapa, qué estrategia (rush, hold, control de mapa), qué Strikers usa cada quien, y qué utilidades. El equipo hace preguntas. Sin preguntas = sin excusas de no entender durante el scrim.",
        },
        {
            "bloque": "⚔️ Scrim de Equipo",
            "duracion": "40 minutos",
            "descripcion": "2-3 partidas completas aplicando la táctica del día. Anderson da órdenes claras. Todos registran el resultado de cada partida en el bot (kills, daño, posición). Sin excusas de lag o de arma — foco total en la táctica.",
        },
        {
            "bloque": "🔍 Review Post-Scrim",
            "duracion": "15 minutos",
            "descripcion": "Ver el replay de las 2-3 rondas más importantes. Anderson señala: ¿dónde fue el error táctico? ¿Quién estuvo fuera de posición? ¿Qué utilidad faltó? Feedback constructivo — sin culpar, solo identificar y corregir. Cada jugador dice 1 cosa que hará diferente la próxima sesión.",
        },
    ],
}
