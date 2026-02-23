"""
modules/meta.py — Meta armas reales, mapas reales, utilidades reales y Strikers
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from data.meta import META_ARMAS, META_UTILIDADES, COMBINACIONES_META, COMBINACIONES_STRIKERS, MAPAS_BLOODSTRIKE, STRIKERS_BLOODSTRIKE


async def meta_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    texto = (
        "🔫 *META BLOOD STRIKE*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n"
        "Parche actualizado: *10/02/2026*\n\n"
        "Selecciona:"
    )
    keyboard = [
        [InlineKeyboardButton("🔫 SMG", callback_data="meta_arma_SMG"), InlineKeyboardButton("⚔️ AR", callback_data="meta_arma_AR")],
        [InlineKeyboardButton("🎯 Francotirador", callback_data="meta_arma_Francotirador"), InlineKeyboardButton("📡 DMR", callback_data="meta_arma_DMR")],
        [InlineKeyboardButton("💥 Escopeta", callback_data="meta_arma_Escopeta")],
        [InlineKeyboardButton("💣 Utilidades Reales", callback_data="meta_utilidades")],
        [InlineKeyboardButton("🗺️ Tácticas por Mapa", callback_data="meta_mapas")],
        [InlineKeyboardButton("⚡ Combinaciones Tácticas", callback_data="meta_combos")],
        [InlineKeyboardButton("🦾 Strikers — Combinaciones", callback_data="meta_strikers")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def meta_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "meta":
        await meta_menu(update, context)
    elif data == "meta_mapas":
        await mostrar_menu_mapas(query)
    elif data == "meta_combos":
        await mostrar_menu_combos(query)
    elif data == "meta_utilidades":
        await mostrar_utilidades(query)
    elif data == "meta_strikers":
        await mostrar_menu_strikers(query)
    elif data.startswith("meta_mapa_"):
        mapa = data.replace("meta_mapa_", "")
        await mostrar_detalle_mapa(query, mapa)
    elif data.startswith("meta_combo_"):
        idx = int(data.replace("meta_combo_", ""))
        await mostrar_detalle_combo(query, idx)
    elif data.startswith("meta_striker_combo_"):
        idx = int(data.replace("meta_striker_combo_", ""))
        await mostrar_detalle_striker_combo(query, idx)
    elif data.startswith("meta_striker_info_"):
        nombre = data.replace("meta_striker_info_", "")
        await mostrar_info_striker(query, nombre)
    elif data.startswith("meta_arma_"):
        cat = data.replace("meta_arma_", "")
        await mostrar_armas(query, cat)


async def mostrar_armas(query, categoria):
    if categoria not in META_ARMAS:
        await query.answer("Categoría no disponible", show_alert=True)
        return

    armas = META_ARMAS[categoria]
    tier_emoji = {"S": "🔴", "A": "🟠", "B": "🟡"}

    texto = f"🔫 *{categoria} — PARCHE 10/02/2026*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
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
        [InlineKeyboardButton("⚡ Ver Combinaciones", callback_data="meta_combos")],
        [InlineKeyboardButton("🏠 Menú Principal", callback_data="volver_menu")],
    ]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def mostrar_utilidades(query):
    texto = "💣 *UTILIDADES REALES DE BLOOD STRIKE*\n━━━━━━━━━━━━━━━━━━━━━━\n\n"
    for nombre, info in META_UTILIDADES.items():
        texto += (
            f"🔸 *{nombre}*\n"
            f"  {info['descripcion']}\n"
            f"  📌 Uso: {info['uso']}\n"
            f"  💡 Tip: _{info['tip']}_\n\n"
        )

    keyboard = [
        [InlineKeyboardButton("⚡ Combinaciones con Utilidades", callback_data="meta_combos")],
        [InlineKeyboardButton("⬅️ Menú Meta", callback_data="meta")],
    ]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def mostrar_menu_mapas(query):
    texto = "🗺️ *TÁCTICAS POR MAPA*\n━━━━━━━━━━━━━━━━━━━━━━\n\nSelecciona el mapa:"
    keyboard = [
        [InlineKeyboardButton("🏚️ Valle Abandonado (The Valley)", callback_data="meta_mapa_Valle Abandonado")],
        [InlineKeyboardButton("🏖️ Playa Cielo (Skyline Beach)", callback_data="meta_mapa_Playa Cielo")],
        [InlineKeyboardButton("🏝️ Isla Siniestra (Shutter Island)", callback_data="meta_mapa_Isla Siniestra")],
        [InlineKeyboardButton("⬅️ Menú Meta", callback_data="meta")],
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
        f"_(Nombre en juego: {m['nombre_ingles']})_\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📋 {m['tipo']}\n"
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
    texto = "⚡ *COMBINACIONES TÁCTICAS*\n━━━━━━━━━━━━━━━━━━━━━━\n\nArmas + Utilidades para BE y TCT:"
    keyboard = []
    for i, nombre in enumerate(COMBINACIONES_META.keys()):
        keyboard.append([InlineKeyboardButton(f"⚡ {nombre}", callback_data=f"meta_combo_{i}")])
    keyboard.append([InlineKeyboardButton("🦾 Combos de Strikers", callback_data="meta_strikers")])
    keyboard.append([InlineKeyboardButton("⬅️ Menú Meta", callback_data="meta")])
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def mostrar_detalle_combo(query, idx):
    nombres = list(COMBINACIONES_META.keys())
    if idx >= len(nombres):
        await query.answer("No encontrado", show_alert=True)
        return

    nombre = nombres[idx]
    c = COMBINACIONES_META[nombre]
    armas_txt = "\n".join([f"  • {a}" for a in c["armas"]])
    utils_txt = "\n".join([f"  • {u}" for u in c["utilidades"]])

    texto = (
        f"⚡ *{nombre}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"🎮 Modo: *{c['modo']}*\n"
        f"📋 _{c['descripcion']}_\n\n"
        f"🔫 *Armas:*\n{armas_txt}\n\n"
        f"💣 *Utilidades:*\n{utils_txt}\n\n"
        f"📖 *Estrategia:*\n{c['estrategia']}\n\n"
        f"🗺️ *Mejor en:* _{c['mejor_en']}_"
    )

    keyboard = [
        [InlineKeyboardButton("⬅️ Otras combinaciones", callback_data="meta_combos")],
        [InlineKeyboardButton("🦾 Combos de Strikers", callback_data="meta_strikers")],
        [InlineKeyboardButton("🏠 Menú Principal", callback_data="volver_menu")],
    ]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def mostrar_menu_strikers(query):
    texto = (
        "🦾 *STRIKERS — COMBINACIONES POR ESTILO*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Combinaciones de Strikers para cada estilo de juego:"
    )
    keyboard = []
    for i, nombre in enumerate(COMBINACIONES_STRIKERS.keys()):
        keyboard.append([InlineKeyboardButton(nombre, callback_data=f"meta_striker_combo_{i}")])
    keyboard.append([InlineKeyboardButton("📋 Info por Striker", callback_data="meta_striker_lista")])
    keyboard.append([InlineKeyboardButton("⬅️ Menú Meta", callback_data="meta")])
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def mostrar_detalle_striker_combo(query, idx):
    nombres = list(COMBINACIONES_STRIKERS.keys())
    if idx >= len(nombres):
        await query.answer("No encontrado", show_alert=True)
        return

    nombre = nombres[idx]
    c = COMBINACIONES_STRIKERS[nombre]
    strikers_txt = "\n".join([f"  • {s}" for s in c["strikers"]])
    armas_txt = "\n".join([f"  • {a}" for a in c["armas"]])
    utils_txt = "\n".join([f"  • {u}" for u in c["utilidades"]])

    texto = (
        f"🦾 *{nombre}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📋 _{c['descripcion']}_\n\n"
        f"👥 *Strikers recomendados:*\n{strikers_txt}\n\n"
        f"🔫 *Armas:*\n{armas_txt}\n\n"
        f"💣 *Utilidades:*\n{utils_txt}\n\n"
        f"📖 *Estrategia:*\n{c['estrategia']}\n\n"
        f"🗺️ *Mejor en:* _{c['mejor_en']}_\n"
        f"⚠️ *Debilidad:* _{c['debilidad']}_"
    )

    keyboard = [
        [InlineKeyboardButton("⬅️ Otros estilos", callback_data="meta_strikers")],
        [InlineKeyboardButton("🏠 Menú Principal", callback_data="volver_menu")],
    ]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def mostrar_info_striker(query, nombre):
    if nombre not in STRIKERS_BLOODSTRIKE:
        await query.answer("Striker no encontrado", show_alert=True)
        return

    s = STRIKERS_BLOODSTRIKE[nombre]
    texto = (
        f"🦾 *STRIKER: {nombre}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"⚡ *Habilidad activa:*\n_{s['habilidad_activa']}_\n\n"
        f"🔹 *Habilidad pasiva:*\n_{s['habilidad_pasiva']}_\n\n"
        f"🎮 *Estilo:* {s['estilo']}\n"
        f"🏆 *Mejor en:* {s['mejor_en']}\n"
        f"🔫 *Sinergias:* {s['sinergias']}"
    )

    keyboard = [
        [InlineKeyboardButton("⬅️ Lista de Strikers", callback_data="meta_striker_lista")],
        [InlineKeyboardButton("⬅️ Combinaciones", callback_data="meta_strikers")],
    ]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
