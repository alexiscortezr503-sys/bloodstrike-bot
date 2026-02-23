"""
modules/examenes.py — Sistema de exámenes con flujo correcto de preguntas
"""

import json, os, random
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


def get_nivel(puntos):
    nivel = "🥉 Bronce"
    for umbral, nombre in sorted(NIVELES_RANKING.items()):
        if puntos >= umbral:
            nivel = nombre
    return nivel


async def examenes_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    texto = (
        "📚 *EXÁMENES DE BLOOD STRIKE*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Estudia, responde, sube en el ranking.\n"
        "✅ Respuesta correcta = *+25 puntos*\n"
        "🔥 Racha de 3 = *+10 bonus*\n"
        "🔥 Racha de 5 = *+25 bonus*\n"
        "🔥 Racha de 7 = *+50 bonus*\n\n"
        "Elige el tipo de examen:"
    )

    keyboard = [
        [InlineKeyboardButton("🎮 Examen de mi Rol", callback_data="exam_elegir_rol")],
        [
            InlineKeyboardButton("🗺️ Valle Abandonado", callback_data="exam_mapa_Valle Abandonado"),
            InlineKeyboardButton("🏖️ Playa Cielo", callback_data="exam_mapa_Playa Cielo"),
        ],
        [InlineKeyboardButton("🏝️ Isla Siniestra", callback_data="exam_mapa_Isla Siniestra")],
        [InlineKeyboardButton("🏆 Mi Ranking", callback_data="exam_mi_rank")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]

    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
    return SELECCION_EXAMEN


async def exam_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data
    user_id = str(query.from_user.id)
    username = query.from_user.first_name or "Jugador"

    if data == "exam_mi_rank":
        await mostrar_ranking_personal(query, user_id, username)
        return SELECCION_EXAMEN

    if data == "exam_elegir_rol":
        await mostrar_selector_rol(query)
        return SELECCION_EXAMEN

    if data.startswith("exam_set_rol_"):
        rol = data.replace("exam_set_rol_", "").replace("_", " ")
        context.user_data["rol_seleccionado"] = rol
        await iniciar_examen(query, context, user_id, username, tipo="rol", valor=rol)
        return RESPONDIENDO_EXAMEN

    if data.startswith("exam_mapa_"):
        mapa = data.replace("exam_mapa_", "")
        await iniciar_examen(query, context, user_id, username, tipo="mapa", valor=mapa)
        return RESPONDIENDO_EXAMEN

    return SELECCION_EXAMEN


async def mostrar_selector_rol(query):
    texto = "¿Cuál es tu rol en Blood Strike?"
    roles = ["IGL", "Fragger", "Ancla", "Soporte Media y Larga"]
    keyboard = [[InlineKeyboardButton(r, callback_data=f"exam_set_rol_{r.replace(' ', '_')}")] for r in roles]
    keyboard.append([InlineKeyboardButton("⬅️ Volver", callback_data="examenes")])
    await query.edit_message_text(texto, reply_markup=InlineKeyboardMarkup(keyboard))


async def iniciar_examen(query, context, user_id, username, tipo, valor):
    pool = []

    if tipo == "rol":
        if valor not in PREGUNTAS:
            await query.edit_message_text(f"Examen para '{valor}' próximamente. 🔜")
            return
        for nivel, preguntas in PREGUNTAS[valor].items():
            for p in preguntas:
                pool.append({**p, "nivel": nivel})

    elif tipo == "mapa":
        mapas = PREGUNTAS.get("Mapas", {})
        # Buscar mapa por nombre similar
        mapa_key = None
        for k in mapas.keys():
            if valor in k or k in valor:
                mapa_key = k
                break
        if not mapa_key:
            await query.edit_message_text(f"Examen para '{valor}' próximamente. 🔜")
            return
        for nivel, preguntas in mapas[mapa_key].items():
            for p in preguntas:
                pool.append({**p, "nivel": nivel})

    if not pool:
        await query.edit_message_text("No hay preguntas disponibles aún para esta selección. 🔜")
        return

    random.shuffle(pool)
    seleccionadas = pool[:min(5, len(pool))]

    context.user_data.update({
        "exam_preguntas": seleccionadas,
        "exam_index": 0,
        "exam_score": 0,
        "exam_racha": 0,
        "exam_tipo": f"{'Rol' if tipo == 'rol' else 'Mapa'}: {valor}",
        "exam_uid": user_id,
        "exam_nombre": username,
        "exam_ultima_correcta": None,
    })

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
    nivel_txt = {1: "🥉 Bronce", 2: "🥈 Plata", 3: "🥇 Oro", 4: "💎 Diamante", 5: "⭐ Elite"}.get(p.get("nivel", 1), "")

    racha_txt = f" 🔥x{racha}" if racha >= 2 else ""
    texto = (
        f"📚 *Pregunta {index + 1} de {total}* | {nivel_txt}\n"
        f"⭐ Puntos: {score}{racha_txt}\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"*{p['pregunta']}*\n\n"
        + "\n".join(p["opciones"])
    )

    letras = ["A", "B", "C", "D"]
    keyboard = [[InlineKeyboardButton(letras[i], callback_data=f"ans_{i}")] for i in range(len(p["opciones"]))]

    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def exam_answer_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # Botón "siguiente pregunta"
    if data == "ans_next":
        await enviar_pregunta(query, context)
        return RESPONDIENDO_EXAMEN

    respuesta_idx = int(data.replace("ans_", ""))
    preguntas = context.user_data.get("exam_preguntas", [])
    index = context.user_data.get("exam_index", 0)

    if index >= len(preguntas):
        await finalizar_examen(query, context)
        return ConversationHandler.END

    p = preguntas[index]
    correcta = p["correcta"]
    es_correcta = (respuesta_idx == correcta)

    if es_correcta:
        context.user_data["exam_racha"] = context.user_data.get("exam_racha", 0) + 1
        racha = context.user_data["exam_racha"]
        bonus = BONUS_RACHA.get(racha, 0)
        puntos = PUNTOS_POR_RESPUESTA + bonus
        context.user_data["exam_score"] = context.user_data.get("exam_score", 0) + puntos
        bonus_txt = f"\n🔥 *¡Racha {racha}x! +{bonus} bonus!*" if bonus > 0 else ""
        feedback = f"✅ *¡CORRECTO!* +{PUNTOS_POR_RESPUESTA} pts{bonus_txt}\n\n💡 _{p['explicacion']}_"
    else:
        context.user_data["exam_racha"] = 0
        opcion_correcta = p["opciones"][correcta]
        feedback = f"❌ *Incorrecto.*\nRespuesta correcta: *{opcion_correcta}*\n\n💡 _{p['explicacion']}_"

    # Avanzar al siguiente
    context.user_data["exam_index"] = index + 1
    siguiente_index = context.user_data["exam_index"]
    total = len(preguntas)

    if siguiente_index >= total:
        btn_txt = "🏁 Ver Resultado Final"
    else:
        btn_txt = f"➡️ Siguiente Pregunta ({siguiente_index + 1}/{total})"

    keyboard = [[InlineKeyboardButton(btn_txt, callback_data="ans_next")]]

    await query.edit_message_text(feedback, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
    return RESPONDIENDO_EXAMEN


async def finalizar_examen(query, context):
    score = context.user_data.get("exam_score", 0)
    tipo = context.user_data.get("exam_tipo", "General")
    uid = context.user_data.get("exam_uid", "0")
    nombre = context.user_data.get("exam_nombre", "Jugador")
    total = len(context.user_data.get("exam_preguntas", []))

    # Guardar ranking
    ranking = cargar_ranking()
    if uid not in ranking:
        ranking[uid] = {"nombre": nombre, "puntos_totales": 0, "examenes": 0, "ultima_actividad": ""}
    ranking[uid]["puntos_totales"] += score
    ranking[uid]["examenes"] += 1
    ranking[uid]["ultima_actividad"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    ranking[uid]["nombre"] = nombre
    guardar_ranking(ranking)

    puntos_totales = ranking[uid]["puntos_totales"]
    nivel = get_nivel(puntos_totales)
    porcentaje = int((score / (total * PUNTOS_POR_RESPUESTA)) * 100) if total > 0 else 0

    if porcentaje >= 80:
        resultado_txt = "🔥 ¡Excelente resultado! Eres un jugador de alto nivel."
    elif porcentaje >= 60:
        resultado_txt = "💪 Buen resultado. Sigue estudiando para llegar al top."
    else:
        resultado_txt = "📚 Hay áreas por mejorar. Repasa los temas y vuelve a intentarlo."

    texto = (
        f"🏁 *EXAMEN COMPLETADO*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📋 {tipo}\n"
        f"✅ Puntos este examen: *+{score}*\n"
        f"📊 Porcentaje correcto: *{porcentaje}%*\n"
        f"🏆 Puntos totales: *{puntos_totales}*\n"
        f"🎖️ Nivel actual: *{nivel}*\n\n"
        f"{resultado_txt}"
    )

    keyboard = [
        [InlineKeyboardButton("📚 Otro Examen", callback_data="examenes")],
        [InlineKeyboardButton("🏆 Ver Ranking", callback_data="rank")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]

    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def mostrar_ranking_personal(query, user_id, username):
    ranking = cargar_ranking()
    if user_id not in ranking:
        await query.edit_message_text(
            "Aún no tienes puntos. ¡Haz tu primer examen! 📚",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📚 Hacer Examen", callback_data="examenes")]])
        )
        return

    datos = ranking[user_id]
    nivel = get_nivel(datos["puntos_totales"])
    sorted_rank = sorted(ranking.items(), key=lambda x: x[1]["puntos_totales"], reverse=True)
    posicion = next((i + 1 for i, (uid, _) in enumerate(sorted_rank) if uid == user_id), "?")

    texto = (
        f"🏆 *TU PERFIL DE RANKING*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 {datos['nombre']}\n"
        f"⭐ Puntos totales: *{datos['puntos_totales']}*\n"
        f"🎖️ Nivel: *{nivel}*\n"
        f"📊 Posición en equipo: *#{posicion}*\n"
        f"📚 Exámenes: {datos['examenes']}\n"
        f"⏰ Última actividad: {datos.get('ultima_actividad', 'N/A')}"
    )

    await query.edit_message_text(
        texto, parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("📚 Hacer Examen", callback_data="examenes")],
            [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
        ])
    )
