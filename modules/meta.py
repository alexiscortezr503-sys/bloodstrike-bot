"""
modules/meta.py — Meta armas, mapas reales y combinaciones
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from data.meta import META_ARMAS, META_HABILIDADES, COMBINACIONES_META, MAPAS_BLOODSTRIKE


async def meta_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    texto = (
        "🔫 *META DE BLOOD STRIKE*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "Parche actualizado: *10/02/2026*\n\n"
        "Selecciona una categoría:"
    )

    keyboard = [
        [InlineKeyboardButton("🔫 SMG", callback_data="meta_arma_SMG"), InlineKeyboardButton("⚔️ AR (Rifle)", callback_data="meta_arma_AR")],
        [InlineKeyboardButton("🎯 Francotirador", callback_data="meta_arma_Francotirador"), InlineKeyboardButton("📡 DMR", callback_data="meta_arma_DMR")],
        [InlineKeyboardButton("💥 Escopeta", callback_data="meta_arma_Escopeta")],
        [InlineKeyboardButton("💣 Habilidades Ofensivas", callback_data="meta_hab_ofensivas")],
        [InlineKeyboardButton("🛡️ Defensivas", callback_data="meta_hab_defensivas"), InlineKeyboardButton("❤️ Soporte", callback_data="meta_hab_soporte")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]

    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def meta_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "meta":
        await meta_menu(update, context)
        return

    if data == "meta_mapas":
        await mostrar_menu_mapas(query)
        return

    if data == "meta_combos":
        await mostrar_menu_combos(query)
        return

    if data.startswith("meta_mapa_"):
        mapa = data.replace("meta_mapa_", "")
        await mostrar_detalle_mapa(query, mapa)
        return

    if data.startswith("meta_combo_"):
        idx = int(data.replace("meta_combo_", ""))
        await mostrar_detalle_combo(query, idx)
        return

    if data.startswith("meta_arma_"):
        cat = data.replace("meta_arma_", "")
        await mostrar_armas(query, cat)
        return

    if data.startswith("meta_hab_"):
        tipo = data.replace("meta_hab_", "")
        await mostrar_habilidades(query, tipo)
        return


async def mostrar_armas(query, categoria):
    if categoria not in META_ARMAS:
        await query.answer("Categoría no disponible", show_alert=True)
        return

    armas = META_ARMAS[categoria]
    tier_emoji = {"S": "🔴", "A": "🟠", "B": "🟡", "C": "⚪"}

    texto = f"🔫 *{categoria} — META PARCHE 10/02/2026*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    for a in armas:
        e = tier_emoji.get(a["tier"], "⚪")
        acc = " / ".join(a["accesorios_meta"])
        texto += (
            f"{e} *{a['nombre']}* (Tier {a['tier']})\n"
            f"🎯 _{a['uso']}_\n"
            f"✅ {a['ventajas']}\n"
            f"⚠️ {a['contras']}\n"
            f"🔧 {acc}\n"
            f"📋 {a['nota_parche']}\n\n"
        )

    keyboard = [
        [InlineKeyboardButton("⬅️ Otras armas", callback_data="meta")],
        [InlineKeyboardButton("🎯 Ver Combinaciones", callback_data="meta_combos")],
        [InlineKeyboardButton("🏠 Menú Principal", callback_data="volver_menu")],
    ]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def mostrar_habilidades(query, tipo):
    if tipo not in META_HABILIDADES:
        await query.answer("No disponible", show_alert=True)
        return

    titulos = {"ofensivas": "💥 OFENSIVAS", "defensivas": "🛡️ DEFENSIVAS", "soporte": "❤️ SOPORTE"}
    habs = META_HABILIDADES[tipo]

    texto = f"*{titulos.get(tipo, tipo)}*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    for h in habs:
        texto += f"🔸 *{h['nombre']}*\n  → {h['uso']}\n\n"

    keyboard = [
        [InlineKeyboardButton("🎯 Ver Combinaciones Meta", callback_data="meta_combos")],
        [InlineKeyboardButton("⬅️ Volver a Meta", callback_data="meta")],
    ]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def mostrar_menu_mapas(query):
    texto = (
        "🗺️ *TÁCTICAS POR MAPA*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Selecciona el mapa:"
    )
    keyboard = [
        [InlineKeyboardButton("🏚️ Valle Abandonado", callback_data="meta_mapa_Valle Abandonado")],
        [InlineKeyboardButton("🏖️ Playa Cielo", callback_data="meta_mapa_Playa Cielo")],
        [InlineKeyboardButton("🏝️ Isla Siniestra", callback_data="meta_mapa_Isla Siniestra")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def mostrar_detalle_mapa(query, mapa):
    if mapa not in MAPAS_BLOODSTRIKE:
        await query.answer("Mapa no encontrado", show_alert=True)
        return

    m = MAPAS_BLOODSTRIKE[mapa]
    zonas_txt = "\n".join([f"  🔹 *{z}:* {desc}" for z, desc in m["zonas_clave"].items()])

    texto = (
        f"🗺️ *{mapa.upper()}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📋 Tipo: {m['tipo']}\n"
        f"_{m['descripcion']}_\n\n"
        f"🔑 *Zonas clave:*\n{zonas_txt}\n\n"
        f"⚔️ *Ataque:*\n{m['estrategia_ataque']}\n\n"
        f"🛡️ *Defensa:*\n{m['estrategia_defensa']}\n\n"
        f"🔫 *Mejores armas:* _{m['mejor_arma']}_\n"
        f"🎮 *Mejor rol:* _{m['mejor_rol']}_\n"
        f"⚠️ *Peligros:* _{m['peligro']}_"
    )

    keyboard = [
        [InlineKeyboardButton("📚 Examen de este mapa", callback_data=f"exam_mapa_{mapa}")],
        [InlineKeyboardButton("⬅️ Otros mapas", callback_data="meta_mapas")],
        [InlineKeyboardButton("🏠 Menú Principal", callback_data="volver_menu")],
    ]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def mostrar_menu_combos(query):
    texto = (
        "🎯 *COMBINACIONES DE HABILIDADES META*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Estrategias completas para BE y TCT.\n"
        "Selecciona una:"
    )

    keyboard = []
    for i, nombre in enumerate(COMBINACIONES_META.keys()):
        keyboard.append([InlineKeyboardButton(f"⚡ {nombre}", callback_data=f"meta_combo_{i}")])

    keyboard.append([InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")])
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def mostrar_detalle_combo(query, idx):
    nombres = list(COMBINACIONES_META.keys())
    if idx >= len(nombres):
        await query.answer("Combo no encontrado", show_alert=True)
        return

    nombre = nombres[idx]
    c = COMBINACIONES_META[nombre]
    armas_txt = "\n".join([f"  • {a}" for a in c["armas"]])
    habs_txt = "\n".join([f"  • {h}" for h in c["habilidades"]])

    texto = (
        f"⚡ *{nombre}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🎮 Modo: *{c['modo']}*\n"
        f"📋 _{c['descripcion']}_\n\n"
        f"🔫 *Armas:*\n{armas_txt}\n\n"
        f"💣 *Habilidades:*\n{habs_txt}\n\n"
        f"📖 *Estrategia:*\n{c['estrategia']}\n\n"
        f"🗺️ *Mejor en:* _{c['mejor_en']}_"
    )

    keyboard = [
        [InlineKeyboardButton("⬅️ Otras combinaciones", callback_data="meta_combos")],
        [InlineKeyboardButton("🏠 Menú Principal", callback_data="volver_menu")],
    ]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
