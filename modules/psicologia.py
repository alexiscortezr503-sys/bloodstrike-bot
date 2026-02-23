"""
modules/psicologia.py — Psicología profesional + Psiquiatría
"""

import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler
from data.psicologia import RESPUESTAS_PSICO_GENERAL, PSICOLOGIA_DEPORTIVA, PSIQUIATRIA

ESPERANDO_SENTIMIENTO = 1
ESPERANDO_RESPUESTA_PSICO = 2


async def psico_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menú unificado de Psicología Deportiva"""
    query = update.callback_query
    await query.answer()

    texto = (
        "🧠 *PSICOLOGÍA DEPORTIVA*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "El rendimiento mental es tan importante como el aim.\n"
        "Los mejores equipos del mundo trabajan su mente igual que sus mecánicas.\n\n"
        "Selecciona un tema:"
    )

    keyboard = [
        [InlineKeyboardButton("😊 ¿Cómo te sientes hoy?", callback_data="psico_sentir")],
        [InlineKeyboardButton("━━━ PSICOLOGÍA DEPORTIVA ━━━", callback_data="psico_noop")],
        [InlineKeyboardButton("🎯 Concentración y Foco", callback_data="psico_dep_concentracion")],
        [InlineKeyboardButton("⚡ Manejo de Presión", callback_data="psico_dep_presion")],
        [InlineKeyboardButton("🎮 Anti-Tilt", callback_data="psico_dep_tilt")],
        [InlineKeyboardButton("💪 Confianza y Autoeficacia", callback_data="psico_dep_confianza")],
        [InlineKeyboardButton("🗣️ Comunicación de Equipo", callback_data="psico_dep_comunicacion")],
        [InlineKeyboardButton("🎯 Establecer Objetivos", callback_data="psico_dep_objetivos")],
        [InlineKeyboardButton("🤝 Psicología de Equipo", callback_data="psico_dep_equipo")],
        [InlineKeyboardButton("🧠 Visualización Mental", callback_data="psico_dep_visualizacion")],
        [InlineKeyboardButton("━━━ PSIQUIATRÍA ━━━", callback_data="psico_noop")],
        [InlineKeyboardButton("🏥 ¿Qué es la Psiquiatría?", callback_data="psico_psi_que_es")],
        [InlineKeyboardButton("😰 Ansiedad — Trastorno", callback_data="psico_psi_ansiedad_trastorno")],
        [InlineKeyboardButton("💙 Depresión", callback_data="psico_psi_depresion")],
        [InlineKeyboardButton("⚡ TDAH y Gaming", callback_data="psico_psi_tdah")],
        [InlineKeyboardButton("🔥 Burnout en Esports", callback_data="psico_psi_burnout")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def psico_deportiva_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Maneja callbacks de psicología deportiva y psiquiatría"""
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "psico_noop":
        return

    if data == "psico_dep":
        await psico_handler(update, context)
        return

    # Psicología deportiva
    if data.startswith("psico_dep_"):
        tema = data.replace("psico_dep_", "")
        if tema in PSICOLOGIA_DEPORTIVA:
            recurso = PSICOLOGIA_DEPORTIVA[tema]
            await mostrar_recurso(query, recurso["titulo"], recurso["contenido"])
        return

    # Psiquiatría
    if data.startswith("psico_psi_"):
        tema = data.replace("psico_psi_", "")
        if tema in PSIQUIATRIA:
            recurso = PSIQUIATRIA[tema]
            await mostrar_recurso(query, recurso["titulo"], recurso["contenido"])
        return


