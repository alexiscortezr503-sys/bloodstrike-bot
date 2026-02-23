"""
modules/coach.py — Panel exclusivo para el coach (Alexis)
"""

import json
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes

RANKING_FILE = "data/ranking.json"
COACH_ID = int(os.getenv("COACH_ID", "0"))


def es_coach(user_id: int) -> bool:
    return COACH_ID == 0 or user_id == COACH_ID


async def coach_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        user_id = update.message.from_user.id
        send = update.message.reply_text
    else:
        query = update.callback_query
        await query.answer()
        user_id = query.from_user.id
        send = query.edit_message_text

    texto = (
        "📋 *PANEL DEL COACH*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "👤 Coach: *Alexis Cortez*\n\n"
        "Herramientas exclusivas de gestión:"
    )

    keyboard = [
        [InlineKeyboardButton("📊 Ver Ranking Completo", callback_data="coach_ranking")],
        [InlineKeyboardButton("📅 Actividad del Equipo", callback_data="coach_actividad")],
        [InlineKeyboardButton("🔄 Ver Todos los Planes", callback_data="coach_planes")],
        [InlineKeyboardButton("📝 Tips para el Coach", callback_data="coach_tips")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]

    await send(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def coach_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "coach_menu":
        await coach_menu(update, context)
        return

    if data == "coach_ranking":
        await coach_ver_ranking(update, context)
    elif data == "coach_actividad":
        await coach_actividad(update, context)
    elif data == "coach_planes":
        await coach_planes(update, context)
    elif data == "coach_tips":
        await coach_tips(update, context)


async def coach_ver_ranking(update, context):
    query = update.callback_query

    if not os.path.exists(RANKING_FILE):
        await query.edit_message_text(
            "No hay datos de ranking aún.\nLos jugadores deben hacer exámenes primero. 📚",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Coach Panel", callback_data="coach_menu")]])
        )
        return

    with open(RANKING_FILE, "r") as f:
        ranking = json.load(f)

    sorted_rank = sorted(ranking.items(), key=lambda x: x[1]["puntos_totales"], reverse=True)

    texto = "📊 *RANKING DETALLADO — COACH VIEW*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"

    for i, (uid, datos) in enumerate(sorted_rank, 1):
        texto += (
            f"{i}. *{datos['nombre']}*\n"
            f"   Puntos: {datos['puntos_totales']} | Exámenes: {datos['examenes']}\n"
            f"   Última actividad: {datos.get('ultima_actividad', 'N/A')}\n\n"
        )

    if not sorted_rank:
        texto += "_No hay datos aún._"

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Coach Panel", callback_data="coach_menu")]])
    )


async def coach_actividad(update, context):
    query = update.callback_query

    if not os.path.exists(RANKING_FILE):
        await query.edit_message_text(
            "Sin actividad registrada aún.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Coach Panel", callback_data="coach_menu")]])
        )
        return

    with open(RANKING_FILE, "r") as f:
        ranking = json.load(f)

    sorted_by_activity = sorted(
        ranking.items(),
        key=lambda x: x[1].get("ultima_actividad", ""),
        reverse=True
    )

    texto = "📅 *ACTIVIDAD RECIENTE DEL EQUIPO*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"

    for uid, datos in sorted_by_activity:
        ultima = datos.get("ultima_actividad", "Sin actividad")
        examenes = datos.get("examenes", 0)
        texto += f"👤 *{datos['nombre']}*\n  ⏰ {ultima} | 📚 {examenes} exámenes\n\n"

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Coach Panel", callback_data="coach_menu")]])
    )


async def coach_planes(update, context):
    query = update.callback_query

    from data.entrenamiento import PLANES_INDIVIDUALES

    texto = "🔄 *RESUMEN DE PLANES DE ENTRENAMIENTO*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"

    for key, plan in PLANES_INDIVIDUALES.items():
        fase = plan["fase_actual"]
        total_fases = len(plan["fases"])
        fase_data = plan["fases"].get(fase, {})
        texto += (
            f"👤 *{plan['nombre']}*\n"
            f"   Fase {fase}/{total_fases}: {fase_data.get('titulo', '')[:40]}\n"
            f"   Meta: {fase_data.get('meta', 'N/A')[:60]}\n\n"
        )

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("🏋️ Ver planes completos", callback_data="entren")],
            [InlineKeyboardButton("⬅️ Coach Panel", callback_data="coach_menu")],
        ])
    )


async def coach_tips(update, context):
    query = update.callback_query

    texto = (
        "💡 *TIPS PARA EL COACH*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "📌 *Gestión del equipo:*\n"
        "• Haz scrims 3-4 veces/semana mínimo\n"
        "• El VOD review post-scrim es MÁS importante que el scrim mismo\n"
        "• Rota los roles en práctica para que todos entiendan a sus compañeros\n\n"
        "📌 *Psicología de equipo:*\n"
        "• Después de cada derrota: primero valida emociones, LUEGO analiza\n"
        "• El feedback 1-a-1 privado es más efectivo que la crítica grupal\n"
        "• Los jugadores jóvenes (14-16) necesitan más refuerzo positivo\n\n"
        "📌 *Desarrollo individual:*\n"
        "• Anderson (IGL, 15): dale liderazgo progresivo — que haga pequeñas calls primero\n"
        "• Jose (Fragger, 14): motivación constante, ve sus progresos en SMG semana a semana\n"
        "• Maxi (14): el más joven del roster 2 — necesita el ambiente más positivo\n"
        "• Xavier: con más técnica de movimiento mejorará exponencialmente\n"
        "• Alejandro: el más maduro — puede ser voz de liderazgo en el roster principal\n\n"
        "📌 *Sobre el roster incompleto:*\n"
        "• El rol que falta: considera un *Entry Fragger puro* o segundo *IGL de respaldo*\n"
        "• Anderson 2 puede adaptarse — evalúalo en 2 semanas con roles diferentes"
    )

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Coach Panel", callback_data="coach_menu")]])
    )
