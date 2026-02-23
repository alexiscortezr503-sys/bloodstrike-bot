"""
data/meta.py — META real Blood Strike | Parche 10/02/2026
Mapas reales: Valle Abandonado, Playa Cielo, Isla Siniestra
"""

META_ARMAS = {
    "SMG": [
        {"nombre": "MP5", "tier": "S", "uso": "CQB / Rush", "ventajas": "DPS altísimo, muy manejable", "contras": "Inútil a media-larga", "accesorios_meta": ["Cañón largo", "Cargador extendido", "Punto rojo"], "nota_parche": "Pilar del meta CQB"},
        {"nombre": "MP7", "tier": "S", "uso": "Corta-media / Rush agresivo", "ventajas": "BUFF: +1 daño todo el cuerpo, precisión sin apuntar mejorada. Disponible en suelo TCT", "contras": "Cargador pequeño base", "accesorios_meta": ["Gatillo pesado", "Cargador extendido", "Holográfica"], "nota_parche": "🔺 BUFFED 29/01/2026"},
        {"nombre": "PP-19 Bizon", "tier": "A", "uso": "Rush / Supresión continua", "ventajas": "Cargador enorme, alta movilidad, fuego supresivo sin parar", "contras": "Daño por bala moderado", "accesorios_meta": ["Cargador extendido", "Holográfica"], "nota_parche": "🆕 NUEVO diciembre 2025"},
        {"nombre": "P90", "tier": "A", "uso": "Supresión / CQB", "ventajas": "BUFF: Ráfaga 5 ya no reduce alcance. 50 balas en cargador", "contras": "Daño por bala bajo", "accesorios_meta": ["Perno ráfaga 5", "Cargador extendido"], "nota_parche": "🔺 BUFFED 29/01/2026"},
        {"nombre": "UMP45", "tier": "B", "uso": "Corta-media versátil", "ventajas": "Control fácil, bueno para aprender", "contras": "Eclipsado por MP7 y MP5", "accesorios_meta": ["Supresor", "Empuñadura delantera"], "nota_parche": "Sin cambios"},
    ],
    "AR": [
        {"nombre": "HK416", "tier": "S", "uso": "Corta-media / Todo terreno agresivo", "ventajas": "NUEVO: alta cadencia + movilidad, accesorio BAS elimina retraso correr/disparar", "contras": "Nuevo — poca data competitiva aún", "accesorios_meta": ["Culata retráctil BAS Tipo C", "Cargador extendido", "Mira 2x"], "nota_parche": "🆕 NUEVO 15/02/2026 — meta inmediato"},
        {"nombre": "M4A1", "tier": "S", "uso": "Media distancia / Todo terreno", "ventajas": "El arma más equilibrada del juego. Fácil control, cualquier rol la usa", "contras": "No brilla en ningún extremo", "accesorios_meta": ["Cañón largo", "Empuñadura delantera", "Mira 2x", "Cargador extendido"], "nota_parche": "Pilar eterno del meta"},
        {"nombre": "FN2000", "tier": "A", "uso": "Media distancia", "ventajas": "BUFF: +1 daño pecho, abdomen y cabeza", "contras": "Diseño poco intuitivo para nuevos", "accesorios_meta": ["Empuñadura delantera", "Mira 2x", "Cargador extendido"], "nota_parche": "🔺 BUFFED 29/01/2026"},
        {"nombre": "AR97", "tier": "A", "uso": "Media-larga distancia", "ventajas": "BUFF DOBLE: mayor cadencia + retroceso muy reducido. Ahora viable en larga", "contras": "Requiere aprender nueva cadencia post-buff", "accesorios_meta": ["Mira 4x", "Empuñadura delantera", "Cañón largo"], "nota_parche": "🔺 BUFFED 29/01/2026"},
        {"nombre": "AK-47", "tier": "A", "uso": "Media-larga / Alto daño", "ventajas": "Mayor daño por bala que M4, excelente soporte media", "contras": "Recoil vertical duro de dominar", "accesorios_meta": ["Empuñadura trasera", "Empuñadura delantera", "Mira 2x"], "nota_parche": "Sin cambios"},
        {"nombre": "RPK", "tier": "B", "uso": "Supresión / Hold defensivo", "ventajas": "Cargador enorme, ideal para suprimir posiciones", "contras": "NERF: daño bajó 29→27 pecho/abdomen, supresión reducida", "accesorios_meta": ["Bípode", "Mira 3x", "Cargador extendido"], "nota_parche": "🔻 NERFED 29/01/2026"},
    ],
    "Francotirador": [
        {"nombre": "Kar98k", "tier": "S", "uso": "Larga distancia / One-shot", "ventajas": "One-shot a la cabeza, ícono competitivo", "contras": "Solo jugadores experimentados lo usan bien", "accesorios_meta": ["Mira 8x", "Cañón largo", "Bípode"], "nota_parche": "Pilar del meta competitivo"},
        {"nombre": "M82", "tier": "A", "uso": "Larga / Anti-material", "ventajas": "Ahora disponible como arma de suelo en TCT. Daño masivo", "contras": "Cadencia muy baja", "accesorios_meta": ["Mira 8x", "Bípode"], "nota_parche": "🆕 Añadido suelo TCT 10/02/2026"},
        {"nombre": "M700", "tier": "A", "uso": "Larga distancia / Aprendizaje", "ventajas": "Mayor cadencia que Kar, mejor para aprender sniper", "contras": "One-shot menos consistente", "accesorios_meta": ["Mira 6x", "Cañón largo"], "nota_parche": "Sin cambios"},
    ],
    "DMR": [
        {"nombre": "SKS", "tier": "S", "uso": "Media-larga / Soporte perfecto", "ventajas": "Semi-automático, rey del rol soporte media. Ideal para Alejandro", "contras": "Requiere centering y tracking dominados", "accesorios_meta": ["Mira 4x", "Cargador extendido", "Empuñadura delantera"], "nota_parche": "Pilar del meta de soporte"},
        {"nombre": "Spear", "tier": "A", "uso": "Media distancia / DMR ágil", "ventajas": "Nuevo en suelo TCT, ágil para un DMR", "contras": "Poca data competitiva aún", "accesorios_meta": ["Mira 3x", "Cargador extendido"], "nota_parche": "🆕 Añadido suelo TCT 10/02/2026"},
    ],
    "Escopeta": [
        {"nombre": "Origin-12", "tier": "A", "uso": "CQB extremo / Semi-auto", "ventajas": "Semi-automática, más perdona que S1897. Ideal Isla Siniestra", "contras": "Solo efectiva en ultra-corta", "accesorios_meta": ["Cañón corto", "Cargador extendido"], "nota_parche": "Sólida para CQB cerrado"},
        {"nombre": "S1897", "tier": "B", "uso": "CQB / One-shot", "ventajas": "One-shot ultra corta, presión psicológica alta", "contras": "Una bala efectiva, pump lento", "accesorios_meta": ["Cañón modificado", "Culata"], "nota_parche": "Sin cambios"},
    ],
}

