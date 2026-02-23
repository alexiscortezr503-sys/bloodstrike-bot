"""
modules/menu.py — Menú principal con donaciones
"""
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

BIENVENIDA = (
    "⚔️ *BLOODSTRIKE ELITE BOT* ⚔️\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n"
    "🎮 Sistema de entrenamiento profesional\n"
    "👤 Coach: *Alexis Cortez*\n"
    "━━━━━━━━━━━━━━━━━━━━━━\n\n"
    "Selecciona una opción:"
)


def build_main_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("😊 ¿Cómo te sientes?", callback_data="psico_sentir"),
         InlineKeyboardButton("🧠 Psicología Deportiva", callback_data="psico_dep")],
        [InlineKeyboardButton("🏋️ Entrenamiento", callback_data="entren"),
         InlineKeyboardButton("📚 Exámenes", callback_data="examenes")],
        [InlineKeyboardButton("🔫 META Armas", callback_data="meta"),
         InlineKeyboardButton("📐 Sensibilidad", callback_data="sensi")],
        [InlineKeyboardButton("🗺️ Mapas y Tácticas", callback_data="meta_mapas"),
         InlineKeyboardButton("🦾 Strikers", callback_data="meta_strikers")],
        [InlineKeyboardButton("⚡ Combinaciones", callback_data="meta_combos"),
         InlineKeyboardButton("💣 Utilidades", callback_data="meta_utilidades")],
        [InlineKeyboardButton("👥 Jugadores", callback_data="jugadores"),
         InlineKeyboardButton("🏆 Ranking", callback_data="rank")],
        [InlineKeyboardButton("⚔️ Registrar Scrim", callback_data="scrims")],
        [InlineKeyboardButton("💝 Apoyar el Bot", callback_data="donaciones")],
        [InlineKeyboardButton("📋 Panel Coach 🔐", callback_data="coach_menu")],
    ])


async def menu_principal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = build_main_keyboard()
    if update.message:
        await update.message.reply_text(BIENVENIDA, parse_mode="Markdown", reply_markup=keyboard)
    elif update.callback_query:
        await update.callback_query.edit_message_text(BIENVENIDA, parse_mode="Markdown", reply_markup=keyboard)


async def handle_menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data in ("volver_menu", "main_back"):
        await menu_principal(update, context)
