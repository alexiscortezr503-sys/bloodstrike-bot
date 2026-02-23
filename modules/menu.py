"""
modules/menu.py — Menú principal con botones inline de Telegram
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

BIENVENIDA = (
    "⚔️ *BLOODSTRIKE ELITE BOT* ⚔️\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🎮 Sistema de entrenamiento profesional\n"
    "👤 Coach: *Alexis Cortez*\n"
    "📱 Plataforma: Móvil\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"
    "Selecciona una opción:"
)


def build_main_keyboard():
    keyboard = [
        [
            InlineKeyboardButton("😊 ¿Cómo te sientes?", callback_data="psico_sentir"),
            InlineKeyboardButton("🧠 Psicología Deportiva", callback_data="psico_dep"),
        ],
        [
            InlineKeyboardButton("🏋️ Mi Plan de Entrenamiento", callback_data="entren"),
            InlineKeyboardButton("📚 Exámenes y Ranking", callback_data="examenes"),
        ],
        [
            InlineKeyboardButton("🔫 META Armas", callback_data="meta"),
            InlineKeyboardButton("📐 Mi Sensibilidad", callback_data="sensi"),
        ],
        [
            InlineKeyboardButton("👥 Jugadores del Equipo", callback_data="jugadores"),
            InlineKeyboardButton("🏆 Ranking Equipo", callback_data="rank"),
        ],
        [
            InlineKeyboardButton("🗺️ Táctica por Mapa", callback_data="meta_mapas"),
            InlineKeyboardButton("🎯 Combinaciones de Habilidades", callback_data="meta_combos"),
        ],
        [
            InlineKeyboardButton("📋 Coach Panel", callback_data="coach_menu"),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


async def menu_principal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = build_main_keyboard()
    if update.message:
        await update.message.reply_text(
            BIENVENIDA,
            parse_mode="Markdown",
            reply_markup=keyboard
        )
    elif update.callback_query:
        await update.callback_query.edit_message_text(
            BIENVENIDA,
            parse_mode="Markdown",
            reply_markup=keyboard
        )


async def handle_menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data in ("main_back", "volver_menu"):
        await menu_principal(update, context)
    else:
        # Fallback genérico — redirige al menú
        await menu_principal(update, context)


def back_button(label="⬅️ Menú Principal", data="volver_menu"):
    return InlineKeyboardMarkup([[InlineKeyboardButton(label, callback_data=data)]])
