"""
modules/coach.py — Panel del Coach con contraseña y sistema de scrims
Contraseña: 2006
"""

import json, os
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler, MessageHandler, filters, CommandHandler
from modules.ranking import cargar_ranking

COACH_PASSWORD = "2006"
COACH_FILE = "data/scrims.json"
ESPERANDO_PASSWORD = 20
ESPERANDO_SCRIM_DATA = 21
ESPERANDO_SCRIM_TIPO = 22

COACH_TIPS = [
    "🎯 Anderson (IGL): Su toma de decisiones mejora cuando tiene 3 segundos para pensar antes de ordenar. Practicar briefings pre-ronda cortos y claros.",
    "🔥 Jose (Fragger): Necesita recordar que el Flash va ANTES de entrar, no después. Revisar timing de entry en cada scrim.",
    "🛡️ Xavier (Ancla): Tendencia a moverse de su zona sin avisar al IGL. Reforzar la regla: comunicar ANTES de rotar.",
    "📡 Alejandro (Soporte): Potencial alto con AR97 post-buff. Trabajar el centering a larga distancia con mira 4x — debe ser automático.",
    "⚡ Antonio (Fragger Entry): Agresividad alta — canalizar esa energía con timing. Primero Flash, luego entrada. No al revés.",
    "🎮 Anderson 2: En fase de definición de rol. Darle variedad de situaciones para descubrir dónde brilla naturalmente.",
    "🌱 Maximiliano: El jugador con mayor margen de mejora. Priorizar fundamentos sobre tácticas avanzadas — la base importa más.",
    "🧠 Equipo: El sistema Wildcard nuevo (parche 10/02/2026) abre nuevas combinaciones. Experimentar en scrims de entrenamiento antes de torneos.",
    "📊 Economía TCT: La reforma económica del parche 10/02/2026 cambió los precios. Revisar qué comprar en cada ronda según el dinero disponible.",
    "🗺️ Valle Abandonado: El equipo suele perder Observation Deck en el minuto 1. Establecer protocolo de toma de Observation Deck como prioridad máxima al inicio.",
    "🏝️ Isla Siniestra: El rush a Prisión debe ser sincronizado — si llegan en distintos tiempos, el primero muere solo. Practicar timing de llegada.",
    "🏖️ Playa Cielo: Skyline City es la trampa más común — el equipo la pelea de frente. Practicar el split: uno entra por Yacht Club mientras el otro entra por Cultural Center.",
    "💣 Utilidades: El equipo subestima la Granada Adhesiva. Es más precisa que la normal y funciona como trampa en corners — educar sobre su uso.",
    "🔫 HK416 nuevo: Evaluar si Anderson o Jose se benefician del HK416 con BAS Tipo C. La eliminación del retraso sprint/disparo puede cambiar el estilo de rush.",
    "📱 Sensi: Verificar que todos usan la sensibilidad avanzada (X)(Y) correcta para su celular. Una sensi inconsistente destruye el aim entrenado.",
    "🧘 Psicología: Si el equipo pierde 3 rondas seguidas, hacer pausa de 30 segundos antes de la siguiente. El tilt en cadena es el error más común en torneos.",
    "🎖️ Sistema Wildcard: Los Wildcards de rareza alta pueden cambiar el resultado de rondas. Investigar cuáles son más útiles para cada rol del equipo.",
    "⭐ Strikers: Revisar que cada jugador usa el Striker correcto para su rol. RAN/KRAKEN para fraggers, NOVA/ETHAN para IGL/soporte, VOLT/EMMA para ancla.",
]


def cargar_scrims():
    if os.path.exists(COACH_FILE):
        with open(COACH_FILE, "r") as f:
            return json.load(f)
    return {"entrenamiento": [], "liga": []}


