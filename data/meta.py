"""
data/meta.py — META real Blood Strike | Parche 10/02/2026
Armas con nombres reales del juego
Utilidades reales: Granada, Flash, Molotov, Humo, Granada Adhesiva
Strikers con habilidades reales
"""

META_ARMAS = {
    "SMG": [
        {"nombre": "MP5", "tier": "S", "uso": "CQB / Rush", "ventajas": "DPS más alto en corta distancia del juego, muy manejable", "contras": "Inútil a media-larga distancia", "accesorios_meta": ["Cañón largo", "Cargador extendido", "Punto rojo"], "nota_parche": "Pilar del meta CQB"},
        {"nombre": "MP7", "tier": "S", "uso": "Corta-media / Rush agresivo", "ventajas": "BUFF: +1 daño en todo el cuerpo, mejor precisión sin apuntar. Disponible en suelo TCT", "contras": "Cargador pequeño base", "accesorios_meta": ["Gatillo pesado", "Cargador extendido", "Holográfica"], "nota_parche": "🔺 BUFFED 29/01/2026"},
        {"nombre": "Bizon (PP-19)", "tier": "A", "uso": "Rush / Supresión continua", "ventajas": "Cargador enorme, alta movilidad, fuego supresivo sin recargar frecuente", "contras": "Daño por bala moderado", "accesorios_meta": ["Cargador extendido", "Holográfica"], "nota_parche": "🆕 NUEVO diciembre 2025"},
        {"nombre": "P90", "tier": "A", "uso": "Supresión / CQB", "ventajas": "BUFF: Perno de ráfaga de 5 ya no reduce alcance. 50 balas en cargador base", "contras": "Daño por bala bajo", "accesorios_meta": ["Perno ráfaga 5 (BAS)", "Cargador extendido"], "nota_parche": "🔺 BUFFED 29/01/2026"},
        {"nombre": "UMP45", "tier": "B", "uso": "Corta-media versátil", "ventajas": "Control fácil, bueno para aprender SMG", "contras": "Eclipsado por MP7 y MP5 tras últimos buffs", "accesorios_meta": ["Supresor", "Empuñadura delantera"], "nota_parche": "Sin cambios"},
    ],
    "AR": [
        {"nombre": "HK416", "tier": "S", "uso": "Corta-media / Todo terreno agresivo", "ventajas": "NUEVO: alta cadencia + movilidad. Culata retráctil BAS Tipo C elimina retraso correr/disparar", "contras": "Nuevo — poca data competitiva aún", "accesorios_meta": ["Culata retráctil BAS Tipo C", "Cargador extendido", "Mira 2x"], "nota_parche": "🆕 NUEVO 15/02/2026 — meta inmediato"},
        {"nombre": "M4A1", "tier": "S", "uso": "Media distancia / Todo terreno", "ventajas": "El arma más equilibrada. Cualquier rol la puede usar con efectividad", "contras": "No brilla en ningún extremo", "accesorios_meta": ["Cañón largo", "Empuñadura delantera", "Mira 2x", "Cargador extendido"], "nota_parche": "Pilar eterno del meta"},
        {"nombre": "FN2000", "tier": "A", "uso": "Media distancia", "ventajas": "BUFF: +1 daño pecho, abdomen y cabeza", "contras": "Diseño poco intuitivo para nuevos jugadores", "accesorios_meta": ["Empuñadura delantera", "Mira 2x", "Cargador extendido"], "nota_parche": "🔺 BUFFED 29/01/2026"},
        {"nombre": "AR97", "tier": "A", "uso": "Media-larga distancia", "ventajas": "BUFF DOBLE: mayor cadencia + retroceso muy reducido. Ahora viable en larga distancia", "contras": "Requiere adaptarse a la nueva cadencia post-buff", "accesorios_meta": ["Mira 4x", "Empuñadura delantera", "Cañón largo"], "nota_parche": "🔺 BUFFED 29/01/2026"},
        {"nombre": "AK-47", "tier": "A", "uso": "Media-larga / Alto daño", "ventajas": "Mayor daño por bala que M4A1, excelente para soporte media", "contras": "Recoil vertical duro de dominar", "accesorios_meta": ["Empuñadura trasera", "Empuñadura delantera", "Mira 2x"], "nota_parche": "Sin cambios"},
        {"nombre": "RPK", "tier": "B", "uso": "Supresión / Hold defensivo", "ventajas": "Cargador enorme, ideal para suprimir posiciones largas", "contras": "NERF: daño bajó 29→27 en pecho y abdomen, supresión reducida", "accesorios_meta": ["Bípode", "Mira 3x", "Cargador extendido"], "nota_parche": "🔻 NERFED 29/01/2026"},
    ],
    "Francotirador": [
        {"nombre": "Kar98k", "tier": "S", "uso": "Larga distancia / One-shot cabeza", "ventajas": "One-shot a la cabeza, ícono del meta competitivo", "contras": "Solo jugadores con aim preciso lo aprovechan", "accesorios_meta": ["Mira 8x", "Cañón largo", "Bípode"], "nota_parche": "Pilar del meta competitivo"},
        {"nombre": "M82", "tier": "A", "uso": "Larga / Anti-material", "ventajas": "Ahora disponible como arma de suelo en TCT. Daño masivo por disparo", "contras": "Cadencia muy baja — una oportunidad por disparo", "accesorios_meta": ["Mira 8x", "Bípode"], "nota_parche": "🆕 Añadido suelo TCT 10/02/2026"},
        {"nombre": "M700", "tier": "A", "uso": "Larga distancia / Aprendizaje sniper", "ventajas": "Mayor cadencia que Kar98k, más fácil para aprender sniper", "contras": "One-shot menos consistente que Kar98k", "accesorios_meta": ["Mira 6x", "Cañón largo"], "nota_parche": "Sin cambios"},
    ],
    "DMR": [
        {"nombre": "AR97 (modo DMR)", "tier": "S", "uso": "Media-larga / Semi-auto", "ventajas": "Post-buff es el DMR más versátil. Cadencia alta para un DMR", "contras": "Requiere precisión — no es spray and pray", "accesorios_meta": ["Mira 4x", "Empuñadura delantera", "Cargador extendido"], "nota_parche": "🔺 BUFFED 29/01/2026"},
        {"nombre": "VSS", "tier": "A", "uso": "Media / Semi-silencioso", "ventajas": "BUFF: +10 balas en TODOS los cargadores. Disparo semi-silencioso", "contras": "Cargador era muy pequeño base — ahora más viable", "accesorios_meta": ["Mira 4x", "Cargador extendido"], "nota_parche": "🔺 BUFFED 29/01/2026"},
        {"nombre": "Spear", "tier": "A", "uso": "Media distancia / DMR ágil", "ventajas": "Disponible como arma de suelo en TCT. Más ágil que otros DMR", "contras": "Poca data competitiva aún", "accesorios_meta": ["Mira 3x", "Cargador extendido"], "nota_parche": "🆕 Añadido suelo TCT 10/02/2026"},
    ],
    "Escopeta": [
        {"nombre": "M1887", "tier": "A", "uso": "CQB extremo", "ventajas": "Daño devastador en ultra-corta. Icónica del juego", "contras": "Una bala efectiva, pump muy lento, solo en CQB extremo", "accesorios_meta": ["Cañón modificado", "Culata"], "nota_parche": "Sin cambios recientes"},
        {"nombre": "Origin-12", "tier": "A", "uso": "CQB / Semi-automática", "ventajas": "Semi-auto — más perdona que M1887. Ideal para Isla Siniestra", "contras": "Solo efectiva en ultra-corta distancia", "accesorios_meta": ["Cañón corto", "Cargador extendido"], "nota_parche": "Sólida para CQB cerrado"},
    ],
}

