#!/usr/bin/env python3
"""
BloodStrike Elite Bot - Bot principal para equipo competitivo móvil
Coach: Alexis Cortez | Sistema: Arch Linux | Deploy: Railway
"""

import logging
import os
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ConversationHandler
)

from modules.menu import menu_principal, handle_menu_callback
from modules.psicologia import (
    psico_handler, psico_deportiva_handler,
    como_te_sientes_start, como_te_sientes_respuesta,
    ESPERANDO_SENTIMIENTO, ESPERANDO_RESPUESTA_PSICO
)
from modules.examenes import (
    examenes_menu, exam_handler, exam_answer_handler,
    SELECCION_EXAMEN, RESPONDIENDO_EXAMEN
)
from modules.jugadores import jugadores_menu, jugador_handler
from modules.sensi import sensi_menu, sensi_handler
from modules.meta import meta_menu, meta_handler
from modules.entrenamiento import entren_menu, entren_handler
from modules.ranking import ranking_handler
from modules.coach import coach_menu, coach_handler

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("BOT_TOKEN", "8698428588:AAHfxnFq2maUP_OfW9Pa4KB_v-o9_69yP_0")
COACH_ID = int(os.getenv("COACH_ID", "8495287319"))


def main():
    app = Application.builder().token(TOKEN).build()

    # ──────────── Comandos básicos ────────────
    app.add_handler(CommandHandler("start", menu_principal))
    app.add_handler(CommandHandler("menu", menu_principal))
    app.add_handler(CommandHandler("ranking", ranking_handler))
    app.add_handler(CommandHandler("meta", meta_handler))
    app.add_handler(CommandHandler("coach", coach_menu))

    # ──────────── ConversationHandler: ¿Cómo te sientes? ────────────
    conv_psico = ConversationHandler(
        entry_points=[CallbackQueryHandler(como_te_sientes_start, pattern="^psico_sentir$")],
        states={
            ESPERANDO_SENTIMIENTO: [MessageHandler(filters.TEXT & ~filters.COMMAND, como_te_sientes_respuesta)],
        },
        fallbacks=[CommandHandler("menu", menu_principal)],
        allow_reentry=True
    )
    app.add_handler(conv_psico)

    # ──────────── ConversationHandler: Exámenes ────────────
    conv_exam = ConversationHandler(
        entry_points=[CallbackQueryHandler(examenes_menu, pattern="^examenes$")],
        states={
            SELECCION_EXAMEN: [CallbackQueryHandler(exam_handler, pattern="^exam_")],
            RESPONDIENDO_EXAMEN: [CallbackQueryHandler(exam_answer_handler, pattern="^ans_")],
        },
        fallbacks=[CommandHandler("menu", menu_principal)],
        allow_reentry=True
    )
    app.add_handler(conv_exam)

    # ──────────── Callbacks generales (inline buttons) ────────────
    app.add_handler(CallbackQueryHandler(handle_menu_callback,        pattern="^main_"))
    app.add_handler(CallbackQueryHandler(jugadores_menu,              pattern="^jugadores$"))
    app.add_handler(CallbackQueryHandler(jugador_handler,             pattern="^jug_"))
    app.add_handler(CallbackQueryHandler(sensi_menu,                  pattern="^sensi$"))
    app.add_handler(CallbackQueryHandler(sensi_handler,               pattern="^sensi_"))
    app.add_handler(CallbackQueryHandler(meta_menu,                   pattern="^meta$"))
    app.add_handler(CallbackQueryHandler(meta_handler,                pattern="^meta_"))
    app.add_handler(CallbackQueryHandler(entren_menu,                 pattern="^entren$"))
    app.add_handler(CallbackQueryHandler(entren_handler,              pattern="^entren_"))
    app.add_handler(CallbackQueryHandler(psico_handler,               pattern="^psico$"))
    app.add_handler(CallbackQueryHandler(psico_deportiva_handler,     pattern="^psico_dep$"))
    app.add_handler(CallbackQueryHandler(coach_handler,               pattern="^coach_"))
    app.add_handler(CallbackQueryHandler(ranking_handler,             pattern="^rank$"))

    # Catch-all para evitar timeouts
    app.add_handler(CallbackQueryHandler(handle_menu_callback))

    logger.info("🎮 BloodStrike Elite Bot iniciado — 24/7 Railway")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
