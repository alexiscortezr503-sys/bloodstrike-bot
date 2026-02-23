"""
modules/ranking.py — Ranking global del equipo
"""

import json
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from data.examenes import NIVELES_RANKING

RANKING_FILE = "data/ranking.json"

MEDALLAS = {1: "🥇", 2: "🥈", 3: "🥉"}


def cargar_ranking():
    if os.path.exists(RANKING_FILE):
        with open(RANKING_FILE, "r") as f:
            return json.load(f)
    return {}


def get_nivel(puntos: int) -> str:
    nivel = "🥉 Bronce"
    for umbral, nombre in sorted(NIVELES_RANKING.items()):
        if puntos >= umbral:
            nivel = nombre
    return nivel


async def ranking_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Muestra el ranking general del equipo"""

    ranking = cargar_ranking()

    if update.callback_query:
        query = update.callback_query
        await query.answer()
        send = query.edit_message_text
    else:
        send = update.message.reply_text

    if not ranking:
        texto = (
            "🏆 *RANKING DEL EQUIPO*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
            "Aún no hay puntos en el ranking.\n"
            "¡Haz exámenes para aparecer en el top! 📚"
        )
    else:
        sorted_rank = sorted(ranking.items(), key=lambda x: x[1]["puntos_totales"], reverse=True)

        texto = (
            "🏆 *RANKING DEL EQUIPO — BLOOD STRIKE*\n"
            "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        )

        for i, (uid, datos) in enumerate(sorted_rank, 1):
            medalla = MEDALLAS.get(i, f"{i}.")
            nivel = get_nivel(datos["puntos_totales"])
            ultima = datos.get("ultima_actividad", "N/A")
            texto += (
                f"{medalla} *{datos['nombre']}*\n"
                f"   ⭐ {datos['puntos_totales']} pts | {nivel}\n"
                f"   📚 {datos['examenes']} exámenes | ⏰ {ultima}\n\n"
            )

        texto += "¡Sigue haciendo exámenes para subir en el ranking! 🔥"

    keyboard = [
        [InlineKeyboardButton("📚 Hacer Examen", callback_data="examenes")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]

    await send(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
