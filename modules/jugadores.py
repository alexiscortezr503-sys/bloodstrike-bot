"""
modules/jugadores.py — Perfiles de jugadores y estado individual
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from data.jugadores import JUGADORES


async def jugadores_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    texto = (
        "👥 *ROSTER DEL EQUIPO*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "🔴 *ROSTER PRINCIPAL (4/4)*\n"
        "🟡 *ROSTER SECUNDARIO (3/4 — buscando 1 jugador)*\n\n"
        "Selecciona un jugador para ver su perfil:"
    )

    keyboard = []

    # Principal
    principales = [(k, v) for k, v in JUGADORES.items() if v["roster"] == "PRINCIPAL"]
    for key, jug in principales:
        keyboard.append([InlineKeyboardButton(
            f"🔴 {jug['nombre']} | {jug['rol']}",
            callback_data=f"jug_{key}"
        )])

    keyboard.append([InlineKeyboardButton("── SECUNDARIO ──", callback_data="jug_separator")])

    secundarios = [(k, v) for k, v in JUGADORES.items() if v["roster"] == "SECUNDARIO"]
    for key, jug in secundarios:
        keyboard.append([InlineKeyboardButton(
            f"🟡 {jug['nombre']} | {jug['rol']}",
            callback_data=f"jug_{key}"
        )])

    keyboard.append([InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")])

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def jugador_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "jug_separator":
        return

    key = data.replace("jug_", "")

    if key not in JUGADORES:
        await query.answer("Jugador no encontrado", show_alert=True)
        return

    j = JUGADORES[key]
    sensi = j.get("sensi_base", {"x": "?", "y": "?"})

    objetivos_txt = "\n".join([f"  • {obj}" for obj in j["objetivos"]])
    mejorar_txt = "\n".join([f"  • {m}" for m in j["mejorar"]])

    roster_emoji = "🔴" if j["roster"] == "PRINCIPAL" else "🟡"

    texto = (
        f"{roster_emoji} *{j['nombre'].upper()}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🎮 Rol: *{j['rol']}*\n"
        f"📅 Edad: {j['edad']} años\n"
        f"📱 Plataforma: {j['plataforma']}\n"
        f"🏠 Roster: {j['roster']}\n\n"
        f"📐 *Sensibilidad base:*\n"
        f"  X: {sensi['x']} | Y: {sensi['y']}\n\n"
        f"🎯 *Áreas a mejorar:*\n{mejorar_txt}\n\n"
        f"✅ *Objetivos de desarrollo:*\n{objetivos_txt}"
    )

    keyboard = [
        [InlineKeyboardButton("🏋️ Ver Plan de Entrenamiento", callback_data=f"entren_{key}")],
        [InlineKeyboardButton("📐 Ver Sensibilidad Detallada", callback_data="sensi")],
        [InlineKeyboardButton("⬅️ Roster", callback_data="jugadores")],
    ]

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
