"""
modules/sensi.py — Sensibilidad personalizada por jugador y consejos pro
Celulares reales de cada jugador del equipo
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

# Sensibilidades por celular y rol
SENSI_DATA = {
    "Infinix GT30": {
        "descripcion": "Pantalla 6.78\" 144Hz — Alta fluidez, excelente para gaming agresivo",
        "roles": {
            "IGL / Todo terreno": {"X": "22-26", "Y": "20-24", "mira_2x": "15-18", "mira_4x": "10-13"},
            "Fragger / CQB": {"X": "28-33", "Y": "26-30", "mira_2x": "18-22", "mira_4x": "12-15"},
            "Ancla / Media": {"X": "20-25", "Y": "18-22", "mira_2x": "13-16", "mira_4x": "9-12"},
            "Soporte Larga": {"X": "15-20", "Y": "13-18", "mira_2x": "10-13", "mira_4x": "7-10"},
        }
    },
    "Samsung Galaxy S22+": {
        "descripcion": "Pantalla 6.6\" 120Hz AMOLED — Fluidez y precisión táctil excelente",
        "roles": {
            "IGL / Todo terreno": {"X": "20-24", "Y": "18-22", "mira_2x": "14-17", "mira_4x": "9-12"},
            "Fragger / CQB": {"X": "26-30", "Y": "24-28", "mira_2x": "17-20", "mira_4x": "11-14"},
            "Ancla / Media": {"X": "18-22", "Y": "16-20", "mira_2x": "12-15", "mira_4x": "8-11"},
            "Soporte Larga": {"X": "14-18", "Y": "12-16", "mira_2x": "9-12", "mira_4x": "6-9"},
        }
    },
    "Xiaomi 14 Pro 5G": {
        "descripcion": "Pantalla 6.73\" 120Hz LTPO — Ultra premium, respuesta táctil top tier",
        "roles": {
            "IGL / Todo terreno": {"X": "18-22", "Y": "16-20", "mira_2x": "12-15", "mira_4x": "8-11"},
            "Fragger / CQB": {"X": "24-28", "Y": "22-26", "mira_2x": "15-19", "mira_4x": "10-13"},
            "Ancla / Media": {"X": "16-20", "Y": "14-18", "mira_2x": "11-14", "mira_4x": "7-10"},
            "Soporte Larga": {"X": "12-16", "Y": "10-14", "mira_2x": "8-11", "mira_4x": "5-8"},
        }
    },
    "Redmi Note 11": {
        "descripcion": "Pantalla 6.43\" 90Hz — Buena pantalla, sensi ligeramente mayor para compensar",
        "roles": {
            "IGL / Todo terreno": {"X": "24-28", "Y": "22-26", "mira_2x": "16-19", "mira_4x": "10-13"},
            "Fragger / CQB": {"X": "30-35", "Y": "28-32", "mira_2x": "19-23", "mira_4x": "13-16"},
            "Ancla / Media": {"X": "22-26", "Y": "20-24", "mira_2x": "14-17", "mira_4x": "9-12"},
            "Soporte Larga": {"X": "16-20", "Y": "14-18", "mira_2x": "10-13", "mira_4x": "7-10"},
        }
    },
    "Xiaomi POCO X7 Pro": {
        "descripcion": "Pantalla 6.67\" 120Hz — Alta gama media, respuesta táctil muy buena",
        "roles": {
            "IGL / Todo terreno": {"X": "20-25", "Y": "18-23", "mira_2x": "13-17", "mira_4x": "9-12"},
            "Fragger / CQB": {"X": "26-31", "Y": "24-29", "mira_2x": "17-21", "mira_4x": "11-14"},
            "Ancla / Media": {"X": "18-23", "Y": "16-21", "mira_2x": "12-15", "mira_4x": "8-11"},
            "Soporte Larga": {"X": "14-19", "Y": "12-17", "mira_2x": "9-12", "mira_4x": "6-9"},
        }
    },
    "Tecno POVA 5": {
        "descripcion": "Pantalla 6.78\" 120Hz — Buen gaming phone gama media, táctil competente",
        "roles": {
            "IGL / Todo terreno": {"X": "23-27", "Y": "21-25", "mira_2x": "15-18", "mira_4x": "10-13"},
            "Fragger / CQB": {"X": "29-34", "Y": "27-31", "mira_2x": "18-22", "mira_4x": "12-15"},
            "Ancla / Media": {"X": "21-25", "Y": "19-23", "mira_2x": "13-16", "mira_4x": "9-12"},
            "Soporte Larga": {"X": "15-19", "Y": "13-17", "mira_2x": "10-13", "mira_4x": "7-10"},
        }
    },
    "Samsung Galaxy S21 FE": {
        "descripcion": "Pantalla 6.4\" 120Hz AMOLED — Excelente pantalla gaming, táctil de calidad",
        "roles": {
            "IGL / Todo terreno": {"X": "20-24", "Y": "18-22", "mira_2x": "13-16", "mira_4x": "9-12"},
            "Fragger / CQB": {"X": "26-30", "Y": "24-28", "mira_2x": "16-20", "mira_4x": "11-14"},
            "Ancla / Media": {"X": "18-22", "Y": "16-20", "mira_2x": "12-15", "mira_4x": "8-11"},
            "Soporte Larga": {"X": "14-18", "Y": "12-16", "mira_2x": "9-12", "mira_4x": "6-9"},
        }
    },
}

# Celulares por jugador
CELULAR_JUGADOR = {
    "anderson1": "Infinix GT30",
    "jose": "Samsung Galaxy S22+",
    "alejandro": "Xiaomi 14 Pro 5G",
    "maximiliano": "Redmi Note 11",
    "xavier": "Xiaomi POCO X7 Pro",
    "antonio": "Tecno POVA 5",
    "anderson2": "Samsung Galaxy S21 FE",
}

CONSEJOS_PRO_SENSI = """
🎯 *GUÍA PROFESIONAL PARA ENCONTRAR TU SENSI (X)(Y)*
━━━━━━━━━━━━━━━━━━━━━━

