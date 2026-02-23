#!/usr/bin/env python3
"""
BloodStrike Elite Bot v4 — Coach: Alexis Cortez
Novedades v4: donaciones, preguntas profesionales de combate real, ranking expandido
"""

import logging, os
from telegram import Update
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, filters, ConversationHandler
)

from modules.menu import menu_principal, handle_menu_callback
from modules.psicologia import (
    psico_handler, psico_deportiva_handler,
    como_te_sientes_start, como_te_sientes_respuesta,
    ESPERANDO_SENTIMIENTO
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
from modules.coach import (
    coach_menu, coach_handler, coach_password_handler,
    ESPERANDO_PASSWORD
)
from modules.scrims import (
    scrims_menu, scrim_tipo_handler, scrim_mapa_handler,
    scrim_kills_handler, scrim_daño_handler, scrim_posicion_handler,
    scrim_notas_handler, mis_partidas_handler,
    ESPERANDO_SCRIM_KILLS, ESPERANDO_SCRIM_DAÑO,
    ESPERANDO_SCRIM_POSICION, ESPERANDO_SCRIM_MAPA,
    ESPERANDO_SCRIM_NOTAS
)
from modules.donaciones import (
    donaciones_menu, donar_estrellas_handler, donar_ton_handler
)

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = os.getenv("BOT_TOKEN", "")
COACH_ID = int(os.getenv("COACH_ID", "0"))


def main():
    app = Application.builder().token(TOKEN).build()

    # ── Comandos ─────────────────────────────────────────────
    app.add_handler(CommandHandler("start", menu_principal))
    app.add_handler(CommandHandler("menu", menu_principal))

    # ── ConversationHandler: Psicología ─────────────────────
    conv_psico = ConversationHandler(
        entry_points=[CallbackQueryHandler(como_te_sientes_start, pattern="^psico_sentir$")],
        states={ESPERANDO_SENTIMIENTO: [MessageHandler(filters.TEXT & ~filters.COMMAND, como_te_sientes_respuesta)]},
        fallbacks=[CommandHandler("menu", menu_principal)],
        allow_reentry=True
    )
    app.add_handler(conv_psico)

    # ── ConversationHandler: Exámenes ────────────────────────
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

    # ── ConversationHandler: Panel Coach ────────────────────
    conv_coach = ConversationHandler(
        entry_points=[CallbackQueryHandler(coach_menu, pattern="^coach_menu$")],
        states={ESPERANDO_PASSWORD: [MessageHandler(filters.TEXT & ~filters.COMMAND, coach_password_handler)]},
        fallbacks=[CommandHandler("menu", menu_principal)],
        allow_reentry=True
    )
    app.add_handler(conv_coach)

    # ── ConversationHandler: Scrims ──────────────────────────
    conv_scrims = ConversationHandler(
        entry_points=[
            CallbackQueryHandler(scrims_menu, pattern="^scrims$"),
            CallbackQueryHandler(scrim_tipo_handler, pattern="^scrim_tipo_"),
        ],
        states={
            ESPERANDO_SCRIM_MAPA:     [CallbackQueryHandler(scrim_mapa_handler, pattern="^scrim_mapa_")],
            ESPERANDO_SCRIM_KILLS:    [MessageHandler(filters.TEXT & ~filters.COMMAND, scrim_kills_handler)],
            ESPERANDO_SCRIM_DAÑO:     [MessageHandler(filters.TEXT & ~filters.COMMAND, scrim_daño_handler)],
            ESPERANDO_SCRIM_POSICION: [MessageHandler(filters.TEXT & ~filters.COMMAND, scrim_posicion_handler)],
            ESPERANDO_SCRIM_NOTAS:    [MessageHandler(filters.TEXT & ~filters.COMMAND, scrim_notas_handler)],
        },
        fallbacks=[CommandHandler("menu", menu_principal)],
        allow_reentry=True
    )
    app.add_handler(conv_scrims)

    # ── Donaciones ───────────────────────────────────────────
    app.add_handler(CallbackQueryHandler(donaciones_menu,         pattern="^donaciones$"))
    app.add_handler(CallbackQueryHandler(donar_estrellas_handler, pattern="^donar_estrellas$"))
    app.add_handler(CallbackQueryHandler(donar_ton_handler,       pattern="^donar_ton$"))

    # ── Callbacks inline ─────────────────────────────────────
    app.add_handler(CallbackQueryHandler(psico_handler,           pattern="^psico_dep$"))
    app.add_handler(CallbackQueryHandler(psico_deportiva_handler, pattern="^psico_(dep_|psi_|noop)"))

    app.add_handler(CallbackQueryHandler(jugadores_menu,  pattern="^jugadores$"))
    app.add_handler(CallbackQueryHandler(jugador_handler, pattern="^jug_"))

    app.add_handler(CallbackQueryHandler(sensi_menu,    pattern="^sensi$"))
    app.add_handler(CallbackQueryHandler(sensi_handler, pattern="^sensi_"))

    app.add_handler(CallbackQueryHandler(meta_menu,    pattern="^meta$"))
    app.add_handler(CallbackQueryHandler(meta_handler, pattern="^meta_"))

    app.add_handler(CallbackQueryHandler(entren_menu,    pattern="^entren$"))
    app.add_handler(CallbackQueryHandler(entren_handler, pattern="^entren_"))

    app.add_handler(CallbackQueryHandler(ranking_handler,       pattern="^rank$"))
    app.add_handler(CallbackQueryHandler(coach_handler,         pattern="^coach_"))
    app.add_handler(CallbackQueryHandler(mis_partidas_handler,  pattern="^scrim_mis_partidas$"))

    # ── Volver al menú ───────────────────────────────────────
    app.add_handler(CallbackQueryHandler(handle_menu_callback, pattern="^volver_menu$"))
    app.add_handler(CallbackQueryHandler(handle_menu_callback))

    logger.info("🎮 BloodStrike Elite Bot v4 iniciado")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
