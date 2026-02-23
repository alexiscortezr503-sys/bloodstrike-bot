"""
data/meta.py — META actualizado de Blood Strike (Armas, Habilidades, Combinaciones)
Se actualiza cuando hay parches nuevos vía /actualizarmeta (solo coach)
"""

META_ARMAS = {
    "SMG": [
        {
            "nombre": "MP5",
            "tier": "S",
            "uso": "Corta distancia, rush, CQB",
            "ventajas": "Alto DPS, baja al calentar rápido, ideal para entry",
            "contras": "Pierde contra AR a media distancia",
            "accesorios_meta": ["Cañón largo", "Cargador extendido", "Mira punto rojo"],
        },
        {
            "nombre": "UMP45",
            "tier": "A",
            "uso": "Corta-media, tanqueo",
            "ventajas": "Buen control, versátil, daño decente",
            "contras": "Velocidad de fuego moderada",
            "accesorios_meta": ["Supresor", "Empuñadura delantera", "Cargador extendido"],
        },
        {
            "nombre": "PP-19",
            "tier": "A",
            "uso": "Rush corta distancia",
            "ventajas": "Cadencia muy alta, devastador en CQB",
            "contras": "Recoil agresivo, poco alcance",
            "accesorios_meta": ["Cargador extendido", "Mira holográfica"],
        },
    ],
    "AR": [
        {
            "nombre": "M4A1",
            "tier": "S",
            "uso": "Media distancia, todo terreno",
            "ventajas": "Equilibrio perfecto, fácil de controlar",
            "contras": "No sobresale en nada extremo",
            "accesorios_meta": ["Cañón largo", "Empuñadura delantera", "Mira 2x", "Cargador extendido"],
        },
        {
            "nombre": "AK-47",
            "tier": "S",
            "uso": "Media-larga, daño alto",
            "ventajas": "Mayor daño por bala que M4, excelente en media",
            "contras": "Recoil vertical difícil de dominar",
            "accesorios_meta": ["Empuñadura trasera", "Empuñadura delantera", "Mira 2x"],
        },
        {
            "nombre": "SCAR",
            "tier": "A",
            "uso": "Media distancia",
            "ventajas": "Estable, buen daño",
            "contras": "Cadencia baja comparado con M4",
            "accesorios_meta": ["Cañón largo", "Mira 4x", "Empuñadura delantera"],
        },
    ],
    "Francotirador": [
        {
            "nombre": "Kar98k",
            "tier": "S",
            "uso": "Larga distancia, one-shot",
            "ventajas": "One-shot a la cabeza, alta satisfacción, ícono competitivo",
            "contras": "Solo semi-jugadores experimentados lo usan bien",
            "accesorios_meta": ["Mira 8x", "Cañón largo", "Bípode"],
        },
        {
            "nombre": "M24",
            "tier": "A",
            "uso": "Larga distancia",
            "ventajas": "Mayor cadencia que Kar, bueno para scrim",
            "contras": "Daño ligeramente menor",
            "accesorios_meta": ["Mira 6x", "Cañón largo"],
        },
    ],
    "DMR": [
        {
            "nombre": "SKS",
            "tier": "S",
            "uso": "Media-larga, soporte",
            "ventajas": "Semi-automático, ideal para soporte media",
            "contras": "Requiere buen centering y tracking",
            "accesorios_meta": ["Mira 4x", "Cargador extendido", "Empuñadura delantera"],
        },
        {
            "nombre": "Mini14",
            "tier": "A",
            "uso": "Media distancia, molestia",
            "ventajas": "Alta cadencia para DMR",
            "contras": "Daño menor por disparo",
            "accesorios_meta": ["Mira 3x", "Cargador extendido"],
        },
    ],
    "Escopeta": [
        {
            "nombre": "S1897",
            "tier": "A",
            "uso": "CQB extremo, one-shot close",
            "ventajas": "One-shot al cuerpo en ultra corta",
            "contras": "Una sola bala efectiva, requiere ejecución perfecta",
            "accesorios_meta": ["Cañón modificado", "Culata"],
        },
    ],
}