# Utilidades REALES de Blood Strike — NO hay minas ni alambradas
META_UTILIDADES = {
    "Granada": {
        "descripcion": "Granada de fragmentación — daño de área al explotar",
        "uso": "Lanzar a zona abierta, forzar salida de cover, limpiar habitaciones",
        "tip": "Rebotar en paredes para llegar a covers imposibles de lanzar directo",
    },
    "Flash": {
        "descripcion": "Granada de destello — ciega temporalmente a todos en radio",
        "uso": "Cegar rivales antes de entrar a un cuarto o hacer rush",
        "tip": "Lanzar hacia arriba y dejar que caiga — da tiempo a posicionarse. No mirarlo propio",
    },
    "Molotov": {
        "descripcion": "Cóctel molotov — crea zona de fuego con daño continuo",
        "uso": "Bloquear entradas, forzar movimiento de un cover, control de zona",
        "tip": "Ideal para forzar al rival que hace hold — el fuego obliga a moverse o morir",
    },
    "Humo": {
        "descripcion": "Granada de humo — crea cortina de humo que bloquea visión",
        "uso": "Cruzar zonas abiertas, tapar ángulos de francotirador, crear cover visual",
        "tip": "Colocar entre tú y el rival — no entre tú y tu equipo",
    },
    "Granada Adhesiva": {
        "descripcion": "Granada que se pega a superficies antes de explotar",
        "uso": "Pegar en cover para precisión, controlar entradas específicas, sorprender en corners",
        "tip": "Más precisa que la normal para corners y covers. Se pega en paredes y suelo",
    },
}

