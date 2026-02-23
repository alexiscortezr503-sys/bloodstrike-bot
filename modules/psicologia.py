"""
modules/psicologia.py — Módulo de psicología general y deportiva
"""

import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler
from data.psicologia import RESPUESTAS_PSICO_GENERAL, RECURSOS_PSICO_DEPORTIVA
from modules.menu import back_button

ESPERANDO_SENTIMIENTO = 1
ESPERANDO_RESPUESTA_PSICO = 2


async def psico_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Menú de psicología general"""
    query = update.callback_query
    await query.answer()

    texto = (
        "🧠 *PSICOLOGÍA DEPORTIVA*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "El rendimiento mental es tan importante como el aim.\n"
        "Los mejores jugadores del mundo trabajan su mente igual que sus mecánicas.\n\n"
        "📚 *Temas disponibles:*"
    )

    keyboard = []
    temas = {
        "concentracion": "🎯 Concentración y Foco",
        "presion": "⚡ Manejo de Presión",
        "tilt": "🎮 Anti-Tilt",
        "comunicacion": "🗣️ Comunicación de Equipo",
        "objetivos": "🎯 Establecer Objetivos",
        "trabajo_equipo": "🤝 Psicología de Equipo",
    }

    for key, label in temas.items():
        keyboard.append([InlineKeyboardButton(label, callback_data=f"psico_tema_{key}")])

    keyboard.append([InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")])

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def psico_deportiva_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Mostrar tema específico de psicología deportiva"""
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "psico_dep":
        await psico_handler(update, context)
        return

    if data.startswith("psico_tema_"):
        tema = data.replace("psico_tema_", "")
        if tema in RECURSOS_PSICO_DEPORTIVA:
            recurso = RECURSOS_PSICO_DEPORTIVA[tema]
            texto = f"*{recurso['titulo']}*\n━━━━━━━━━━━━━━━━━━━━━━\n\n{recurso['contenido']}"

            keyboard = [
                [InlineKeyboardButton("📚 Ver otro tema", callback_data="psico_dep")],
                [InlineKeyboardButton("😊 ¿Cómo me siento?", callback_data="psico_sentir")],
                [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
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
        "Este es tu espacio seguro. Aquí puedes ser honesto/a.\n"
        "Lo que escribas no se comparte con nadie.\n\n"
        "Puedes escribir:\n"
        "• Una emoción: *ansioso, feliz, triste, frustrado, enojado...*\n"
        "• O simplemente cuéntame cómo estás en tus propias palabras.\n\n"
        "Escríbeme ahora 👇"
    )

    keyboard = [[InlineKeyboardButton("❌ Cancelar", callback_data="volver_menu")]]

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

    return ESPERANDO_SENTIMIENTO


async def como_te_sientes_respuesta(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Procesar el estado emocional del jugador"""
    texto_usuario = update.message.text.lower().strip()

    # Detectar emoción del texto
    emocion_detectada = detectar_emocion(texto_usuario)

    if emocion_detectada and emocion_detectada in RESPUESTAS_PSICO_GENERAL:
        respuesta_data = RESPUESTAS_PSICO_GENERAL[emocion_detectada]
        respuesta = respuesta_data["respuesta"]
    else:
        # Respuesta genérica empática
        respuesta = generar_respuesta_empatica(texto_usuario)

    keyboard = [
        [InlineKeyboardButton("💬 Seguir hablando", callback_data="psico_sentir")],
        [InlineKeyboardButton("🧠 Recursos de Psicología", callback_data="psico_dep")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]

    await update.message.reply_text(
        respuesta,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

    return ConversationHandler.END


def detectar_emocion(texto: str) -> str:
    """Detecta la emoción principal del texto del usuario"""
    palabras_clave = {
        "ansioso": ["ansioso", "ansiosa", "ansiedad", "nervioso", "preocupado", "preocupada", "estrés", "estresado"],
        "frustrado": ["frustrado", "frustrada", "frustración", "no puedo", "imposible", "siempre fallo", "mal"],
        "feliz": ["feliz", "bien", "contento", "contenta", "alegre", "genial", "excelente", "top"],
        "triste": ["triste", "tristeza", "llorar", "deprimido", "deprimida", "bajoneado", "bajoneada"],
        "enojado": ["enojado", "enojada", "enojo", "rabia", "ira", "molesto", "molesta", "odio"],
        "cansado": ["cansado", "cansada", "cansancio", "agotado", "agotada", "sin energía", "dormido"],
        "nervioso": ["nervioso", "nerviosa", "nervios", "torneo", "scrim", "importante", "competencia"],
        "motivado": ["motivado", "motivada", "ganas", "quiero ganar", "determinado", "enfocado"],
    }

    for emocion, palabras in palabras_clave.items():
        for palabra in palabras:
            if palabra in texto:
                return emocion

    return None


def generar_respuesta_empatica(texto: str) -> str:
    """Genera una respuesta empática cuando no se detecta emoción específica"""
    respuestas = [
        (
            f"Gracias por compartirlo conmigo. 💙\n\n"
            f"Lo que describes suena importante. En el gaming de alto rendimiento, "
            f"lo que sentimos afecta directamente cómo jugamos.\n\n"
            f"¿Puedes contarme un poco más? ¿Esto tiene que ver con el juego, "
            f"con el equipo, o es algo de fuera de las partidas? "
            f"Quiero entenderte mejor para ayudarte mejor. 🤝"
        ),
        (
            f"Te escucho. 💙\n\n"
            f"Todo lo que sientes es válido. Los grandes jugadores no son "
            f"los que no sienten — son los que aprenden a procesar lo que sienten.\n\n"
            f"¿Hay algo específico que está pesando? Cuéntame más. 👂"
        ),
        (
            f"Aprecio que me lo cuentes. 💙\n\n"
            f"Recuerda: buscar apoyo emocional es una fortaleza, no una debilidad. "
            f"Los equipos de esports de élite tienen psicólogos por exactamente esto.\n\n"
            f"¿Qué está pasando? Soy todo oídos. 🤝"
        ),
    ]

    return random.choice(respuestas)
