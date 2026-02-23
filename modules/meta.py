"""
modules/meta.py — Meta de armas, habilidades, combinaciones y mapas
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from data.meta import META_ARMAS, META_HABILIDADES, COMBINACIONES_META, MAPAS_BLOODSTRIKE


async def meta_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    texto = (
        "🔫 *META DE BLOOD STRIKE*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Conoce las armas y habilidades más poderosas\n"
        "del meta actual. ¡Úsalas a tu favor!\n\n"
        "Selecciona una categoría:"
    )

    keyboard = [
        [
            InlineKeyboardButton("🔫 SMG (Subfusil)", callback_data="meta_arma_SMG"),
            InlineKeyboardButton("⚔️ AR (Rifle)", callback_data="meta_arma_AR"),
        ],
        [
            InlineKeyboardButton("🎯 Francotirador", callback_data="meta_arma_Francotirador"),
            InlineKeyboardButton("📡 DMR", callback_data="meta_arma_DMR"),
        ],
        [
            InlineKeyboardButton("💥 Escopeta", callback_data="meta_arma_Escopeta"),
        ],
        [
            InlineKeyboardButton("💣 Habilidades Ofensivas", callback_data="meta_hab_ofensivas"),
            InlineKeyboardButton("🛡️ Habilidades Defensivas", callback_data="meta_hab_defensivas"),
        ],
        [
            InlineKeyboardButton("❤️ Habilidades de Soporte", callback_data="meta_hab_soporte"),
        ],
        [
            InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu"),
        ],
    ]

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def meta_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "meta":
        await meta_menu(update, context)
        return

    if data == "meta_mapas":
        await mostrar_mapas(update, context)
        return

    if data == "meta_combos":
        await mostrar_combos(update, context)
        return

    if data.startswith("meta_mapa_"):
        mapa = data.replace("meta_mapa_", "")
        await mostrar_detalle_mapa(update, context, mapa)
        return

    if data.startswith("meta_combo_"):
        combo = data.replace("meta_combo_", "").replace("_", " ")
        await mostrar_detalle_combo(update, context, combo)
        return

    if data.startswith("meta_arma_"):
        categoria = data.replace("meta_arma_", "")
        await mostrar_armas(update, context, categoria)
        return

    if data.startswith("meta_hab_"):
        tipo = data.replace("meta_hab_", "")
        await mostrar_habilidades(update, context, tipo)
        return


async def mostrar_armas(update, context, categoria):
    query = update.callback_query

    if categoria not in META_ARMAS:
        await query.answer("Categoría no disponible", show_alert=True)
        return

    armas = META_ARMAS[categoria]
    tier_emoji = {"S": "🔴", "A": "🟠", "B": "🟡", "C": "⚪"}

    texto = f"🔫 *{categoria} — META ACTUAL*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"

    for arma in armas:
        emoji = tier_emoji.get(arma["tier"], "⚪")
        acc_txt = " / ".join(arma.get("accesorios_meta", []))
        texto += (
            f"{emoji} *{arma['nombre']}* (Tier {arma['tier']})\n"
            f"🎯 Uso: {arma['uso']}\n"
            f"✅ {arma['ventajas']}\n"
            f"⚠️ {arma['contras']}\n"
            f"🔧 Accesorios: _{acc_txt}_\n\n"
        )

    keyboard = [
        [InlineKeyboardButton("⬅️ Ver otras armas", callback_data="meta")],
        [InlineKeyboardButton("💣 Ver Habilidades", callback_data="meta_hab_ofensivas")],
        [InlineKeyboardButton("🏠 Menú Principal", callback_data="volver_menu")],
    ]

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def mostrar_habilidades(update, context, tipo):
    query = update.callback_query

    if tipo not in META_HABILIDADES:
        await query.answer("Tipo no disponible", show_alert=True)
        return

    habs = META_HABILIDADES[tipo]
    titulos = {
        "ofensivas": "💥 HABILIDADES OFENSIVAS",
        "defensivas": "🛡️ HABILIDADES DEFENSIVAS",
        "soporte": "❤️ HABILIDADES DE SOPORTE",
    }

    texto = f"*{titulos.get(tipo, tipo)}*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"

    for h in habs:
        texto += f"🔸 *{h['nombre']}*\n  → {h['uso']}\n\n"

    keyboard = [
        [InlineKeyboardButton("🎯 Ver Combinaciones Meta", callback_data="meta_combos")],
        [InlineKeyboardButton("⬅️ Volver a Meta", callback_data="meta")],
    ]

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def mostrar_mapas(update, context):
    query = update.callback_query

    texto = (
        "🗺️ *TÁCTICAS POR MAPA*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Blood Strike cuenta con 3 mapas principales.\n"
        "Cada uno requiere una estrategia diferente.\n\n"
        "Selecciona un mapa:"
    )

    keyboard = []
    for mapa in MAPAS_BLOODSTRIKE.keys():
        keyboard.append([InlineKeyboardButton(f"🗺️ {mapa}", callback_data=f"meta_mapa_{mapa}")])

    keyboard.append([InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")])

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def mostrar_detalle_mapa(update, context, mapa):
    query = update.callback_query

    if mapa not in MAPAS_BLOODSTRIKE:
        await query.answer("Mapa no encontrado", show_alert=True)
        return

    m = MAPAS_BLOODSTRIKE[mapa]
    zonas_txt = " | ".join(m["zonas_clave"])

    texto = (
        f"🗺️ *{mapa.upper()}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📋 {m['descripcion']}\n\n"
        f"🔑 *Zonas clave:*\n_{zonas_txt}_\n\n"
        f"⚔️ *Estrategia de Ataque:*\n{m['estrategia_ataque']}\n\n"
        f"🛡️ *Estrategia de Defensa:*\n{m['estrategia_defensa']}\n\n"
        f"🎯 *Rol más importante aquí:*\n_{m['mejor_rol_aqui']}_"
    )

    keyboard = [
        [InlineKeyboardButton("🗺️ Ver otro mapa", callback_data="meta_mapas")],
        [InlineKeyboardButton("📚 Examen de este mapa", callback_data=f"exam_mapa_{mapa}")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def mostrar_combos(update, context):
    query = update.callback_query

    texto = (
        "🎯 *COMBINACIONES DE HABILIDADES META*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Estrategias completas para cada situación.\n"
        "Válidas para BE (Blood Edition) y TCT (Tactical).\n\n"
        "Selecciona una estrategia:"
    )

    keyboard = []
    for nombre in COMBINACIONES_META.keys():
        nombre_key = nombre.replace(" ", "_").replace("(", "").replace(")", "").replace("-", "")
        keyboard.append([InlineKeyboardButton(f"⚡ {nombre}", callback_data=f"meta_combo_{nombre_key}")])

    keyboard.append([InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")])

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def mostrar_detalle_combo(update, context, combo_key):
    query = update.callback_query

    # Buscar combo por nombre aproximado
    combo_data = None
    combo_nombre = None
    for nombre, data in COMBINACIONES_META.items():
        nombre_key = nombre.replace(" ", "_").replace("(", "").replace(")", "").replace("-", "")
        if nombre_key == combo_key or combo_key in nombre_key:
            combo_data = data
            combo_nombre = nombre
            break

    if not combo_data:
        await query.answer("Combo no encontrado", show_alert=True)
        return

    armas_txt = " / ".join(combo_data["armas"])
    habs_txt = " | ".join(combo_data["habilidades"])

    texto = (
        f"⚡ *{combo_nombre}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🎮 Modo: *{combo_data['modo']}*\n\n"
        f"📋 {combo_data['descripcion']}\n\n"
        f"🔫 *Armas recomendadas:*\n_{armas_txt}_\n\n"
        f"💣 *Habilidades:*\n_{habs_txt}_\n\n"
        f"📖 *Estrategia:*\n{combo_data['estrategia']}"
    )

    keyboard = [
        [InlineKeyboardButton("🎯 Ver otras combinaciones", callback_data="meta_combos")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