# Strikers con habilidades reales
STRIKERS_BLOODSTRIKE = {
    "VOLT": {
        "habilidad_activa": "Escudo de energía — proyecta un escudo temporal que absorbe daño frontal",
        "habilidad_pasiva": "Mayor resistencia al daño de zona (explosivos, fuego)",
        "estilo": "Tank / Defensa",
        "mejor_en": "Hold defensivo, ancla, aguantar presión",
        "sinergias": "Bueno con cualquier arma de media distancia en posición defensiva",
    },
    "NACHO": {
        "habilidad_activa": "Granada de señuelo — crea ruido de pasos falsos para confundir al rival",
        "habilidad_pasiva": "Movimiento más silencioso — los rivales escuchan menos sus pasos",
        "estilo": "Engaño / Flanqueo",
        "mejor_en": "Flanqueo sorpresa, confundir al rival, posiciones de info",
        "sinergias": "MP5 o MP7 — llega silencioso y elimina rápido",
    },
    "RAN": {
        "habilidad_activa": "Dash de velocidad — movimiento rápido en una dirección para esquivar o reposicionarse",
        "habilidad_pasiva": "Mayor velocidad de movimiento base",
        "estilo": "Velocidad / Movilidad",
        "mejor_en": "Rush agresivo, entry fragger, Isla Siniestra",
        "sinergias": "MP5, MP7 o HK416 — velocidad + DPS",
    },
    "ZERO": {
        "habilidad_activa": "EMP — desactiva temporalmente las habilidades activas de los Strikers rivales en radio",
        "habilidad_pasiva": "Mayor resistencia a efectos de habilidades enemigas",
        "estilo": "Anti-habilidad / Control",
        "mejor_en": "Contrarrestar equipos con Strikers de habilidades fuertes",
        "sinergias": "M4A1 — neutraliza ventajas rivales y pelea en territorio neutro",
    },
    "NOVA": {
        "habilidad_activa": "Escaneo de área — revela la posición de rivales en un radio por varios segundos",
        "habilidad_pasiva": "Mayor duración de humos propios",
        "estilo": "Info / Soporte",
        "mejor_en": "IGL, dar info al equipo, push con información",
        "sinergias": "Cualquier arma — su valor es la información que da al equipo",
    },
    "EMMA": {
        "habilidad_activa": "Curación de área — cura a todos los aliados cercanos por varios segundos",
        "habilidad_pasiva": "Regeneración de salud más rápida",
        "estilo": "Soporte / Curación",
        "mejor_en": "Soporte de equipo, hold prolongado, scrims largos",
        "sinergias": "AR97 o FN2000 — cura al equipo mientras da supresión de media",
    },
    "SPIKE": {
        "habilidad_activa": "Barrera de pinchos — despliega barrera que daña y ralentiza a rivales que pasan",
        "habilidad_pasiva": "Mayor daño con armas cuerpo a cuerpo",
        "estilo": "Control de zona / Defensa agresiva",
        "mejor_en": "Ancla, bloquear rutas de rush, hold de puntos",
        "sinergias": "M4A1 o FN2000 — bloquea ruta y cubre desde distancia media",
    },
    "BLAST": {
        "habilidad_activa": "Explosión de impulso — salta a gran altura para reposicionarse en posición elevada",
        "habilidad_pasiva": "Mayor resistencia a daño de caída",
        "estilo": "Movilidad vertical / Sorpresa",
        "mejor_en": "Tomar posiciones elevadas inesperadas, flanqueo vertical",
        "sinergias": "Kar98k o M82 — llega a posición elevada y snipea desde ángulo inesperado",
    },
    "LUCIAN": {
        "habilidad_activa": "Visión nocturna — ignora penalizaciones de visión (humos, oscuridad) temporalmente",
        "habilidad_pasiva": "Mayor precisión al disparar en movimiento",
        "estilo": "Precisión / Información bajo cobertura",
        "mejor_en": "Combate en humo, peek agresivo, duelos en movimiento",
        "sinergias": "MP7 o HK416 — dispara en movimiento con mayor precisión",
    },
    "KRAKEN": {
        "habilidad_activa": "Gancho de agarre — se lanza hacia una superficie o rival para acortar distancia rápidamente",
        "habilidad_pasiva": "Mayor velocidad al escalar y saltar",
        "estilo": "Movilidad extrema / Entry agresivo",
        "mejor_en": "Entry fragger, sorprender desde ángulos imposibles, Isla Siniestra",
        "sinergias": "MP5 o MP7 — llega en un segundo y elimina antes de que reaccionen",
    },
    "JACK": {
        "habilidad_activa": "Señuelo holográfico — despliega un señuelo que simula ser un Striker para atraer fuego",
        "habilidad_pasiva": "Menor tiempo de revive a aliados",
        "estilo": "Engaño / Soporte",
        "mejor_en": "Confundir al rival, crear oportunidades para el equipo, salvar aliados",
        "sinergias": "M4A1 — lanza señuelo, rival dispara, tú pegas",
    },
    "ETHAN": {
        "habilidad_activa": "Escáner de huella — detecta la posición de rivales que pisaron la zona recientemente",
        "habilidad_pasiva": "Escucha pasos de rivales desde mayor distancia",
        "estilo": "Info / Rastreo",
        "mejor_en": "Leer rotaciones del rival, anticipar flanqueos, IGL con info extra",
        "sinergias": "AR97 o FN2000 — la info de ETHAN dicta cuándo y desde dónde pelear",
    },
    "JET": {
        "habilidad_activa": "Propulsores — vuelo breve en línea recta para cruzar zonas o reposicionarse",
        "habilidad_pasiva": "Caídas largas sin daño",
        "estilo": "Movilidad aérea / Sorpresa",
        "mejor_en": "Cruzar zonas abiertas rápido, tomar posiciones elevadas, flanqueo aéreo",
        "sinergias": "MP5 o HK416 — llega volando y limpia antes de que reaccionen",
    },
}