META_HABILIDADES = {
    "ofensivas": [
        {"nombre": "Granada de fragmentación", "uso": "Limpiar cover, zonas cerradas"},
        {"nombre": "Bomba de humo", "uso": "Entrar a zona, cubrir retirada"},
        {"nombre": "Granada de destello (Flash)", "uso": "Cegar enemigos antes de rush"},
        {"nombre": "Cóctel molotov", "uso": "Bloquear paso, zona de daño continuo"},
    ],
    "defensivas": [
        {"nombre": "Alambrada", "uso": "Ralentizar rush, defender captura"},
        {"nombre": "Mina antipersona", "uso": "Proteger flanco, alertar movimiento"},
        {"nombre": "Barricada portátil", "uso": "Cover instantáneo"},
    ],
    "soporte": [
        {"nombre": "Kit médico de área", "uso": "Curar al equipo en zona"},
        {"nombre": "Revive rápido", "uso": "Levantar compañero sin quedarse quieto"},
        {"nombre": "Dron de reconocimiento", "uso": "Ver enemigos en mapa"},
    ],
}

COMBINACIONES_META = {
    "Rush (BE - Blood Edition)": {
        "descripcion": "Máxima agresividad, entrar rápido y limpiar",
        "armas": ["MP5 + Pistola", "PP-19 + Pistola"],
        "habilidades": ["Flash + Humo", "Flash + Granada Frag"],
        "estrategia": (
            "Flash primero para cegar, humo para entrada segura. "
            "El entry fragger entra con PP-19/MP5 a máxima velocidad. "
            "IGL dicta el timing. Ancla cubre retaguardia."
        ),
        "modo": "BE",
    },
    "Rush (TCT - Tactical)": {
        "descripcion": "Rush coordinado con equipo táctico",
        "armas": ["M4A1 + SMG de respaldo", "AK47 + SMG"],
        "habilidades": ["Humo + Alambrada (para cubrir flanco)", "Flash + Frag"],
        "estrategia": (
            "Humo para tapar visión, alambrada para asegurar flanco. "
            "Entry fragger abre, IGL ordena timing, soporte cura si hay bajas."
        ),
        "modo": "TCT",
    },
    "Tanqueo (Defensivo)": {
        "descripcion": "Aguantar zona, resistir rush enemigo",
        "armas": ["AK47", "SCAR", "SKS (soporte)"],
        "habilidades": ["Alambrada + Barricada", "Mina + Kit médico"],
        "estrategia": (
            "Alambrada ralentiza push. Barricada da cover. "
            "Ancla se queda firme en ángulo. Soporte media con SKS molesta desde lejos. "
            "No salir a duelos innecesarios — forzar al rival a entrar a nuestro terreno."
        ),
        "modo": "Ambos",
    },
    "Defensiva Lo-que-sea": {
        "descripcion": "Adaptable según situación — hold o counter-rush",
        "armas": ["M4A1", "SKS", "Kar98k para zona abierta"],
        "habilidades": ["Dron + Mina", "Kit médico + Frag"],
        "estrategia": (
            "Dron para info antes del push. Minas en flancos. "
            "Si viene rush corto: counter con SMG. Si viene lento: AR/DMR los molesta. "
            "Kit médico listo para sostener."
        ),
        "modo": "Ambos",
    },
}

MAPAS_BLOODSTRIKE = {
    "Aldea": {
        "descripcion": "Mapa urbano cerrado, muchos CQB, ideal para SMG",
        "zonas_clave": ["Centro del mercado", "Callejones traseros", "Edificio alto norte"],
        "estrategia_ataque": "Rush por callejones con smokes, entry limpio al mercado",
        "estrategia_defensa": "Alambradas en entradas, ancla en edificio alto",
        "mejor_rol_aqui": "Entry Fragger + IGL para el timing",
    },
    "Desierto": {
        "descripcion": "Zona abierta, largas distancias, ideal para DMR/Sniper",
        "zonas_clave": ["Roca central", "Torre de agua", "Bunker sur"],
        "estrategia_ataque": "Humos para cruzar campo abierto, soporte media cubre desde torre",
        "estrategia_defensa": "Kar98k/SKS desde posiciones elevadas, minas en pasos obligatorios",
        "mejor_rol_aqui": "Soporte Larga + Ancla como hold",
    },
    "Puerto": {
        "descripcion": "Mix de corta y media, contenedores para cover, agua de fondo",
        "zonas_clave": ["Zona de contenedores", "Muelle principal", "Almacén"],
        "estrategia_ataque": "Humo al muelle, frag a contenedores, split en dos frentes",
        "estrategia_defensa": "Alambrada en almacén, ancla en contenedores con SMG",
        "mejor_rol_aqui": "Todos los roles tienen valor aquí (mapa completo)",
    },
}
