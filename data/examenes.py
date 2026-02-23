"""
data/examenes.py — Banco de preguntas por rol, mapa y nivel
Sistema de ranking por puntuación acumulada
"""

# Niveles: 1=Bronce | 2=Plata | 3=Oro | 4=Diamante | 5=Elite
# Preguntas con 4 opciones, opcion_correcta=índice 0-3

PREGUNTAS = {
    "IGL": {
        1: [  # Bronce
            {
                "pregunta": "¿Cuál es la función principal del IGL en Blood Strike?",
                "opciones": [
                    "A) Fraggear el mayor número de kills",
                    "B) Dar información, dictar timings y tomar decisiones tácticas",
                    "C) Cubrir la zona trasera siempre",
                    "D) Usar francotiradores desde lejos",
                ],
                "correcta": 1,
                "explicacion": "El IGL (In-Game Leader) dirige al equipo: timings, info, rotaciones y decisiones. Los kills son secundarios.",
            },
            {
                "pregunta": "Tu equipo va perdiendo 3-0 en el mapa Aldea. ¿Qué haces primero?",
                "opciones": [
                    "A) Cambiar completamente la estrategia sin avisar",
                    "B) Pedir timeout, analizar qué falló y ajustar el plan",
                    "C) Atacar más rápido para recuperar el marcador",
                    "D) Ignorar el marcador y seguir igual",
                ],
                "correcta": 1,
                "explicacion": "El IGL debe mantener la calma, analizar y comunicar cambios. El timeout mental (pausa y análisis) es clave.",
            },
            {
                "pregunta": "En el mapa Desierto, ¿cuál posición es ideal para el IGL?",
                "opciones": [
                    "A) Siempre primera línea para ver todo",
                    "B) Torre de agua para info panorámica y dictar desde atrás",
                    "C) En el bunker sur esperando",
                    "D) Cruzando el campo abierto sin cobertura",
                ],
                "correcta": 1,
                "explicacion": "El IGL necesita visión amplia. Posición elevada = más info = mejores decisiones.",
            },
            {
                "pregunta": "¿Qué significa 'timing de push' en Blood Strike?",
                "opciones": [
                    "A) La hora del día para jugar",
                    "B) El momento exacto coordinado para que el equipo avance al mismo tiempo",
                    "C) Pushear solo cuando quieras",
                    "D) Esperar a que el rival venga",
                ],
                "correcta": 1,
                "explicacion": "Timing = coordinación. Todos entran al mismo momento para abrumar al rival. Si uno entra solo, muere.",
            },
        ],
        2: [  # Plata
            {
                "pregunta": "El rival siempre defiende desde el mismo ángulo en Puerto. ¿Qué haces?",
                "opciones": [
                    "A) Seguir atacando al mismo punto — con más jugadores",
                    "B) Flanquear desde el almacén para romper su posición",
                    "C) Rendirte en esa ronda",
                    "D) Esperar 2 minutos sin moverte",
                ],
                "correcta": 1,
                "explicacion": "El IGL lee patrones del rival y usa flanqueos para romper holds repetitivos. Creatividad táctica.",
            },
            {
                "pregunta": "¿Qué es una 'rotación' en términos tácticos?",
                "opciones": [
                    "A) Girar el cuerpo en círculo",
                    "B) Mover a jugadores de una zona a otra para responder a amenazas",
                    "C) Cambiar de arma durante la partida",
                    "D) Repetir la misma táctica varias veces",
                ],
                "correcta": 1,
                "explicacion": "Rotar = mover recursos humanos del mapa donde no son necesarios a donde sí lo son. Clave táctica.",
            },
            {
                "pregunta": "¿Cuándo debes usar un humo como IGL?",
                "opciones": [
                    "A) Al azar para confundir",
                    "B) Para tapar la visión del rival en zonas clave antes de cruzar o entrar",
                    "C) Solo al final de la ronda",
                    "D) Nunca, son inútiles",
                ],
                "correcta": 1,
                "explicacion": "Los humos tapan líneas de visión enemigas. El IGL decide cuándo y dónde se usan para maximizar su efecto.",
            },
        ],
        3: [  # Oro
            {
                "pregunta": "Tu ancla cayó y quedan 3 vs 4. El rival tiene posición ventajosa en Aldea. ¿Qué haces?",
                "opciones": [
                    "A) Rush todos juntos al frente",
                    "B) Forzar split del rival: uno distrae, dos flanquean",
                    "C) Rendirse la ronda",
                    "D) Esperar pasivo a que entren",
                ],
                "correcta": 1,
                "explicacion": "Con desventaja numérica, dividir atención del rival es la mejor opción. El distractor sacrifica tiempo para que los otros flaqueen.",
            },
            {
                "pregunta": "¿Qué es el 'mid-game reset' y cuándo lo aplicas?",
                "opciones": [
                    "A) Reiniciar el juego",
                    "B) Replantear la estrategia a la mitad de la partida cuando el plan A falló",
                    "C) Cambiar de equipo",
                    "D) Pausar indefinidamente",
                ],
                "correcta": 1,
                "explicacion": "El reset táctica ocurre cuando el plan inicial no funciona. El IGL debe adaptarse sin entrar en pánico.",
            },
        ],
        4: [  # Diamante
            {
                "pregunta": "El rival tiene IGL muy pasivo en Desierto — espera siempre. ¿Cómo lo contrarrestas?",
                "opciones": [
                    "A) Ser igual de pasivo",
                    "B) Presión constante en múltiples flancos para forzar errores y rotaciones",
                    "C) Rush frontal masivo",
                    "D) No hacer nada durante 3 minutos",
                ],
                "correcta": 1,
                "explicacion": "Contra IGL pasivo: multi-pressure — hacer que roten, gastar utilidad, crear decisiones difíciles. Un hold es vulnerable si lo atacas desde varios ángulos.",
            },
        ],
        5: [  # Elite
            {
                "pregunta": "Estás en la final. Marcador 3-3. Última ronda en Puerto. Tienes ventaja económica. ¿Qué compras?",
                "opciones": [
                    "A) Cada uno compra lo que quiera",
                    "B) Coordinas: entry con SMG+Flash, soporte con SKS, ancla con AK47+Alambrada, IGL con M4+Humos",
                    "C) Todos van con francotirador",
                    "D) Ahorras el dinero",
                ],
                "correcta": 1,
                "explicacion": "La gestión económica coordinada en rondas decisivas es lo que separa al IGL elite del amateur. Cada rol compra lo que su función requiere.",
            },
        ],
    },

    "Fragger": {
        1: [  # Bronce
            {
                "pregunta": "¿Cuál es el objetivo principal del Fragger en Blood Strike?",
                "opciones": [
                    "A) Dar info y evitar confrontaciones",
                    "B) Eliminar enemigos agresivamente y abrir espacio para el equipo",
                    "C) Defender el punto B siempre",
                    "D) Usar solo francotiradores",
                ],
                "correcta": 1,
                "explicacion": "El Fragger es el principal eliminador. Su rol es abrir entradas con kills rápidos y limpios.",
            },
            {
                "pregunta": "¿Qué arma es más efectiva para el Fragger en corta distancia?",
                "opciones": [
                    "A) Kar98k (francotirador)",
                    "B) SMG (subfusil) como MP5 o PP-19",
                    "C) DMR (rifle de tirador)",
                    "D) Pistola básica",
                ],
                "correcta": 1,
                "explicacion": "SMG domina en corta distancia por su DPS alto y velocidad de fuego. El Fragger vive en rangos cortos.",
            },
            {
                "pregunta": "¿Qué es 'peekear' un ángulo?",
                "opciones": [
                    "A) Quedarse quieto detrás de cover",
                    "B) Salir brevemente de cobertura para ver o disparar y volver",
                    "C) Correr sin disparar",
                    "D) Saltar continuamente",
                ],
                "correcta": 1,
                "explicacion": "Peek = salida controlada de cover para tomar el duelo. El Fragger debe dominar el peek agresivo.",
            },
        ],
        2: [  # Plata
            {
                "pregunta": "El rival está detrás de una caja en Aldea. ¿Cuál es el mejor approach?",
                "opciones": [
                    "A) Dispararle a la caja hasta que muera",
                    "B) Flanquear para cambiar el ángulo y forzar que se mueva",
                    "C) Lanzar todas las granadas a la vez",
                    "D) Esperar que salga solo",
                ],
                "correcta": 1,
                "explicacion": "El Fragger inteligente no se queda en el mismo ángulo. Flanquear fuerza al rival a reposicionarse — exponiéndose.",
            },
            {
                "pregunta": "¿Qué es el 'strafe shooting' (shoot-strafe)?",
                "opciones": [
                    "A) Disparar parado sin moverse",
                    "B) Disparar mientras te mueves lateralmente para ser más difícil de impactar",
                    "C) Disparar hacia arriba",
                    "D) Disparar solo con pistola",
                ],
                "correcta": 1,
                "explicacion": "Strafe shooting = disparar+moverse lateralmente. El fragger que se mueve es más difícil de matar.",
            },
        ],
        3: [  # Oro
            {
                "pregunta": "Vas a entrar a una habitación cerrada en Puerto. ¿Cuál es el protocolo correcto?",
                "opciones": [
                    "A) Entrar directo al centro",
                    "B) Flash/Granada primero, luego entrar pegado a la pared y limpiar ángulos",
                    "C) Lanzar todo y esperar afuera",
                    "D) Pedir que entre otro primero",
                ],
                "correcta": 1,
                "explicacion": "Protocolo de room-clear: utilidad primero (flash/frag), luego entrada pegada a pared, limpiar ángulos esquina por esquina.",
            },
        ],
        4: [
            {
                "pregunta": "Estás 1vs1 con el IGL enemigo. Él es muy pasivo. ¿Cómo ganas el duelo?",
                "opciones": [
                    "A) Esperar que salga",
                    "B) Jiggle peek para obtener info, luego peek agresivo cuando sabes su posición exacta",
                    "C) Rush recto sin cover",
                    "D) Usar sniper aunque estés en corta",
                ],
                "correcta": 1,
                "explicacion": "Jiggle peek = peek rápido para ver sin morir, obtienes info de posición, luego el peek definitivo con ventaja de info.",
            },
        ],
        5: [
            {
                "pregunta": "Tu equipo necesita que abras site A en Desierto. Hay 2 rivales defendiendo. ¿Cuál es tu secuencia?",
                "opciones": [
                    "A) Rush solo inmediatamente",
                    "B) Coordinás con IGL: humo del IGL cubre ángulo derecho, flasheas el izquierdo, entras por la roca central y limpias primero al que esté más expuesto",
                    "C) Pides a otro que entre primero",
                    "D) Disparas desde lejos sin entrar",
                ],
                "correcta": 1,
                "explicacion": "El Fragger elite trabaja en sintonía con el equipo. Utilidad + timing + ángulo de entrada = entry limpio con alta probabilidad de sobrevivir.",
            },
        ],
    },

    "Ancla": {
        1: [
            {
                "pregunta": "¿Cuál es la función principal del Ancla?",
                "opciones": [
                    "A) Rush constantemente",
                    "B) Mantener posición defensiva clave y sostenerla bajo presión",
                    "C) Dar info y moverse mucho",
                    "D) Curar a todos",
                ],
                "correcta": 1,
                "explicacion": "El Ancla es el eje defensivo — su job es no ceder terreno y ganar los duelos en su zona asignada.",
            },
            {
                "pregunta": "¿Qué tipo de arma es más eficiente para el Ancla que defiende zona cerrada?",
                "opciones": [
                    "A) Sniper de largo alcance",
                    "B) SMG para CQB + AR como respaldo",
                    "C) Solo pistola",
                    "D) Solo granada",
                ],
                "correcta": 1,
                "explicacion": "El Ancla en zona cerrada necesita DPS alto en corta (SMG) y un AR de respaldo para si el enemigo se mantiene a media distancia.",
            },
        ],
        2: [
            {
                "pregunta": "Te están flanqueando desde dos lados simultáneamente. Eres el Ancla. ¿Qué haces?",
                "opciones": [
                    "A) Intentar matar a los dos a la vez",
                    "B) Comunicar al equipo, retroceder a posición más segura y esperar apoyo",
                    "C) Ignorar un flanco",
                    "D) Salir corriendo",
                ],
                "correcta": 1,
                "explicacion": "El Ancla inteligente no muere por orgullo. Ceder un metro para sobrevivir y avisar al equipo vale más que un kill doble imposible.",
            },
        ],
        3: [
            {
                "pregunta": "¿Qué es el 'crouch spam' y cuándo lo usa el Ancla?",
                "opciones": [
                    "A) Agacharse repetidamente al disparar para hacer el hitbox más impredecible",
                    "B) Solo agacharse para esconderse",
                    "C) Correr agachado",
                    "D) Saltar y agacharse",
                ],
                "correcta": 0,
                "explicacion": "Crouch spam = bajar/subir rápido durante el duelo. El hitbox cambia y hace más difícil impactar al Ancla. Técnica defensiva avanzada.",
            },
        ],
    },

    "Soporte Media y Larga": {
        1: [
            {
                "pregunta": "¿Cuál es la prioridad del Soporte Media y Larga?",
                "opciones": [
                    "A) Estar siempre al frente",
                    "B) Dar cobertura al equipo desde posiciones seguras y curar si es posible",
                    "C) Solo disparar y nunca moverse",
                    "D) Usar solo SMG",
                ],
                "correcta": 1,
                "explicacion": "El Soporte cubre, protege y mantiene vivo al equipo. Su posición segura le da visión y líneas de fuego largas.",
            },
            {
                "pregunta": "¿Qué es el 'centering' en shooting?",
                "opciones": [
                    "A) Estar en el centro del mapa",
                    "B) Mantener el crosshair a altura de cabeza del enemigo en todo momento",
                    "C) Disparar al centro del pecho",
                    "D) Apuntar al piso",
                ],
                "correcta": 1,
                "explicacion": "Centering = crosshair placement. Si tu mira siempre está a altura de cabeza, el ajuste para impactar es mínimo = más headshots naturales.",
            },
        ],
        2: [
            {
                "pregunta": "¿Qué arma usa el Soporte Media en Blood Strike?",
                "opciones": [
                    "A) Solo SMG",
                    "B) DMR como SKS o AR como M4A1/SCAR para media distancia",
                    "C) Solo escopeta",
                    "D) Solo pistola",
                ],
                "correcta": 1,
                "explicacion": "Para media distancia el SKS (DMR) y el M4A1 (AR) son ideales. Alto daño sostenido y control para cubrir a los fraggers.",
            },
        ],
        3: [
            {
                "pregunta": "¿Cómo ayuda el Soporte Larga a un push de site?",
                "opciones": [
                    "A) Entra primero al site",
                    "B) Cubre desde posición elevada o lejana, suprimiendo a defenders para que el fragger entre seguro",
                    "C) Espera que acabe todo",
                    "D) Lanza granadas al azar",
                ],
                "correcta": 1,
                "explicacion": "El Soporte Larga suprime = mantiene al defensor agachado o en cover, creando el espacio para que el Fragger entre con menor riesgo.",
            },
        ],
    },

    "Mapas": {
        "Aldea": {
            1: [
                {
                    "pregunta": "¿Cuál es la zona de control más importante en Aldea?",
                    "opciones": [
                        "A) La esquina noreste sin importancia",
                        "B) El mercado central — quien lo controla dicta el flujo de la ronda",
                        "C) Las afueras del mapa",
                        "D) El punto de spawn",
                    ],
                    "correcta": 1,
                    "explicacion": "El mercado central de Aldea es el hub táctico. Control aquí = info de todos los flancos y ventaja posicional total.",
                },
                {
                    "pregunta": "Un rival campea en el edificio alto norte de Aldea. ¿Cómo lo sacas?",
                    "opciones": [
                        "A) Rush directo por la escalera",
                        "B) Flanquear por callejón trasero + humo para tapar su línea de visión",
                        "C) Ignorarlo y atacar otro lado",
                        "D) Esperar a que baje",
                    ],
                    "correcta": 1,
                    "explicacion": "El jugador en altura tiene ventaja de ángulo. Humo en su línea de visión + flanqueo por donde no puede ver = eliminación limpia.",
                },
            ],
        },
        "Desierto": {
            1: [
                {
                    "pregunta": "¿Por qué la Roca Central en Desierto es tan valiosa?",
                    "opciones": [
                        "A) Es bonita visualmente",
                        "B) Da cover elevado y visión de múltiples rutas del mapa",
                        "C) No tiene ningún valor táctico",
                        "D) Es el punto de respawn",
                    ],
                    "correcta": 1,
                    "explicacion": "La Roca Central en Desierto es control de mapa — da height advantage y visión 270°. Quien la controla domina el ritmo.",
                },
            ],
        },
        "Puerto": {
            1: [
                {
                    "pregunta": "¿Cuál es la mayor amenaza táctica en el mapa Puerto?",
                    "opciones": [
                        "A) El agua de fondo",
                        "B) Los flancos entre contenedores — son múltiples y difíciles de controlar",
                        "C) El muelle es demasiado corto",
                        "D) No hay flancos en Puerto",
                    ],
                    "correcta": 1,
                    "explicacion": "Puerto tiene múltiples ángulos de flanqueo entre contenedores. El equipo que no controla flancos pierde posición constantemente.",
                },
            ],
        },
    },
}

NIVELES_RANKING = {
    0:    "🥉 Bronce",
    200:  "🥈 Plata",
    500:  "🥇 Oro",
    900:  "💎 Diamante",
    1400: "⭐ Elite",
}

PUNTOS_POR_RESPUESTA = 25
BONUS_RACHA = {3: 10, 5: 25, 7: 50}  # Racha de respuestas correctas → bonus
