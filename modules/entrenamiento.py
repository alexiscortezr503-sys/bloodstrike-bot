"""
modules/entrenamiento.py — Planes de entrenamiento individuales
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from data.entrenamiento import PLANES_INDIVIDUALES, RUTINA_EQUIPO
from data.jugadores import JUGADORES


async def entren_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    texto = (
        "🏋️ *PLANES DE ENTRENAMIENTO*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Cada jugador tiene un plan personalizado\n"
        "basado en sus objetivos y áreas de mejora.\n\n"
        "Selecciona un jugador o la rutina de equipo:"
    )

    keyboard = []

    for key, plan in PLANES_INDIVIDUALES.items():
        keyboard.append([InlineKeyboardButton(
            f"👤 {plan['nombre']}",
            callback_data=f"entren_{key}"
        )])

    keyboard.append([InlineKeyboardButton("👥 Rutina de Equipo", callback_data="entren_equipo")])
    keyboard.append([InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")])

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def entren_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "entren_equipo":
        await mostrar_rutina_equipo(update, context)
        return

    key = data.replace("entren_", "")

    if key not in PLANES_INDIVIDUALES:
        await query.answer("Plan no encontrado", show_alert=True)
        return

    plan = PLANES_INDIVIDUALES[key]
    await mostrar_plan_jugador(update, context, plan, key)


async def mostrar_plan_jugador(update, context, plan, key):
    query = update.callback_query
    fase_actual = plan["fase_actual"]

    texto = (
        f"🏋️ *PLAN DE ENTRENAMIENTO*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 *{plan['nombre']}*\n"
        f"📊 Fase actual: *Fase {fase_actual}*\n\n"
        f"Selecciona una fase para ver los ejercicios:"
    )

    keyboard = []
    for num_fase, fase_data in plan["fases"].items():
        emoji = "▶️" if num_fase == fase_actual else ("✅" if num_fase < fase_actual else "🔒")
        keyboard.append([InlineKeyboardButton(
            f"{emoji} {fase_data['titulo'][:40]}...",
            callback_data=f"entren_fase_{key}_{num_fase}"
        )])

    keyboard.append([InlineKeyboardButton("⬅️ Volver a Planes", callback_data="entren")])

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def mostrar_rutina_equipo(update, context):
    query = update.callback_query
    r = RUTINA_EQUIPO

    bloques_txt = ""
    for b in r["estructura"]:
        bloques_txt += (
            f"\n⏱️ *{b['bloque']}* ({b['duracion']})\n"
            f"   {b['descripcion']}\n"
        )

    texto = (
        f"👥 *RUTINA DE EQUIPO*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📋 {r['titulo']}\n"
        f"📅 Frecuencia: {r['frecuencia']}\n\n"
        f"*Estructura de sesión:*{bloques_txt}"
    )

    keyboard = [
        [InlineKeyboardButton("👤 Ver planes individuales", callback_data="entren")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


# Este handler se llama desde jugadores.py también
async def mostrar_fase_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data  # entren_fase_{key}_{num}

    parts = data.replace("entren_fase_", "").rsplit("_", 1)
    if len(parts) != 2:
        return

    key, num_str = parts
    num_fase = int(num_str)

    if key not in PLANES_INDIVIDUALES:
        return

    plan = PLANES_INDIVIDUALES[key]
    if num_fase not in plan["fases"]:
        return

    fase = plan["fases"][num_fase]

    ejercicios_txt = ""
    for i, ej in enumerate(fase.get("ejercicios", []), 1):
        ejercicios_txt += (
            f"\n*{i}. {ej['nombre']}*\n"
            f"   📝 {ej['descripcion']}\n"
            f"   ⏱️ {ej['duracion']} | 📅 {ej['dias']}\n"
        )

    texto = (
        f"🏋️ *{fase['titulo']}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 Jugador: *{plan['nombre']}*\n\n"
        f"*Ejercicios:*{ejercicios_txt}\n"
        f"🎯 *Meta de esta fase:*\n_{fase.get('meta', 'Completar todos los ejercicios')}_"
    )

    keyboard = [
        [InlineKeyboardButton("⬅️ Ver Fases", callback_data=f"entren_{key}")],
        [InlineKeyboardButton("🏠 Menú Principal", callback_data="volver_menu")],
    ]

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