# Combinaciones de Strikers por estilo de juego
COMBINACIONES_STRIKERS = {
    "Full Rush 🔴": {
        "descripcion": "Máxima agresividad y movilidad. Entrar rápido, limpiar antes de que se reorganicen.",
        "strikers": ["RAN (velocidad — entry fragger)", "KRAKEN (gancho — llega primero)", "JET (vuelo — flanqueo aéreo)", "LUCIAN (dispara en movimiento)"],
        "armas": ["MP5 o MP7 (entry y fragger)", "HK416 con BAS (IGL/apoyo)", "MP7 (support rush)"],
        "utilidades": ["Flash antes de entrar", "Humo para cubrir el cruce inicial"],
        "estrategia": "RAN lidera el rush con velocidad. KRAKEN flanquea por el lado inesperado con su gancho. JET vuela sobre la posición rival. LUCIAN cubre disparando en movimiento. Flash antes de cada entrada. Todos mueven al mismo tiempo — el timing del IGL es todo.",
        "mejor_en": "Prisión (Isla Siniestra), Skyline City (Playa Cielo), Missile Basement (Valle Abandonado)",
        "debilidad": "Si el rival tiene setup defensivo sólido o los tiempos no están coordinados, el rush puede colapsar",
    },
    "Full Defensivo 🔵": {
        "descripcion": "Control total de zona. Forzar al rival a entrar a nuestro terreno y destruirlo.",
        "strikers": ["VOLT (escudo — aguanta presión)", "SPIKE (barrera de pinchos — bloquea entradas)", "EMMA (curación — sostiene hold largo)", "ZERO (EMP — neutraliza habilidades ofensivas del rival)"],
        "armas": ["M4A1 (hold principal)", "AR97 con mira 4x (supresión desde distancia)", "M82 o Kar98k (soporte larga cubre rutas abiertas)"],
        "utilidades": ["Molotov en entradas", "Granada Adhesiva en corners de flanqueo", "Humo para tapar línea de visión del francotirador rival"],
        "estrategia": "SPIKE bloquea la entrada principal con su barrera. VOLT absorbe el primer rush con su escudo. EMMA cura al equipo durante el hold. ZERO neutraliza las habilidades del equipo rival cuando intentan entrar. Molotov en entradas = el rival no puede entrar sin tomar daño. NO salir — que entren a nuestro setup.",
        "mejor_en": "Rocket Base (Valle Abandonado), Sala de Calderas (Isla Siniestra), Hospital (Playa Cielo)",
        "debilidad": "Si el rival no cae en el setup y hace rotación de mapa, puede quedar la defensa en mal ángulo",
    },
    "Rush + Defensivo ⚡": {
        "descripcion": "Atacar un lado mientras se defiende el otro. El estilo más profesional y difícil de leer.",
        "strikers": ["NOVA (escaneo — da info de ambos lados)", "RAN (rush por un flanco)", "VOLT (hold del otro flanco)", "EMMA (soporte que cura a quien lo necesite)"],
        "armas": ["MP5/MP7 (flanco rush)", "M4A1 (flanco defensivo)", "AR97 (soporte cubre ambos lados)"],
        "utilidades": ["Humo en la ruta de rush", "Molotov en la entrada defensiva", "Flash para el entry del flanco agresivo"],
        "estrategia": "NOVA escanea para saber cuántos rivales están en cada lado. Con esa info: RAN rushea el flanco donde hay menos rivales. VOLT holdea el flanco principal. EMMA rota a quien esté bajo presión. El IGL dicta cuándo convertir el hold en push o el rush en hold según la info de NOVA.",
        "mejor_en": "Valle Abandonado (mapa grande con múltiples rutas), Playa Cielo (rotaciones complejas)",
        "debilidad": "Requiere comunicación perfecta — si el equipo no coordina, los dos flancos pueden colapsar al mismo tiempo",
    },
    "Full Tank 🟡": {
        "descripcion": "Aguantar daño masivo y avanzar lento pero seguro. El rival gasta recursos atacando y no elimina.",
        "strikers": ["VOLT (escudo frontal)", "EMMA (curación constante)", "SPIKE (barrera de cobertura)", "ZERO (neutraliza habilidades que rompan el tank)"],
        "armas": ["M4A1 (versátil para avance lento)", "RPK (supresión — aunque nerfed, el cargador enorme ayuda al avanzar)", "UMP45 (respaldo CQB)"],
        "utilidades": ["Humo para tapar francotiradores mientras avanza el grupo", "Granada para limpiar covers antes de avanzar", "Molotov para forzar reposición rival"],
        "estrategia": "VOLT va adelante con escudo. EMMA cura constantemente al equipo desde atrás. SPIKE despliega barrera en cada zona que toman para no perderla. ZERO neutraliza cualquier habilidad que amenace el avance. Avance lento pero imparable — el rival gasta utilidades y no elimina. Humos constantes para tapar francotiradores. Ideal en modos donde mantener zona es prioritario.",
        "mejor_en": "TCT con objetivos de zona, Valle Abandonado (muchas coberturas para avanzar gradualmente)",
        "debilidad": "Muy lento — el rival puede rotar y flanquear. Un buen IGL rival puede leer el avance y preparar una emboscada",
    },
    "Info + Ejecución 🟣": {
        "descripcion": "Leer al rival completamente antes de actuar. El equipo con más info gana.",
        "strikers": ["NOVA (escaneo de área)", "ETHAN (rastrea posiciones recientes)", "NACHO (señuelo de sonido para ver reacciones)", "LUCIAN (combate bajo condiciones de visión reducida)"],
        "armas": ["M4A1 (versátil para ejecutar cualquier táctica)", "VSS (semi-silencioso — no revela posición fácilmente)", "MP7 (cuando la info confirma que es CQB)"],
        "utilidades": ["Humo para comprobar si el rival dispara (confirm info)", "Flash cuando la info confirma posición", "Granada Adhesiva en puntos de info"],
        "estrategia": "NOVA escanea para ubicar rivales. ETHAN rastrea si se movieron. NACHO lanza señuelo de sonido para ver la reacción del rival. Con 3 fuentes de info, el IGL ejecuta la táctica perfecta. LUCIAN combate en humos para confirmar info sin riesgo. Este estilo no improvisa — ejecuta con información completa.",
        "mejor_en": "TCT profesional, cualquier mapa",
        "debilidad": "Lento en gather de info — si el rival es muy agresivo puede no dar tiempo",
    },
}