META_HABILIDADES = {
    "ofensivas": [
        {"nombre": "Granada de fragmentación", "uso": "Limpiar cover, forzar movimiento, daño de zona"},
        {"nombre": "Flash (Granada de destello)", "uso": "Cegar antes del rush — esencial para entry limpio"},
        {"nombre": "Cóctel molotov", "uso": "Bloquear paso, daño continuo, forzar salida de cover"},
        {"nombre": "Granada de humo", "uso": "Tapar visión, cruzar zonas abiertas, confusión táctica"},
    ],
    "defensivas": [
        {"nombre": "Alambrada de púas", "uso": "Ralentizar rush, alertar flanco, defender captura"},
        {"nombre": "Mina antipersona", "uso": "Proteger flanco trasero, trampa en corners y puertas"},
        {"nombre": "Barricada portátil", "uso": "Cover instantáneo en zona abierta"},
        {"nombre": "Sensor de movimiento", "uso": "Radar temporal — info de enemigos para el IGL"},
    ],
    "soporte": [
        {"nombre": "Kit médico de área", "uso": "Curar equipo en zona, sostener push prolongado"},
        {"nombre": "Revive rápido", "uso": "Levantar compañero sin detenerse — crítico en competitivo"},
        {"nombre": "Dron de reconocimiento", "uso": "Ver enemigos antes del push — info clave para IGL"},
        {"nombre": "Escudo balístico", "uso": "Proteger cruce de zona abierta"},
    ],
}