📱 *¿Qué son los valores X e Y?*
En Blood Strike, cuando activas la *Sensibilidad Avanzada*, aparecen dos valores en pantalla: *X* (horizontal) e *Y* (vertical). Ajustar ambos por separado es lo que usan los jugadores pro.

━━━━━━━━━━━━━━━━━━━━━━
🔬 *MÉTODO PRO PARA ENCONTRAR TU SENSI PERFECTA:*

*Paso 1 — Activa la Sensibilidad Avanzada*
Ve a Configuración → Sensibilidad → activa la opción de sensibilidad avanzada. Verás los valores (X)(Y) separados.

*Paso 2 — Empieza con los valores base*
Usa los valores recomendados para tu celular y rol como punto de partida. NO son perfectos — son un punto de inicio.

*Paso 3 — Prueba de línea recta*
Apunta a una pared. Intenta hacer una línea perfectamente horizontal arrastrando el dedo. Si la línea se va hacia arriba: baja Y. Si se va hacia abajo: sube Y.

*Paso 4 — Prueba de velocidad de giro*
Haz un giro de 180° rápido. ¿Te pasas del objetivo? Baja X. ¿No alcanzas el objetivo? Sube X.

*Paso 5 — El ajuste de ±2 en ±2*
Nunca cambies más de 2 puntos por ajuste. Cambios grandes rompen el muscle memory. Pequeño ajuste → 100 duelos → evaluar → otro ajuste si necesario.

*Paso 6 — Sensi de mira separada*
La mira 2x y 4x deben estar en torno al 60-70% de tu sensi base. Con mira lenta se apunta mejor a larga distancia.

