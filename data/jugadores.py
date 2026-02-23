"""
data/jugadores.py — Roster completo + metas individuales + historial de mejora
"""

JUGADORES = {
    # ─── ROSTER PRINCIPAL ───────────────────────────────────────────────────
    "anderson1": {
        "nombre": "Anderson",
        "edad": 15,
        "roster": "PRINCIPAL",
        "rol": "IGL",
        "plataforma": "Móvil",
        "mejorar": ["Corta distancia con subfusil"],
        "objetivos": [
            "Dominar SMG en rangos cortos (≤15m)",
            "Comunicación de info clara al equipo",
            "Toma de decisiones bajo presión",
        ],
        "sensi_base": {"x": 85, "y": 85},
        "progreso": 0,
        "estado_animo": "neutral",
    },
    "jose": {
        "nombre": "Jose",
        "edad": 14,
        "roster": "PRINCIPAL",
        "rol": "Fragger",
        "plataforma": "Móvil",
        "mejorar": ["Corta distancia con subfusil"],
        "objetivos": [
            "Controlar recoil de SMG en menos de 2 semanas",
            "Entry limpio sin exponer al equipo",
            "Velocidad de reacción 0-10m",
        ],
        "sensi_base": {"x": 90, "y": 90},
        "progreso": 0,
        "estado_animo": "neutral",
    },
    "xavier": {
        "nombre": "Xavier",
        "edad": 16,
        "roster": "PRINCIPAL",
        "rol": "Ancla",
        "plataforma": "Móvil",
        "mejorar": ["Movimiento", "Aim corta distancia", "Aim larga distancia"],
        "objetivos": [
            "Dominar movement: peek, strafe, crouch-spam",
            "Aim tracking en corta (SMG) y larga (DMR/Sniper)",
            "Sostener posición ancla bajo presión",
        ],
        "sensi_base": {"x": 75, "y": 75},
        "progreso": 0,
        "estado_animo": "neutral",
    },
    "alejandro": {
        "nombre": "Alejandro",
        "edad": 18,
        "roster": "PRINCIPAL",
        "rol": "Soporte Media y Larga",
        "plataforma": "Móvil",
        "mejorar": ["Centering", "Tracking (Aim)"],
        "objetivos": [
            "Centering profesional — crosshair siempre a altura de cabeza",
            "Tracking suave para rangos medios (AR/DMR)",
            "Visión de mapa y cobertura al equipo",
        ],
        "sensi_base": {"x": 65, "y": 65},
        "progreso": 0,
        "estado_animo": "neutral",
    },

    # ─── ROSTER SECUNDARIO ──────────────────────────────────────────────────
    "antonio": {
        "nombre": "Antonio",
        "edad": 18,
        "roster": "SECUNDARIO",
        "rol": "Fragger",
        "plataforma": "Móvil",
        "mejorar": ["Aim agresivo", "Entry rápido"],
        "objetivos": [
            "Perfeccionar el duelo en corta distancia",
            "Lectura del mapa para entry fragger",
            "Reducir muertes innecesarias en push",
        ],
        "sensi_base": {"x": 88, "y": 88},
        "progreso": 0,
        "estado_animo": "neutral",
    },
    "anderson2": {
        "nombre": "Anderson 2",
        "edad": 16,
        "roster": "SECUNDARIO",
        "rol": "Sin definir",
        "plataforma": "Móvil",
        "mejorar": ["Corta distancia", "Larga distancia"],
        "objetivos": [
            "Definir rol óptimo según habilidades naturales",
            "Mejorar aim en todos los rangos",
            "Aprender fundamentos tácticos de cada rol",
        ],
        "sensi_base": {"x": 80, "y": 80},
        "progreso": 0,
        "estado_animo": "neutral",
    },
    "maximiliano": {
        "nombre": "Maximiliano",
        "edad": 14,
        "roster": "SECUNDARIO",
        "rol": "Soporte Media y Larga",
        "plataforma": "Móvil",
        "mejorar": [
            "Aim corta distancia",
            "Aim larga distancia",
            "Movimientos profesionales",
            "Todo (jugador en desarrollo completo)",
        ],
        "objetivos": [
            "Movimientos como los pros (Profeta-style: peek, jiggle, crouch)",
            "Aim fundamental en todos los rangos",
            "Posicionamiento de soporte",
            "Mentalidad competitiva desde cero",
        ],
        "sensi_base": {"x": 70, "y": 70},
        "progreso": 0,
        "estado_animo": "neutral",
    },
}

ROLES_DISPONIBLES = [
    "Entry Fragger",
    "Fragger",
    "Fragger IGL",
    "IGL",
    "Ancla",
    "Soporte Media",
    "Soporte Larga",
    "Soporte Media y Larga",
]

EQUIPO = {
    "nombre": "Sin nombre aún",
    "coach": "Alexis Cortez",
    "juego": "Blood Strike",
    "plataforma": "Móvil",
}