COMBINACIONES_META = {
    "Rush Agresivo (BE)": {
        "descripcion": "Máxima agresividad. Entrar rápido y limpiar antes de que se reorganicen.",
        "armas": ["MP5 o MP7 (entry y fragger)", "HK416 con BAS Tipo C (IGL/apoyo)"],
        "utilidades": ["Flash antes de entrar + Humo para cubrir cruce inicial"],
        "estrategia": "IGL lanza humo en ángulo principal. Entry lanza Flash y entra inmediatamente con MP5/MP7. Fragger sigue a 1 segundo. Ancla cubre retaguardia. Todos al mismo tiempo — timing del IGL es todo.",
        "modo": "BE",
        "mejor_en": "Prisión (Isla Siniestra), Skyline City (Playa Cielo)",
    },
    "Rush Coordinado (TCT)": {
        "descripcion": "Rush con utilidad completa. Más calculado que BE pero igual de agresivo.",
        "armas": ["M4A1 o HK416 (principal)", "MP7 (respaldo corta)", "AR97 (soporte cubre desde atrás)"],
        "utilidades": ["Humo en ángulo principal + Flash en entrada + Granada para limpiar cover"],
        "estrategia": "Soporte usa humo para tapar visión principal. IGL dicta timing. Flash hacia la entrada ciega defenders. Entry y fragger entran en split — uno distrae, otro limpia. AR97 del soporte suprime a quien intente cortar el push.",
        "modo": "TCT",
        "mejor_en": "Observation Deck (Valle Abandonado), Cultural Center (Playa Cielo)",
    },
    "Hold Defensivo": {
        "descripcion": "Aguantar zona bajo presión. Forzar al rival a entrar a nuestro terreno.",
        "armas": ["AK-47 o M4A1 (hold principal)", "AR97 con mira 4x (molesta desde distancia)", "MP5 (si entran a CQB)"],
        "utilidades": ["Molotov en entradas", "Granada Adhesiva en corners de flanqueo", "Humo para tapar línea de francotirador rival"],
        "estrategia": "Molotov en entrada ralentiza cualquier rush. Granada Adhesiva avisa y daña si flanquean. Ancla en el ángulo más fuerte. Soporte con AR97 molesta a quien intente posicionarse. NO salir a duelos — forzar al rival a entrar al setup.",
        "modo": "Ambos",
        "mejor_en": "Rocket Base (Valle Abandonado), Sala de Calderas (Isla Siniestra)",
    },
    "Control de Mapa (Info First)": {
        "descripcion": "Ganar con información antes que con aim. Estilo profesional.",
        "armas": ["M4A1 (versátil)", "VSS (semi-silencioso — no revela posición)", "MP7 (respaldo CQB)"],
        "utilidades": ["Humo para comprobar si el rival dispara (confirm info)", "Flash cuando la info confirma posición"],
        "estrategia": "NOVA o ETHAN dan info de posiciones. Con esa info, el equipo rota al lado menos defendido. Humos para cruzar zonas abiertas. VSS para molestar sin revelar posición. Este estilo gana por decisiones.",
        "modo": "TCT",
        "mejor_en": "Valle Abandonado (mapa grande), Playa Cielo (rotaciones complejas)",
    },
    "Anti-Rush": {
        "descripcion": "Destruir el rush enemigo antes de que entre.",
        "armas": ["MP5 o MP7 (duelos CQB)", "M1887 u Origin-12 (pasillos angostos)"],
        "utilidades": ["Flash lanzado HACIA donde entran para cegar al primer rushero", "Molotov en la entrada — deben entrar tomando daño", "Granada Adhesiva en el cover que usan al rushear"],
        "estrategia": "Molotov en la entrada obliga al rival a entrar tomando daño. Flash ciega al primer rushero. Ancla en ángulo ventajoso espera al rival ralentizado y cegado. Fragger hace counter-peek cuando el rival está en desventaja. Anticipación, no reacción.",
        "modo": "Ambos",
        "mejor_en": "Puerto (Isla Siniestra), Cargo Port (Playa Cielo)",
    },
}

