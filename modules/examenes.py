"""
modules/examenes.py — Sistema de exámenes por rol/mapa con ranking
"""

import json
import os
import random
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler
from data.examenes import PREGUNTAS, NIVELES_RANKING, PUNTOS_POR_RESPUESTA, BONUS_RACHA

SELECCION_EXAMEN = 10
RESPONDIENDO_EXAMEN = 11

RANKING_FILE = "data/ranking.json"


def cargar_ranking():
    if os.path.exists(RANKING_FILE):
        with open(RANKING_FILE, "r") as f:
            return json.load(f)
    return {}


def guardar_ranking(data):
    os.makedirs("data", exist_ok=True)
    with open(RANKING_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def get_nivel(puntos: int) -> str:
    nivel = "🥉 Bronce"
    for umbral, nombre in sorted(NIVELES_RANKING.items()):
        if puntos >= umbral:
            nivel = nombre
    return nivel


async def examenes_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menú de exámenes"""
    query = update.callback_query
    await query.answer()

    texto = (
        "📚 *EXÁMENES DE BLOOD STRIKE*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Estudia, responde, sube en el ranking.\n"
        "Cada respuesta correcta = +25 puntos 🏅\n"
        "¡Rachas de respuestas dan bonus extra! 🔥\n\n"
        "Elige el tipo de examen:"
    )

    keyboard = [
        [InlineKeyboardButton("🎯 Mi Rol", callback_data="exam_rol")],
        [
            InlineKeyboardButton("🗺️ Aldea", callback_data="exam_mapa_Aldea"),
            InlineKeyboardButton("🏜️ Desierto", callback_data="exam_mapa_Desierto"),
            InlineKeyboardButton("⚓ Puerto", callback_data="exam_mapa_Puerto"),
        ],
        [InlineKeyboardButton("🏆 Ver Mi Ranking", callback_data="exam_mi_rank")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

    return SELECCION_EXAMEN


async def exam_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja selección de examen e inicia preguntas"""
    query = update.callback_query
    await query.answer()
    data = query.data
    user_id = str(query.from_user.id)
    username = query.from_user.first_name or query.from_user.username or "Jugador"

    if data == "exam_mi_rank":
        await mostrar_ranking_personal(update, context, user_id, username)
        return SELECCION_EXAMEN

    if data == "exam_rol":
        # Usar rol del contexto o mostrar selección
        rol = context.user_data.get("rol_seleccionado")
        if not rol:
            await seleccionar_rol(update, context)
            return SELECCION_EXAMEN

    if data.startswith("exam_set_rol_"):
        rol = data.replace("exam_set_rol_", "")
        context.user_data["rol_seleccionado"] = rol
        await iniciar_examen_rol(update, context, user_id, username, rol)
        return RESPONDIENDO_EXAMEN

    if data.startswith("exam_mapa_"):
        mapa = data.replace("exam_mapa_", "")
        await iniciar_examen_mapa(update, context, user_id, username, mapa)
        return RESPONDIENDO_EXAMEN

    if data == "exam_rol":
        await seleccionar_rol(update, context)
        return SELECCION_EXAMEN


async def seleccionar_rol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    texto = "¿Cuál es tu rol en Blood Strike?\nSelecciona para hacer el examen de tu rol:"

    roles = {
        "IGL": "exam_set_rol_IGL",
        "Fragger": "exam_set_rol_Fragger",
        "Ancla": "exam_set_rol_Ancla",
        "Soporte Media y Larga": "exam_set_rol_Soporte Media y Larga",
    }

    keyboard = [[InlineKeyboardButton(k, callback_data=v)] for k, v in roles.items()]
    keyboard.append([InlineKeyboardButton("⬅️ Volver", callback_data="examenes")])

    await query.edit_message_text(
        texto,
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def iniciar_examen_rol(update, context, user_id, username, rol):
    query = update.callback_query

    if rol not in PREGUNTAS:
        await query.edit_message_text(f"Rol '{rol}' no tiene examen disponible aún.")
        return

    # Construir pool de preguntas de todos los niveles
    pool = []
    for nivel, preguntas in PREGUNTAS[rol].items():
        for p in preguntas:
            pool.append({**p, "nivel": nivel})

    random.shuffle(pool)
    preguntas_seleccionadas = pool[:5]  # 5 preguntas por examen

    context.user_data["exam_preguntas"] = preguntas_seleccionadas
    context.user_data["exam_index"] = 0
    context.user_data["exam_score"] = 0
    context.user_data["exam_racha"] = 0
    context.user_data["exam_tipo"] = f"Rol: {rol}"
    context.user_data["exam_user"] = {"id": user_id, "nombre": username}

    await enviar_pregunta(query, context)


async def iniciar_examen_mapa(update, context, user_id, username, mapa):
    query = update.callback_query

    if mapa not in PREGUNTAS.get("Mapas", {}):
        await query.edit_message_text(f"Mapa '{mapa}' no tiene examen disponible aún.")
        return

    pool = []
    for nivel, preguntas in PREGUNTAS["Mapas"][mapa].items():
        for p in preguntas:
            pool.append({**p, "nivel": nivel})

    random.shuffle(pool)
    preguntas_seleccionadas = pool[:min(5, len(pool))]

    context.user_data["exam_preguntas"] = preguntas_seleccionadas
    context.user_data["exam_index"] = 0
    context.user_data["exam_score"] = 0
    context.user_data["exam_racha"] = 0
    context.user_data["exam_tipo"] = f"Mapa: {mapa}"
    context.user_data["exam_user"] = {"id": user_id, "nombre": username}

    await enviar_pregunta(query, context)


async def enviar_pregunta(query, context):
    preguntas = context.user_data["exam_preguntas"]
    index = context.user_data["exam_index"]
    score = context.user_data["exam_score"]
    racha = context.user_data["exam_racha"]
    total = len(preguntas)

    if index >= total:
        await finalizar_examen(query, context)
        return

    p = preguntas[index]
    nivel_nombre = {1: "Bronce", 2: "Plata", 3: "Oro", 4: "Diamante", 5: "Elite"}.get(p.get("nivel", 1), "?")

    texto = (
        f"📚 *Pregunta {index + 1}/{total}* | Nivel {nivel_nombre}\n"
        f"⭐ Puntos: {score} | 🔥 Racha: {racha}\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"*{p['pregunta']}*\n\n"
    )
    for i, op in enumerate(p["opciones"]):
        texto += f"{op}\n"

    keyboard = []
    for i in range(len(p["opciones"])):
        keyboard.append([InlineKeyboardButton(
            f"{'ABCD'[i]}",
            callback_data=f"ans_{i}"
        )])

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def exam_answer_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    respuesta_idx = int(data.replace("ans_", ""))
    preguntas = context.user_data["exam_preguntas"]
    index = context.user_data["exam_index"]
    p = preguntas[index]

    correcta = p["correcta"]
    es_correcta = (respuesta_idx == correcta)

    if es_correcta:
        context.user_data["exam_racha"] = context.user_data.get("exam_racha", 0) + 1
        racha = context.user_data["exam_racha"]
        bonus = BONUS_RACHA.get(racha, 0)
        puntos_ganados = PUNTOS_POR_RESPUESTA + bonus
        context.user_data["exam_score"] = context.user_data.get("exam_score", 0) + puntos_ganados

        bonus_txt = f" *+{bonus} BONUS de racha {racha}x!* 🔥" if bonus > 0 else ""
        feedback = (
            f"✅ *¡CORRECTO!* +{PUNTOS_POR_RESPUESTA} pts{bonus_txt}\n\n"
            f"💡 *{p['explicacion']}*"
        )
    else:
        context.user_data["exam_racha"] = 0
        opcion_correcta = p["opciones"][correcta]
        feedback = (
            f"❌ *Incorrecto.*\n\n"
            f"La respuesta correcta era: *{opcion_correcta}*\n\n"
            f"💡 *{p['explicacion']}*"
        )

    context.user_data["exam_index"] = index + 1

    keyboard = [[InlineKeyboardButton(
        "➡️ Siguiente" if context.user_data["exam_index"] < len(preguntas) else "🏁 Ver Resultado",
        callback_data="ans_next"
    )]]

    await query.edit_message_text(
        feedback,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

    return RESPONDIENDO_EXAMEN


async def finalizar_examen(query, context):
    score = context.user_data.get("exam_score", 0)
    tipo = context.user_data.get("exam_tipo", "General")
    user_data = context.user_data.get("exam_user", {"id": "0", "nombre": "Jugador"})
    total_preguntas = len(context.user_data.get("exam_preguntas", []))

    # Guardar en ranking
    ranking = cargar_ranking()
    uid = user_data["id"]
    nombre = user_data["nombre"]

    if uid not in ranking:
        ranking[uid] = {"nombre": nombre, "puntos_totales": 0, "examenes": 0, "ultima_actividad": ""}

    ranking[uid]["puntos_totales"] += score
    ranking[uid]["examenes"] += 1
    ranking[uid]["ultima_actividad"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    ranking[uid]["nombre"] = nombre

    guardar_ranking(ranking)

    nivel = get_nivel(ranking[uid]["puntos_totales"])
    puntos_totales = ranking[uid]["puntos_totales"]

    texto = (
        f"🏁 *EXAMEN COMPLETADO*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📋 Tipo: {tipo}\n"
        f"✅ Puntos este examen: *+{score}*\n"
        f"🏆 Puntos totales: *{puntos_totales}*\n"
        f"🎖️ Nivel actual: *{nivel}*\n\n"
        f"{'🔥 ¡Excelente resultado! Sigue así.' if score >= total_preguntas * PUNTOS_POR_RESPUESTA * 0.7 else '💪 Sigue practicando. La constancia gana torneos.'}\n\n"
        f"Haz más exámenes para subir en el ranking y demostrar quién es el mejor del equipo. 👊"
    )

    keyboard = [
        [InlineKeyboardButton("📚 Otro Examen", callback_data="examenes")],
        [InlineKeyboardButton("🏆 Ver Ranking", callback_data="rank")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def mostrar_ranking_personal(update, context, user_id, username):
    query = update.callback_query
    ranking = cargar_ranking()

    if user_id not in ranking:
        await query.edit_message_text(
            "Aún no tienes puntos en el ranking.\nHaz tu primer examen para empezar! 📚",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📚 Hacer Examen", callback_data="examenes")]])
        )
        return

    datos = ranking[user_id]
    nivel = get_nivel(datos["puntos_totales"])

    # Posición en ranking
    sorted_rank = sorted(ranking.items(), key=lambda x: x[1]["puntos_totales"], reverse=True)
    posicion = next((i + 1 for i, (uid, _) in enumerate(sorted_rank) if uid == user_id), "?")

    texto = (
        f"🏆 *TU PERFIL DE RANKING*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 Nombre: {datos['nombre']}\n"
        f"⭐ Puntos totales: *{datos['puntos_totales']}*\n"
        f"🎖️ Nivel: *{nivel}*\n"
        f"📊 Posición en equipo: *#{posicion}*\n"
        f"📚 Exámenes completados: {datos['examenes']}\n"
        f"⏰ Última actividad: {datos.get('ultima_actividad', 'N/A')}\n"
    )

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📚 Hacer Examen", callback_data="examenes")],
            [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
        ])
    )
