"""
modules/scrims.py — Sistema de registro de scrims para jugadores
Los jugadores registran sus partidas, el coach las ve en su panel
"""

import json, os
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, ConversationHandler, MessageHandler, filters, CommandHandler

SCRIMS_FILE = "data/scrims.json"
ESPERANDO_SCRIM_KILLS = 30
ESPERANDO_SCRIM_DAÑO = 31
ESPERANDO_SCRIM_POSICION = 32
ESPERANDO_SCRIM_MAPA = 33
ESPERANDO_SCRIM_NOTAS = 34


def cargar_scrims():
    if os.path.exists(SCRIMS_FILE):
        with open(SCRIMS_FILE, "r") as f:
            return json.load(f)
    return {"entrenamiento": [], "liga": []}


def guardar_scrims(data):
    os.makedirs("data", exist_ok=True)
    with open(SCRIMS_FILE, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


async def scrims_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    texto = (
        "⚔️ *REGISTRAR PARTIDA*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Registra tus estadísticas después de cada scrim.\n"
        "El coach puede ver todos los resultados desde su panel.\n\n"
        "¿Qué tipo de scrim fue?"
    )
    keyboard = [
        [InlineKeyboardButton("🏋️ Scrim de Entrenamiento", callback_data="scrim_tipo_entrenamiento")],
        [InlineKeyboardButton("🏆 Scrim de Liga", callback_data="scrim_tipo_liga")],
        [InlineKeyboardButton("📋 Ver mis últimas partidas", callback_data="scrim_mis_partidas")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def scrim_tipo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    tipo = query.data.replace("scrim_tipo_", "")
    context.user_data["scrim_tipo"] = tipo
    context.user_data["scrim_jugador"] = query.from_user.first_name
    context.user_data["scrim_uid"] = str(query.from_user.id)

    tipo_txt = "ENTRENAMIENTO" if tipo == "entrenamiento" else "LIGA"
    texto = (
        f"📝 *Scrim de {tipo_txt}*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "¿En qué mapa jugaron?"
    )
    keyboard = [
        [InlineKeyboardButton("🏚️ Valle Abandonado", callback_data="scrim_mapa_Valle Abandonado")],
        [InlineKeyboardButton("🏖️ Playa Cielo", callback_data="scrim_mapa_Playa Cielo")],
        [InlineKeyboardButton("🏝️ Isla Siniestra", callback_data="scrim_mapa_Isla Siniestra")],
        [InlineKeyboardButton("❌ Cancelar", callback_data="scrims")],
    ]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
    return ESPERANDO_SCRIM_MAPA


async def scrim_mapa_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    mapa = query.data.replace("scrim_mapa_", "")
    context.user_data["scrim_mapa"] = mapa

    await query.edit_message_text(
        f"🗺️ Mapa: *{mapa}*\n\n✍️ Escribe tus *kills* (eliminaciones) en esta partida:\nEjemplo: `8`",
        parse_mode="Markdown"
    )
    return ESPERANDO_SCRIM_KILLS


async def scrim_kills_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.strip()
    try:
        kills = int(texto)
        context.user_data["scrim_kills"] = kills
        await update.message.reply_text(
            f"🔫 Kills: *{kills}*\n\n✍️ Escribe el *daño total* que hiciste:\nEjemplo: `1850`",
            parse_mode="Markdown"
        )
        return ESPERANDO_SCRIM_DAÑO
    except ValueError:
        await update.message.reply_text("Por favor escribe solo un número. Ejemplo: `8`", parse_mode="Markdown")
        return ESPERANDO_SCRIM_KILLS


async def scrim_daño_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.strip()
    try:
        daño = int(texto)
        context.user_data["scrim_daño"] = daño
        await update.message.reply_text(
            f"💥 Daño: *{daño}*\n\n✍️ ¿En qué *posición* terminó el equipo?\nEjemplo: `1` (si ganaron) o `4` si quedaron cuartos",
            parse_mode="Markdown"
        )
        return ESPERANDO_SCRIM_POSICION
    except ValueError:
        await update.message.reply_text("Por favor escribe solo un número. Ejemplo: `1850`", parse_mode="Markdown")
        return ESPERANDO_SCRIM_DAÑO


async def scrim_posicion_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    texto = update.message.text.strip()
    try:
        posicion = int(texto)
        context.user_data["scrim_posicion"] = posicion
        await update.message.reply_text(
            f"🏅 Posición: *#{posicion}*\n\n✍️ Escribe alguna nota sobre la partida (opcional):\nEjemplo: `Fallamos el rush a Prisión en la ronda 4` o escribe `no` para omitir",
            parse_mode="Markdown"
        )
        return ESPERANDO_SCRIM_NOTAS
    except ValueError:
        await update.message.reply_text("Por favor escribe solo un número. Ejemplo: `1`", parse_mode="Markdown")
        return ESPERANDO_SCRIM_POSICION


async def scrim_notas_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    notas = update.message.text.strip()
    if notas.lower() == "no":
        notas = ""

    # Guardar el scrim
    scrims = cargar_scrims()
    tipo = context.user_data.get("scrim_tipo", "entrenamiento")
    nuevo_scrim = {
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "jugador": context.user_data.get("scrim_jugador", "Jugador"),
        "uid": context.user_data.get("scrim_uid", "0"),
        "mapa": context.user_data.get("scrim_mapa", "N/A"),
        "kills": context.user_data.get("scrim_kills", 0),
        "daño": context.user_data.get("scrim_daño", 0),
        "posicion": context.user_data.get("scrim_posicion", 0),
        "resultado": f"{'🥇 Victoria' if context.user_data.get('scrim_posicion', 0) == 1 else '❌ Derrota'}",
        "notas": notas,
    }

    if tipo not in scrims:
        scrims[tipo] = []
    scrims[tipo].append(nuevo_scrim)
    guardar_scrims(scrims)

    tipo_txt = "Entrenamiento" if tipo == "entrenamiento" else "Liga"
    keyboard = [
        [InlineKeyboardButton("📝 Registrar otra", callback_data="scrims")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]
    await update.message.reply_text(
        f"✅ *¡Scrim de {tipo_txt} registrado!*\n\n"
        f"🗺️ Mapa: {nuevo_scrim['mapa']}\n"
        f"🔫 Kills: {nuevo_scrim['kills']}\n"
        f"💥 Daño: {nuevo_scrim['daño']}\n"
        f"🏅 Posición: #{nuevo_scrim['posicion']}\n\n"
        f"El coach puede ver tus resultados desde su panel. 🎮",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return ConversationHandler.END


async def mis_partidas_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    uid = str(query.from_user.id)
    nombre = query.from_user.first_name

    scrims = cargar_scrims()
    todas = scrims.get("entrenamiento", []) + scrims.get("liga", [])
    mias = [s for s in todas if s.get("uid") == uid]

    if not mias:
        await query.edit_message_text(
            "📋 No tienes partidas registradas aún.\n¡Registra tu próximo scrim!",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("📝 Registrar Scrim", callback_data="scrims")],
                [InlineKeyboardButton("⬅️ Menú", callback_data="volver_menu")],
            ])
        )
        return

    texto = f"📋 *TUS ÚLTIMAS PARTIDAS — {nombre}*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    for s in mias[-5:]:
        texto += (
            f"📅 {s.get('fecha', 'N/A')}\n"
            f"🗺️ {s.get('mapa', 'N/A')} | {s.get('resultado', '')}\n"
            f"🔫 {s.get('kills', 0)} kills | 💥 {s.get('daño', 0)} daño | 🏅 #{s.get('posicion', '?')}\n"
            + (f"📝 _{s.get('notas')}_\n" if s.get("notas") else "") + "\n"
        )

    # Promedios
    kills_prom = sum(s.get("kills", 0) for s in mias) / len(mias)
    daño_prom = sum(s.get("daño", 0) for s in mias) / len(mias)
    texto += f"📊 *Promedios:* {kills_prom:.1f} kills | {daño_prom:.0f} daño"

    keyboard = [
        [InlineKeyboardButton("📝 Registrar nueva", callback_data="scrims")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