━━━━━━━━━━━━━━━━━━━━━━
⚠️ *REGLAS DE ORO:*
→ Una vez que encuentras tu sensi — *NO LA CAMBIES* sin razón. La consistencia vale más que la perfecta
→ Dale mínimo *5-7 días* a una nueva sensi antes de evaluar si funciona
→ Si cambias de celular: ajustar desde cero con el método
→ La sensi que usas en training mode debe ser *exactamente igual* a la de partidas reales
→ Si un pro usa sensi X no significa que sea correcta para ti — cada mano y cada pantalla son distintas
"""


async def sensi_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    texto = (
        "📐 *SENSIBILIDAD POR JUGADOR*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Selecciona tu celular o consulta la guía pro:"
    )

    keyboard = [
        [InlineKeyboardButton("🔴 Anderson — Infinix GT30", callback_data="sensi_cel_Infinix GT30")],
        [InlineKeyboardButton("🔴 Jose — Samsung S22+", callback_data="sensi_cel_Samsung Galaxy S22+")],
        [InlineKeyboardButton("🔴 Alejandro — Xiaomi 14 Pro", callback_data="sensi_cel_Xiaomi 14 Pro 5G")],
        [InlineKeyboardButton("🔴 Xavier — POCO X7 Pro", callback_data="sensi_cel_Xiaomi POCO X7 Pro")],
        [InlineKeyboardButton("🟡 Antonio — Tecno POVA 5", callback_data="sensi_cel_Tecno POVA 5")],
        [InlineKeyboardButton("🟡 Anderson 2 — Samsung S21 FE", callback_data="sensi_cel_Samsung Galaxy S21 FE")],
        [InlineKeyboardButton("🟡 Maximiliano — Redmi Note 11", callback_data="sensi_cel_Redmi Note 11")],
        [InlineKeyboardButton("🎯 Guía Pro para encontrar tu Sensi", callback_data="sensi_guia_pro")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]

    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def sensi_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "sensi_guia_pro":
        keyboard = [
            [InlineKeyboardButton("📐 Ver sensibilidades", callback_data="sensi")],
            [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
        ]
        await query.edit_message_text(CONSEJOS_PRO_SENSI, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
        return

    if data.startswith("sensi_cel_"):
        cel = data.replace("sensi_cel_", "")
        await mostrar_sensi_celular(query, cel)
        return

    if data.startswith("sensi_rol_"):
        parts = data.replace("sensi_rol_", "").split("|||")
        if len(parts) == 2:
            cel, rol = parts
            await mostrar_valores_sensi(query, cel, rol)
        return


async def mostrar_sensi_celular(query, celular):
    if celular not in SENSI_DATA:
        await query.answer("Celular no encontrado", show_alert=True)
        return

    info = SENSI_DATA[celular]
    texto = (
        f"📱 *{celular}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"_{info['descripcion']}_\n\n"
        f"Selecciona tu rol para ver los valores (X)(Y):"
    )

    keyboard = []
    for rol in info["roles"].keys():
        keyboard.append([InlineKeyboardButton(rol, callback_data=f"sensi_rol_{celular}|||{rol}")])
    keyboard.append([InlineKeyboardButton("🎯 Guía Pro de Sensi", callback_data="sensi_guia_pro")])
    keyboard.append([InlineKeyboardButton("⬅️ Volver", callback_data="sensi")])

    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def mostrar_valores_sensi(query, celular, rol):
    if celular not in SENSI_DATA or rol not in SENSI_DATA[celular]["roles"]:
        await query.answer("No disponible", show_alert=True)
        return

    vals = SENSI_DATA[celular]["roles"][rol]
    texto = (
        f"📐 *SENSIBILIDAD (X)(Y)*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📱 {celular}\n"
        f"🎮 Rol: {rol}\n\n"
        f"*Sensibilidad general:*\n"
        f"  X (horizontal): *{vals['X']}*\n"
        f"  Y (vertical): *{vals['Y']}*\n\n"
        f"*Con mira 2x:*\n"
        f"  X e Y: *{vals['mira_2x']}*\n\n"
        f"*Con mira 4x:*\n"
        f"  X e Y: *{vals['mira_4x']}*\n\n"
        f"💡 *Activa la Sensibilidad Avanzada* en el juego para ver y ajustar los valores X e Y por separado. "
        f"Los rangos son un punto de inicio — ajusta de a ±2 hasta encontrar tu punto exacto.\n\n"
        f"🎯 Consulta la *Guía Pro* para el método completo de ajuste."
    )

    keyboard = [
        [InlineKeyboardButton("🎯 Guía Pro de Sensi", callback_data="sensi_guia_pro")],
        [InlineKeyboardButton("⬅️ Otros roles", callback_data=f"sensi_cel_{celular}")],
        [InlineKeyboardButton("🏠 Menú Principal", callback_data="volver_menu")],
    ]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