COMBINACIONES_META = {
    "Rush Agresivo (BE)": {
        "descripcion": "Máxima agresividad. Entrar rápido y limpiar antes de que se reorganicen.",
        "armas": ["MP5 o MP7 (entry)", "HK416 o M4A1 (IGL/fragger de apoyo)"],
        "habilidades": ["Flash → Humo (entry cegado con cobertura)", "Flash → Frag (entry + daño de zona)"],
        "estrategia": "IGL lanza humo en ángulo principal. Entry lanza flash y entra inmediatamente con SMG. Ancla cubre retaguardia. Soporte usa dron antes del push. Todos entran al mismo tiempo — el timing lo dicta el IGL.",
        "modo": "BE",
        "mejor_en": "Prisión (Isla Siniestra), Skyline City (Playa Cielo)",
    },
    "Rush Coordinado (TCT)": {
        "descripcion": "Rush con utilidad completa. Más lento pero más seguro.",
        "armas": ["M4A1 o HK416", "SKS (soporte cubre desde atrás)", "MP7 de respaldo"],
        "habilidades": ["Humo en ángulo principal + Alambrada en flanco", "Flash + Frag en entrada"],
        "estrategia": "Soporte usa dron para ubicar defenders. IGL dicta timing. Humo tapa visión principal. Alambrada asegura flanco. Entry y fragger entran en split — uno distrae, otro limpia. SKS suprime a quien intente cortar el push.",
        "modo": "TCT",
        "mejor_en": "Observation Deck (Valle Abandonado), Cultural Center (Playa Cielo)",
    },
    "Hold Defensivo": {
        "descripcion": "Aguantar zona bajo presión. Forzar al rival a entrar a nuestro terreno.",
        "armas": ["AK-47 o M4A1 (hold)", "SKS (molesta desde distancia)", "MP5 (CQB si entran)"],
        "habilidades": ["Alambrada en entradas + Mina en flanco", "Kit médico + Sensor de movimiento"],
        "estrategia": "Alambrada ralentiza rush. Mina avisa y daña si flanquean. Sensor da info al IGL. Ancla en el ángulo más fuerte. Soporte con SKS molesta a quien intente posicionarse. NO salir a duelos innecesarios — que el rival entre a nuestro setup.",
        "modo": "Ambos",
        "mejor_en": "Rocket Base (Valle Abandonado), Sala de Calderas (Isla Siniestra)",
    },
    "Control de Mapa (Info First)": {
        "descripcion": "Ganar con información antes que con aim. Estilo profesional.",
        "armas": ["M4A1", "SKS", "MP7 de respaldo"],
        "habilidades": ["Dron de reconocimiento (IGL)", "Sensor de movimiento + Humo"],
        "estrategia": "El IGL usa dron ANTES de cualquier movimiento para ubicar a los rivales. Con esa info, el equipo rota al lado menos defendido. Humo para cruzar zonas abiertas. Sensor en zona ya tomada para no perderla. Este estilo gana por decisiones, no por mecánicas.",
        "modo": "TCT",
        "mejor_en": "Valle Abandonado (mapa grande), Playa Cielo (rotaciones complejas)",
    },
    "Anti-Rush": {
        "descripcion": "Destruir el rush enemigo antes de que entre.",
        "armas": ["MP5 o MP7 (duelos CQB)", "Origin-12 (pasillos)"],
        "habilidades": ["Alambrada en entrada + Flash de contraataque", "Mina + Barricada"],
        "estrategia": "Alambrada en entrada principal ralentiza y avisa del rush. Ancla toma posición ventajosa con el aviso. Flash hacia el punto de entrada ciega al primer rushero. Fragger hace counter-peek cuando el rival está cegado y lento. Clave: anticipación, no reacción.",
        "modo": "Ambos",
        "mejor_en": "Puerto (Isla Siniestra), Cargo Port (Playa Cielo)",
    },
}

