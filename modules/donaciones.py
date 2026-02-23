"""
modules/donaciones.py — Sistema de donaciones
"""
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

TON_ADDRESS = "UQAv_WaJjv6r7Frys8POL1m3xhoAzq7jNjFk7n803b2gmde2"
COACH_USERNAME = "@mkoialex"


async def donaciones_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    texto = (
        "💝 *APOYAR BLOODSTRIKE ELITE BOT*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Este bot es completamente *gratuito* para el equipo. "
        "Si quieres apoyar su desarrollo y mantenimiento, "
        "puedes donar desde Telegram.\n\n"
        "Cada donación ayuda a mantener el bot activo y agregar "
        "nuevas funciones para el equipo 🙏\n\n"
        "Elige cómo quieres apoyar:"
    )

    keyboard = [
        [InlineKeyboardButton("⭐ Donar Estrellas de Telegram", callback_data="donar_estrellas")],
        [InlineKeyboardButton("💎 Donar Toncoins (TON)", callback_data="donar_ton")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]

    await query.edit_message_text(
        texto, parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def donar_estrellas_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    texto = (
        "⭐ *DONAR ESTRELLAS DE TELEGRAM*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Las Estrellas son la moneda oficial de Telegram.\n\n"
        "*Cómo donarme Estrellas:*\n"
        f"1. Abre Telegram y busca *{COACH_USERNAME}*\n"
        "2. Abre mi perfil\n"
        "3. Toca los tres puntos *( ... )*\n"
        "4. Selecciona *'Enviar regalo'*\n"
        "5. Elige la cantidad de Estrellas ⭐\n\n"
        "¡Cualquier cantidad es muy apreciada! 🙏\n"
        "Las Estrellas ayudan a mantener el bot gratuito para el equipo. 💪"
    )

    keyboard = [
        [InlineKeyboardButton("⬅️ Volver", callback_data="donaciones")],
        [InlineKeyboardButton("🏠 Menú Principal", callback_data="volver_menu")],
    ]

    await query.edit_message_text(
        texto, parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def donar_ton_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    texto = (
        "💎 *DONAR TONCOINS (TON)*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "TON es la criptomoneda oficial de Telegram.\n\n"
        "*Para donar TON:*\n"
        "1. Abre *@wallet* en Telegram\n"
        "2. Ve a *Enviar*\n"
        "3. Envía TON a esta dirección:\n\n"
        f"`{TON_ADDRESS}`\n\n"
        "4. Envía la cantidad que desees 💎\n\n"
        "¡Cualquier cantidad es muy apreciada! 🙏"
    )

    keyboard = [
        [InlineKeyboardButton("⬅️ Volver", callback_data="donaciones")],
        [InlineKeyboardButton("🏠 Menú Principal", callback_data="volver_menu")],
    ]

    await query.edit_message_text(
        texto, parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