def guardar_scrims(data):
    os.makedirs("data", exist_ok=True)
    with open(COACH_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


async def coach_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Si ya autenticado en esta sesión
    if context.user_data.get("coach_auth"):
        await mostrar_panel_coach(query, context)
        return

    # Pedir contraseña
    texto = (
        "🔐 *PANEL DEL COACH*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Este panel es exclusivo del Coach.\n\n"
        "✍️ Escribe la contraseña para continuar:"
    )
    keyboard = [[InlineKeyboardButton("❌ Cancelar", callback_data="volver_menu")]]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
    return ESPERANDO_PASSWORD


async def coach_password_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Verificar contraseña del coach"""
    password = update.message.text.strip()

    if password == COACH_PASSWORD:
        context.user_data["coach_auth"] = True
        await update.message.reply_text(
            "✅ *Acceso concedido. Bienvenido Coach Alexis.* 🎮",
            parse_mode="Markdown"
        )
        # Mostrar panel directamente
        keyboard = [
            [InlineKeyboardButton("📊 Ranking del Equipo", callback_data="coach_ranking")],
            [InlineKeyboardButton("⚔️ Scrims de Entrenamiento", callback_data="coach_scrims_entren")],
            [InlineKeyboardButton("🏆 Scrims de Liga", callback_data="coach_scrims_liga")],
            [InlineKeyboardButton("📝 Registrar Scrim", callback_data="coach_add_scrim")],
            [InlineKeyboardButton("💡 Tips de Coaching", callback_data="coach_tips")],
            [InlineKeyboardButton("📈 Estadísticas Generales", callback_data="coach_stats")],
            [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
        ]
        await update.message.reply_text(
            "📋 *PANEL DEL COACH*\n━━━━━━━━━━━━━━━━━━━━━━\nSelecciona una opción:",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
    else:
        await update.message.reply_text(
            "❌ Contraseña incorrecta. Inténtalo de nuevo o presiona /menu para cancelar."
        )
        return ESPERANDO_PASSWORD

    return ConversationHandler.END


async def mostrar_panel_coach(query, context):
    keyboard = [
        [InlineKeyboardButton("📊 Ranking del Equipo", callback_data="coach_ranking")],
        [InlineKeyboardButton("⚔️ Scrims de Entrenamiento", callback_data="coach_scrims_entren")],
        [InlineKeyboardButton("🏆 Scrims de Liga", callback_data="coach_scrims_liga")],
        [InlineKeyboardButton("📝 Registrar Scrim", callback_data="coach_add_scrim")],
        [InlineKeyboardButton("💡 Tips de Coaching", callback_data="coach_tips")],
        [InlineKeyboardButton("📈 Estadísticas Generales", callback_data="coach_stats")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]
    await query.edit_message_text(
        "📋 *PANEL DEL COACH*\n━━━━━━━━━━━━━━━━━━━━━━\nSelecciona una opción:",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def coach_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if not context.user_data.get("coach_auth"):
        await query.edit_message_text(
            "🔐 Necesitas autenticarte primero.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔑 Ir al Panel", callback_data="coach_menu")]])
        )
        return

    if data == "coach_ranking":
        await mostrar_ranking_coach(query)
    elif data == "coach_scrims_entren":
        await mostrar_scrims(query, "entrenamiento")
    elif data == "coach_scrims_liga":
        await mostrar_scrims(query, "liga")
    elif data == "coach_tips":
        await mostrar_tips_coach(query)
    elif data == "coach_stats":
        await mostrar_estadisticas(query)
    elif data == "coach_add_scrim":
        await iniciar_registro_scrim(query, context)
    elif data == "coach_back":
        await mostrar_panel_coach(query, context)


async def mostrar_ranking_coach(query):
    ranking = cargar_ranking()
    if not ranking:
        await query.edit_message_text(
            "📊 No hay datos de ranking aún. Los jugadores deben hacer exámenes.",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("⬅️ Panel", callback_data="coach_back")]])
        )
        return

    sorted_rank = sorted(ranking.items(), key=lambda x: x[1]["puntos_totales"], reverse=True)
    medallas = ["🥇", "🥈", "🥉"]
    texto = "📊 *RANKING COMPLETO DEL EQUIPO*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"

    for i, (uid, datos) in enumerate(sorted_rank):
        medal = medallas[i] if i < 3 else f"#{i+1}"
        texto += (
            f"{medal} *{datos['nombre']}*\n"
            f"   ⭐ {datos['puntos_totales']} pts | 📚 {datos['examenes']} exámenes\n"
            f"   ⏰ {datos.get('ultima_actividad', 'Sin actividad')}\n\n"
        )

    keyboard = [[InlineKeyboardButton("⬅️ Panel", callback_data="coach_back")]]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def mostrar_scrims(query, tipo):
    scrims = cargar_scrims()
    lista = scrims.get(tipo, [])
    tipo_txt = "ENTRENAMIENTO" if tipo == "entrenamiento" else "LIGA"

    if not lista:
        await query.edit_message_text(
            f"📋 No hay scrims de {tipo_txt} registrados aún.\n\nUsa 'Registrar Scrim' para agregar.",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📝 Registrar Scrim", callback_data="coach_add_scrim")],
                [InlineKeyboardButton("⬅️ Panel", callback_data="coach_back")],
            ])
        )
        return

    texto = f"⚔️ *SCRIMS DE {tipo_txt}*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    for s in lista[-8:]:  # Últimos 8
        texto += (
            f"📅 {s.get('fecha', 'N/A')} | {s.get('mapa', 'N/A')}\n"
            f"👤 {s.get('jugador', 'N/A')} — {s.get('resultado', 'N/A')}\n"
            f"🔫 Kills: {s.get('kills', 0)} | 💥 Daño: {s.get('daño', 0)}\n"
            f"🏅 Posición: #{s.get('posicion', '?')}\n"
            f"📝 {s.get('notas', '')}\n\n"
        )

    keyboard = [
        [InlineKeyboardButton("📝 Registrar Nuevo", callback_data="coach_add_scrim")],
        [InlineKeyboardButton("⬅️ Panel", callback_data="coach_back")],
    ]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def mostrar_tips_coach(query):
    import random
    tips_seleccionados = random.sample(COACH_TIPS, min(5, len(COACH_TIPS)))
    texto = "💡 *TIPS DE COACHING — BloodStrike Elite*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    for tip in tips_seleccionados:
        texto += f"{tip}\n\n"

    keyboard = [
        [InlineKeyboardButton("🔄 Más Tips", callback_data="coach_tips")],
        [InlineKeyboardButton("⬅️ Panel", callback_data="coach_back")],
    ]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def mostrar_estadisticas(query):
    scrims = cargar_scrims()
    entren = scrims.get("entrenamiento", [])
    liga = scrims.get("liga", [])
    ranking = cargar_ranking()

    total_scrims = len(entren) + len(liga)
    total_kills = sum(s.get("kills", 0) for s in entren + liga)
    total_daño = sum(s.get("daño", 0) for s in entren + liga)
    total_exams = sum(d.get("examenes", 0) for d in ranking.values())

    texto = (
        "📈 *ESTADÍSTICAS GENERALES*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        f"⚔️ Total scrims registrados: *{total_scrims}*\n"
        f"   • Entrenamiento: {len(entren)}\n"
        f"   • Liga: {len(liga)}\n\n"
        f"🔫 Kills totales del equipo: *{total_kills}*\n"
        f"💥 Daño total del equipo: *{total_daño}*\n\n"
        f"📚 Exámenes completados: *{total_exams}*\n"
        f"👥 Jugadores activos en ranking: *{len(ranking)}*\n"
    )

    keyboard = [[InlineKeyboardButton("⬅️ Panel", callback_data="coach_back")]]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def iniciar_registro_scrim(query, context):
    texto = (
        "📝 *REGISTRAR SCRIM*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "¿Qué tipo de scrim fue?"
    )
    keyboard = [
        [InlineKeyboardButton("🏋️ Scrim de Entrenamiento", callback_data="scrim_tipo_entrenamiento")],
        [InlineKeyboardButton("🏆 Scrim de Liga", callback_data="scrim_tipo_liga")],
        [InlineKeyboardButton("❌ Cancelar", callback_data="coach_back")],
    ]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