async def mostrar_recurso(query, titulo, contenido):
    texto = f"*{titulo}*\n━━━━━━━━━━━━━━━━━━━━━━\n\n{contenido}"
    keyboard = [
        [InlineKeyboardButton("😊 ¿Cómo me siento?", callback_data="psico_sentir")],
        [InlineKeyboardButton("⬅️ Psicología Deportiva", callback_data="psico_dep")],
        [InlineKeyboardButton("🏠 Menú Principal", callback_data="volver_menu")],
    ]
    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def como_te_sientes_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Inicio del flujo de bienestar emocional"""
    query = update.callback_query
    await query.answer()

    texto = (
        "💙 *¿CÓMO TE SIENTES HOY?*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Este es tu espacio seguro. 🔒\n"
        "Lo que escribas es solo para ayudarte — nadie más lo ve.\n\n"
        "Puedes escribir:\n"
        "• Una emoción: *ansioso, frustrado, enojado, triste, cansado...*\n"
        "• O simplemente cuéntame cómo estás con tus propias palabras.\n"
        "• No hay respuesta incorrecta.\n\n"
        "✍️ Escríbeme ahora:"
    )

    keyboard = [[InlineKeyboardButton("❌ Cancelar", callback_data="volver_menu")]]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
    return ESPERANDO_SENTIMIENTO


async def como_te_sientes_respuesta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Procesar el estado emocional con psicología profesional"""
    texto_usuario = update.message.text.lower().strip()
    emocion = detectar_emocion(texto_usuario)

    if emocion and emocion in RESPUESTAS_PSICO_GENERAL:
        respuesta = RESPUESTAS_PSICO_GENERAL[emocion]["respuesta"]
    else:
        respuesta = generar_respuesta_empatica(texto_usuario)

    keyboard = [
        [InlineKeyboardButton("💬 Seguir hablando", callback_data="psico_sentir")],
        [InlineKeyboardButton("🧠 Recursos de Psicología", callback_data="psico_dep")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]

    await update.message.reply_text(respuesta, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
    return ConversationHandler.END


def detectar_emocion(texto: str) -> str:
    """Detecta emoción con contexto — prioriza lo negativo"""

    # Frases negativas completas — máxima prioridad
    frases_enojo = ["enojado conmigo", "enojado con migo", "me da rabia", "me da coraje", "estoy harto", "estoy harta", "me odio", "no sirvo"]
    frases_frustrado = ["no sé jugar", "no se jugar", "no puedo", "siempre fallo", "siempre pierdo", "juego mal", "no mejoro", "nunca mejoro"]
    frases_triste = ["me rindo", "quiero dejarlo", "no tiene sentido", "para qué", "no vale la pena"]
    frases_presionado = ["mucha presión", "me presionan", "siento presión", "me estresa", "me estreso", "no aguanto"]
    frases_solo = ["me siento solo", "me siento sola", "nadie me entiende", "estoy solo", "estoy sola"]

    for f in frases_enojo:
        if f in texto:
            return "enojado"
    for f in frases_frustrado:
        if f in texto:
            return "frustrado"
    for f in frases_triste:
        if f in texto:
            return "triste"
    for f in frases_presionado:
        if f in texto:
            return "presionado"
    for f in frases_solo:
        if f in texto:
            return "solo"

    # Negaciones de positivos
    if any(n in texto for n in ["no estoy bien", "no me siento bien", "no ando bien", "no muy bien"]):
        return "triste"

    # Emociones negativas directas
    if any(p in texto for p in ["enojado", "enojada", "rabia", "ira", "furioso", "harto", "harta", "coraje", "odio"]):
        return "enojado"
    if any(p in texto for p in ["frustrado", "frustrada", "frustración", "desesperado"]):
        return "frustrado"
    if any(p in texto for p in ["triste", "tristeza", "llorar", "llorando", "deprimido", "deprimida", "bajoneado"]):
        return "triste"
    if any(p in texto for p in ["ansioso", "ansiosa", "ansiedad", "angustiado", "estresado", "estresada", "preocupado"]):
        return "ansioso"
    if any(p in texto for p in ["nervioso", "nerviosa", "nervios", "temblando"]):
        return "nervioso"
    if any(p in texto for p in ["cansado", "cansada", "agotado", "agotada", "sin energía", "sin ganas"]):
        return "cansado"

    # Positivas (solo si no hay contexto negativo)
    if any(p in texto for p in ["motivado", "motivada", "con ganas", "determinado", "enfocado"]):
        return "motivado"
    if any(p in texto for p in ["feliz", "contento", "contenta", "alegre", "genial", "excelente"]):
        return "feliz"

    # 'bien' solo si no hay negación cercana
    if "bien" in texto and not any(n in texto for n in ["no ", "ni ", "tampoco", "nunca"]):
        return "feliz"

    return None


def generar_respuesta_empatica(texto: str) -> str:
    respuestas = [
        (
            "Gracias por compartirlo conmigo. 💙\n\n"
            "Lo que describes suena importante. En el gaming de alto rendimiento, "
            "lo que sentimos afecta directamente cómo jugamos — "
            "eso lo confirma la psicología del deporte.\n\n"
            "¿Puedes contarme un poco más? ¿Tiene que ver con el juego, "
            "con el equipo, o es algo de afuera de las partidas? "
            "Quiero entenderte mejor para ayudarte mejor. 🤝"
        ),
        (
            "Te escucho. 💙\n\n"
            "Todo lo que sientes es válido. Los grandes jugadores no tienen "
            "menos emociones que los demás — aprenden a procesarlas mejor. "
            "Eso también se entrena.\n\n"
            "¿Qué está pasando? Cuéntame más. 👂"
        ),
        (
            "Aprecio que me lo cuentes. 💙\n\n"
            "Buscar apoyo emocional es una fortaleza, no una debilidad. "
            "Los equipos de esports de élite tienen psicólogos deportivos por exactamente esto.\n\n"
            "¿Qué está pesando hoy? Soy todo oídos. 🤝"
        ),
    ]
    return random.choice(respuestas)