MAPAS_BLOODSTRIKE = {
    "Valle Abandonado": {
        "tipo": "Grande — Mix de distancias",
        "descripcion": "Mapa grande con zonas industriales, vegetación y estructuras militares. Combina CQB en edificios con duelos de media-larga en zonas abiertas. La línea diagonal (Cliff Town → Rocket Base) divide el mapa en dos flancos principales.",
        "zonas_clave": {
            "Rocket Base": "Control sur — quien la tiene controla el paso al Trade Zone",
            "Observation Deck": "Centro del mapa — altura y visión de múltiples rutas. Zona de control prioritaria",
            "Airforce Base": "Control norte — posiciones elevadas y mucho loot",
            "Missile Basement": "CQB denso — ideal para SMG y fraggers",
            "Sentry Camp": "Cruce central — punto de rotación obligatorio",
            "Bridge": "Paso obligado oeste — zona de emboscadas frecuentes",
            "Sakura Valley": "Centro-sur — zona abierta, peligrosa sin cobertura",
            "Satellite Base": "Esquina suroeste — posición aislada",
        },
        "estrategia_ataque": "Tomar Observation Deck primero para visión del mapa. Desde ahí, IGL decide si pushear norte (Airforce) o sur (Rocket Base). Usar humos para cruzar Sakura Valley. Split por ambos flancos obliga al rival a dividir su defensa.",
        "estrategia_defensa": "Controlar Sentry Camp y Observation Deck. Alambradas en Bridge para cortar flanco oeste. Ancla en Missile Basement con SMG. Soporte larga en Airforce Base con Kar98k/SKS.",
        "mejor_arma": "M4A1 (versatilidad), Kar98k (zonas abiertas), MP5 (edificios)",
        "mejor_rol": "Todos los roles tienen valor — mapa más balanceado",
        "peligro": "Sakura Valley muy expuesto, Bridge es trampa clásica",
    },
    "Playa Cielo": {
        "tipo": "Mediano — Urbano denso",
        "descripcion": "Mapa urbano y turístico. Calles amplias con edificios de varios pisos. Skyline City es el corazón — quien lo controla dicta el ritmo. Mucho combate vertical.",
        "zonas_clave": {
            "Skyline City": "Centro absoluto — control aquí = control del mapa completo",
            "Cultural Center": "Cruce norte-centro — zona de alto tráfico y rotaciones",
            "Lighthouse": "Norte elevado — posición de francotirador dominante",
            "Arena": "Este — duelos abiertos, múltiples ángulos peligrosos",
            "Hospital": "Este-centro — muchos cuartos, ideal para ancla",
            "Yacht Club": "Noroeste — flanqueo sorpresa por el agua",
            "Cargo Port": "Suroeste — zona industrial, buen loot",
            "Institute": "Sur — zona de respawn, cuidado al bajar",
        },
        "estrategia_ataque": "Tomar Cultural Center para partir el mapa. Entry limpia Skyline City con flash+SMG. Soporte larga desde Lighthouse cubre con SKS. Un jugador flanquea por Yacht Club para sorprender.",
        "estrategia_defensa": "Hold en Skyline City con ancla. Alambradas en Cultural Center. Sensor en Arena para detectar rotaciones. Soporte media en Hospital.",
        "mejor_arma": "HK416/M4A1 (urbano), MP7 (Skyline CQB), SKS (Lighthouse)",
        "mejor_rol": "Ancla (Skyline City), IGL (rotaciones complejas), Soporte Larga (Lighthouse)",
        "peligro": "Skyline City tiene ángulos desde 4 direcciones, Arena expone mucho",
    },
    "Isla Siniestra": {
        "tipo": "Pequeño — CQB y media distancia puro",
        "descripcion": "Isla compacta rodeada de agua. Toda la pelea es en la isla — no hay escapatoria. Distancias cortas y medias dominan completamente. Prisión es el control central más importante.",
        "zonas_clave": {
            "Prisión": "Centro absoluto — zona de máximo conflicto, control = ventaja total",
            "Sala de Calderas": "Suroeste — industrial cerrada, CQB intenso",
            "Área Residencial": "Norte — edificios residenciales, muchos ángulos verticales",
            "Zona de Procesamiento": "Este — industrial semiabierta, cuidado con flancos",
            "Puerto": "Sur — entrada principal, combate inicial intenso",
            "Planta de Tratamiento de Agua": "Oeste — posición aislada, fácil de defender",
        },
        "estrategia_ataque": "Tomar Puerto rápido para cortar spawn sur. Rush a Prisión con flash+SMG — quien llega primero tiene ventaja enorme. Flanquear por Planta de Agua para sorprender en Sala de Calderas. Isla pequeña = el timing de push debe ser exacto.",
        "estrategia_defensa": "Hold en Prisión con ancla. Alambradas en las dos entradas de Sala de Calderas. Minas en el pasillo Área Residencial → Prisión. Soporte media en Zona de Procesamiento con SKS.",
        "mejor_arma": "MP5/MP7 (CQB dominante), Origin-12 (pasillos de Prisión), M4A1 (Procesamiento)",
        "mejor_rol": "Fragger (duelos constantes), Ancla (Prisión), Entry (Puerto)",
        "peligro": "La isla no tiene escape — si te rodean estás muerto. Prisión tiene ángulos desde arriba",
    },
}