MAPAS_BLOODSTRIKE = {
    "Valle Abandonado": {
        "nombre_ingles": "The Valley",
        "tipo": "Grande — Mix de todas las distancias",
        "descripcion": "El mapa más grande de Blood Strike. Zonas industriales, militares y naturales. Combina CQB en edificios con duelos de media-larga en zonas abiertas. La línea diagonal (Cliff Town → Rocket Base) divide el mapa en dos flancos.",
        "zonas_clave": {
            "Rocket Base": "Control sur — quien la tiene controla el acceso al Trade Zone",
            "Observation Deck": "Centro del mapa — altura y visión de múltiples rutas. Prioridad máxima",
            "Airforce Base": "Norte elevado — posiciones de francotirador y mucho loot",
            "Missile Basement": "CQB denso — pasillos cortos, dominio de SMG",
            "Sentry Camp": "Cruce central — rotación obligatoria entre norte y sur",
            "Bridge": "Paso obligado oeste — zona de emboscadas clásicas",
            "Sakura Valley": "Centro-sur — zona abierta, peligrosa sin cover",
            "Satellite Base": "Esquina suroeste — posición aislada para flanqueo sorpresa",
            "Trade Zone": "Sur — zona de loot y rotación",
            "Energy Station": "Noreste — control de zona con buenas posiciones",
        },
        "estrategia_ataque": "Tomar Observation Deck primero para visión completa. IGL decide norte (Airforce) o sur (Rocket Base). Humos para cruzar Sakura Valley. Split por ambos flancos obliga al rival a dividir defensa.",
        "estrategia_defensa": "Controlar Sentry Camp y Observation Deck como pivotes. Molotov en Bridge para cortar flanco oeste. Ancla en Missile Basement con MP5. Soporte larga en Airforce Base con Kar98k.",
        "mejor_arma": "M4A1 (versatilidad total), Kar98k (zonas abiertas), MP5 (edificios y Missile Basement)",
        "mejor_rol": "Todos los roles tienen valor — mapa más balanceado del juego",
        "peligro": "Sakura Valley muy expuesto, Bridge es trampa clásica, Satellite Base fácil de aislar",
    },
    "Playa Cielo": {
        "nombre_ingles": "Skyline Beach",
        "tipo": "Mediano — Urbano denso con combate vertical",
        "descripcion": "Mapa urbano y turístico. Calles amplias con edificios de varios pisos. Skyline City es el corazón — quien lo controla dicta el ritmo de todo el mapa. Mucho combate vertical (arriba/abajo de edificios).",
        "zonas_clave": {
            "Skyline City": "Centro absoluto — control aquí = control del mapa completo. Ángulos desde 4 direcciones",
            "Cultural Center": "Cruce norte-centro — zona de alto tráfico y rotaciones constantes",
            "Lighthouse": "Norte elevado — posición premium para Kar98k o M82",
            "Arena": "Este — duelos abiertos con múltiples ángulos peligrosos",
            "Hospital": "Este-centro — muchos cuartos, ideal para Ancla con SMG",
            "Yacht Club": "Noroeste — ruta de flanqueo sorpresa por el agua",
            "Cargo Port": "Suroeste — zona industrial con buen loot",
            "Institute": "Sur — zona de respawn frecuente, peligrosa al bajar",
        },
        "estrategia_ataque": "Tomar Cultural Center para partir el mapa. Entry limpia Skyline City con Flash + MP5/MP7. Soporte larga desde Lighthouse cubre con Kar98k. Un jugador flanquea por Yacht Club.",
        "estrategia_defensa": "Hold en Skyline City con Ancla. Molotov en Cultural Center para cortar acceso norte. Granada Adhesiva en Arena para alertar rotaciones. Soporte media en Hospital.",
        "mejor_arma": "HK416/M4A1 (urbano), MP7 (Skyline CQB), Kar98k (Lighthouse)",
        "mejor_rol": "Ancla (Skyline City), IGL (rotaciones complejas), Soporte Larga (Lighthouse)",
        "peligro": "Skyline City expone desde 4 direcciones, Arena tiene muchos ángulos, Institute es trampa al bajar",
    },
    "Isla Siniestra": {
        "nombre_ingles": "Shutter Island",
        "tipo": "Pequeño — CQB y media distancia exclusivamente",
        "descripcion": "Isla compacta rodeada de agua. No hay escapatoria — toda la pelea es en la isla. Distancias cortas y medias dominan completamente. Los francotiradores de larga distancia son inútiles aquí.",
        "zonas_clave": {
            "Prisión": "Centro absoluto — zona de máximo conflicto. Control = ventaja total del mapa",
            "Sala de Calderas": "Suroeste — industrial cerrada, CQB muy intenso",
            "Área Residencial": "Norte — edificios residenciales, muchos ángulos verticales",
            "Zona de Procesamiento": "Este — semiabierta, cuidado con flancos",
            "Puerto": "Sur — entrada principal, combate inicial intenso cada ronda",
            "Planta de Tratamiento de Agua": "Oeste — posición aislada, fácil de defender",
        },
        "estrategia_ataque": "Tomar Puerto rápido para cortar spawn sur. Rush a Prisión con Flash + MP5 — quien llega primero gana. Flanquear por Planta de Agua para sorprender en Sala de Calderas. Timing exacto — 1 segundo importa.",
        "estrategia_defensa": "Hold en Prisión con Ancla. Molotov en las dos entradas de Sala de Calderas. Granada Adhesiva en pasillo de Área Residencial → Prisión. Soporte media en Zona de Procesamiento con AR97.",
        "mejor_arma": "MP5/MP7 (CQB dominante), Origin-12 o M1887 (pasillos de Prisión), M4A1 (Zona de Procesamiento)",
        "mejor_rol": "Fragger (duelos constantes en isla pequeña), Ancla (Prisión), Entry (Puerto)",
        "peligro": "La isla no tiene escapatoria — si te rodean estás muerto. Prisión tiene ángulos verticales peligrosos",
    },
}
