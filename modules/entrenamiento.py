"""
modules/entrenamiento.py — Planes de entrenamiento con fases navegables
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from data.entrenamiento import PLANES_INDIVIDUALES, RUTINA_EQUIPO


async def entren_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    texto = (
        "🏋️ *PLANES DE ENTRENAMIENTO*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Cada jugador tiene un plan personalizado\n"
        "con fases progresivas de desarrollo.\n\n"
        "Selecciona un jugador:"
    )

    keyboard = []
    for key, plan in PLANES_INDIVIDUALES.items():
        jug = plan["nombre"]
        roster = "🔴" if any(n in jug for n in ["Anderson (IGL)", "Jose", "Xavier", "Alejandro"]) else "🟡"
        keyboard.append([InlineKeyboardButton(f"{roster} {jug}", callback_data=f"entren_ver_{key}")])

    keyboard.append([InlineKeyboardButton("👥 Rutina de Equipo", callback_data="entren_equipo")])
    keyboard.append([InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")])

    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def entren_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "entren_equipo":
        await mostrar_rutina_equipo(query)
        return

    if data.startswith("entren_ver_"):
        key = data.replace("entren_ver_", "")
        if key in PLANES_INDIVIDUALES:
            await mostrar_fases_jugador(query, key)
        return

    if data.startswith("entren_fase_"):
        # formato: entren_fase_KEY_NUMFASE
        parts = data.replace("entren_fase_", "").rsplit("_", 1)
        if len(parts) == 2:
            key, num_str = parts
            try:
                num_fase = int(num_str)
                if key in PLANES_INDIVIDUALES:
                    await mostrar_detalle_fase(query, key, num_fase)
            except ValueError:
                pass
        return


async def mostrar_fases_jugador(query, key):
    plan = PLANES_INDIVIDUALES[key]
    fase_actual = plan["fase_actual"]
    total_fases = len(plan["fases"])

    texto = (
        f"🏋️ *{plan['nombre']}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📊 Fase actual: *{fase_actual} de {total_fases}*\n\n"
        f"Toca una fase para ver sus ejercicios:"
    )

    keyboard = []
    for num, fase in plan["fases"].items():
        if num < fase_actual:
            emoji = "✅"
        elif num == fase_actual:
            emoji = "▶️"
        else:
            emoji = "🔒"
        # Truncar título largo
        titulo_corto = fase["titulo"][:45] + ("..." if len(fase["titulo"]) > 45 else "")
        keyboard.append([InlineKeyboardButton(
            f"{emoji} {titulo_corto}",
            callback_data=f"entren_fase_{key}_{num}"
        )])

    keyboard.append([InlineKeyboardButton("⬅️ Ver todos los planes", callback_data="entren")])

    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def mostrar_detalle_fase(query, key, num_fase):
    plan = PLANES_INDIVIDUALES[key]
    if num_fase not in plan["fases"]:
        await query.answer("Fase no encontrada", show_alert=True)
        return

    fase = plan["fases"][num_fase]
    total_fases = len(plan["fases"])

    ejercicios_txt = ""
    for i, ej in enumerate(fase.get("ejercicios", []), 1):
        ejercicios_txt += (
            f"\n*{i}. {ej['nombre']}*\n"
            f"📝 {ej['descripcion']}\n"
            f"⏱️ _{ej['duracion']}_ | 📅 _{ej['dias']}_\n"
        )

    texto = (
        f"🏋️ *{fase['titulo']}*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"👤 {plan['nombre']} | Fase {num_fase}/{total_fases}\n"
        f"{ejercicios_txt}\n"
        f"🎯 *Meta:* _{fase.get('meta', 'Completar todos los ejercicios')}_"
    )

    keyboard = []
    # Navegación entre fases
    nav = []
    if num_fase > 1:
        nav.append(InlineKeyboardButton("⬅️ Fase anterior", callback_data=f"entren_fase_{key}_{num_fase - 1}"))
    if num_fase < total_fases:
        nav.append(InlineKeyboardButton("Siguiente fase ➡️", callback_data=f"entren_fase_{key}_{num_fase + 1}"))
    if nav:
        keyboard.append(nav)

    keyboard.append([InlineKeyboardButton("📋 Ver todas las fases", callback_data=f"entren_ver_{key}")])
    keyboard.append([InlineKeyboardButton("⬅️ Planes", callback_data="entren")])

    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))


async def mostrar_rutina_equipo(query):
    r = RUTINA_EQUIPO
    bloques_txt = ""
    for b in r["estructura"]:
        bloques_txt += f"\n⏱️ *{b['bloque']}* ({b['duracion']})\n_{b['descripcion']}_\n"

    texto = (
        f"👥 *RUTINA DE EQUIPO*\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"📋 {r['titulo']}\n"
        f"📅 Frecuencia: {r['frecuencia']}\n"
        f"{bloques_txt}"
    )

    keyboard = [
        [InlineKeyboardButton("👤 Planes individuales", callback_data="entren")],
        [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
    ]
    await query.edit_message_text(texto, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))
