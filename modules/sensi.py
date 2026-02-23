"""
modules/sensi.py — Recomendación de sensibilidad por celular y rol
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from data.sensibilidad import SENSI_POR_DISPOSITIVO, LISTA_DISPOSITIVOS, CONSEJOS_SENSI
from data.jugadores import ROLES_DISPONIBLES


async def sensi_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    texto = (
        "📐 *SENSIBILIDAD AVANZADA — BLOOD STRIKE*\n"
        "━━━━━━━━━━━━━━━━━━━━━━\n\n"
        "Selecciona tu celular y rol para obtener\n"
        "tu sensibilidad base recomendada (X)(Y).\n\n"
        "¿Qué celular tienes?"
    )

    # Mostrar por marcas
    keyboard = []
    marcas = {}
    for dispositivo in LISTA_DISPOSITIVOS:
        marca = dispositivo.split()[0]
        if marca not in marcas:
            marcas[marca] = []
        marcas[marca].append(dispositivo)

    for marca, dispositivos in marcas.items():
        for d in dispositivos:
            d_key = d.replace(" ", "_")
            keyboard.append([InlineKeyboardButton(f"📱 {d}", callback_data=f"sensi_cel_{d_key}")])

    keyboard.append([InlineKeyboardButton("💡 Consejos de Sensibilidad", callback_data="sensi_consejos")])
    keyboard.append([InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")])

    await query.edit_message_text(
        texto,
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )


async def sensi_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    if data == "sensi_consejos":
        keyboard = [[InlineKeyboardButton("⬅️ Sensibilidades", callback_data="sensi")]]
        await query.edit_message_text(
            CONSEJOS_SENSI,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    if data.startswith("sensi_cel_"):
        dispositivo_key = data.replace("sensi_cel_", "")
        dispositivo = dispositivo_key.replace("_", " ")
        context.user_data["dispositivo_seleccionado"] = dispositivo

        # Mostrar roles
        texto = f"📱 *{dispositivo}*\n\n¿Cuál es tu rol?"
        keyboard = []
        for rol in ROLES_DISPONIBLES:
            rol_key = rol.replace(" ", "_")
            keyboard.append([InlineKeyboardButton(rol, callback_data=f"sensi_rol_{rol_key}")])
        keyboard.append([InlineKeyboardButton("⬅️ Cambiar celular", callback_data="sensi")])

        await query.edit_message_text(
            texto,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        return

    if data.startswith("sensi_rol_"):
        rol_key = data.replace("sensi_rol_", "")
        rol = rol_key.replace("_", " ")
        dispositivo = context.user_data.get("dispositivo_seleccionado", "")

        if not dispositivo or dispositivo not in SENSI_POR_DISPOSITIVO:
            await query.answer("Dispositivo no encontrado. Vuelve a seleccionar.", show_alert=True)
            return

        info = SENSI_POR_DISPOSITIVO[dispositivo]
        sensi_data = info["sensi"]

        # Buscar rol exacto o similar
        if rol in sensi_data:
            s = sensi_data[rol]
        else:
            # Buscar el más cercano
            s = sensi_data.get("Sin definir", {"x": 80, "y": 80, "giro": 85})

        texto = (
            f"📐 *SENSIBILIDAD RECOMENDADA*\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"📱 Celular: *{dispositivo}*\n"
            f"🎮 Rol: *{rol}*\n"
            f"📺 {info['pantalla']}\n\n"
            f"*Configuración Avanzada:*\n"
            f"  🔷 Sensibilidad X: *{s['x']}*\n"
            f"  🔶 Sensibilidad Y: *{s['y']}*\n"
            f"  🔄 Giro: *{s['giro']}*\n\n"
            f"ℹ️ *Nota del dispositivo:*\n_{info['nota']}_\n\n"
            f"⚠️ Esta es tu *base de inicio*.\n"
            f"Ajusta de a *5 puntos* según tu comodidad.\n"
            f"¡No cambies todos los días! Dale 1 semana mínimo."
        )

        keyboard = [
            [InlineKeyboardButton("💡 Cómo ajustar mi sensi", callback_data="sensi_consejos")],
            [InlineKeyboardButton("🔄 Cambiar rol", callback_data=f"sensi_cel_{dispositivo.replace(' ', '_')}")],
            [InlineKeyboardButton("📱 Cambiar celular", callback_data="sensi")],
            [InlineKeyboardButton("⬅️ Menú Principal", callback_data="volver_menu")],
        ]

        await query.edit_message_text(
            texto,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
