"""
data/psicologia.py — Psicología profesional completa + Psiquiatría
Basado en: TCC, Psicología Positiva, Psicología Deportiva, DSM-5, CIE-11
"""

# ═══════════════════════════════════════════════════════
# RESPUESTAS DE PSICOLOGÍA GENERAL (Desahogo emocional)
# ═══════════════════════════════════════════════════════

RESPUESTAS_PSICO_GENERAL = {
    "ansioso": {
        "respuesta": (
            "Gracias por contarme que te sientes ansioso. Eso requiere valentía. 💙\n\n"
            "La ansiedad es una respuesta natural del sistema nervioso ante una amenaza percibida. "
            "En el gaming, suele aparecer por miedo al error, a decepcionar al equipo, o a perder. "
            "Tu cerebro está en modo 'alerta' aunque no haya peligro real.\n\n"
            "🧘 *Técnica de regulación rápida — Respiración 4-7-8:*\n"
            "→ Inhala lentamente durante 4 segundos\n"
            "→ Sostén el aire durante 7 segundos\n"
            "→ Exhala despacio durante 8 segundos\n"
            "Repite 3 veces. Esto activa el nervio vago y reduce el cortisol.\n\n"
            "🧠 *Lo que dice la psicología cognitiva:*\n"
            "La ansiedad crece cuando ponemos el foco en el resultado ('¿y si perdemos?'). "
            "Cuando lo cambiamos al proceso ('¿qué puedo hacer YO en este momento?'), disminuye.\n\n"
            "¿Quieres contarme qué específicamente te genera esta ansiedad? Estoy aquí. 🤝"
        ),
    },
    "frustrado": {
        "respuesta": (
            "La frustración que sientes es válida y tiene una razón. 💙\n\n"
            "Desde la psicología, la frustración ocurre cuando hay una brecha entre lo que "
            "esperamos de nosotros mismos y lo que logramos. Eso significa que tienes estándares "
            "— y eso es positivo. El problema es cuando esa frustración se convierte en autocrítica destructiva.\n\n"
            "🛑 *Técnica del Semáforo (TCC):*\n"
            "🔴 Para. Respira. 10 segundos sin hacer nada.\n"
            "🟡 Analiza: ¿Qué pasó exactamente? ¿Qué estaba bajo tu control?\n"
            "🟢 Aprende: ¿Qué harías diferente? Luego sigue.\n\n"
            "🧠 *Reencuadre cognitivo:*\n"
            "❌ 'No sirvo para esto'\n"
            "✅ 'Todavía no domino esta parte — y eso es normal en el proceso'\n\n"
            "Los mejores jugadores del mundo se frustran. La diferencia es que procesan la emoción "
            "y la convierten en aprendizaje, no en autodestrucción. 💪\n\n"
            "¿Qué fue lo que te frustró? Cuéntame. 👂"
        ),
    },
    "enojado": {
        "respuesta": (
            "Entiendo que estás enojado. No voy a decirte que no te enojes — el enojo es una emoción legítima. 💙\n\n"
            "Lo que sí importa es cómo lo manejas, porque jugar con enojo activo es jugar "
            "con el lóbulo prefrontal (razonamiento) desactivado — tomas peores decisiones, "
            "rusheas sin pensar, culpas a otros. La neurociencia lo confirma.\n\n"
            "🥊 *Técnica de regulación del enojo:*\n"
            "1. PARA — sal del lobby si es necesario, no es cobardía\n"
            "2. DESCARGA física — 10 saltos, camina, toma agua fría\n"
            "3. NOMBRA la emoción en voz alta: 'Estoy enojado porque...'\n"
            "   Nombrarlo activa el córtex prefrontal y reduce la intensidad\n"
            "4. PREGÚNTATE: ¿Qué está bajo mi control en esta situación?\n"
            "5. VUELVE solo cuando estés en calma\n\n"
            "🧠 *Lo que la psicología dice del enojo en deportes:*\n"
            "Un nivel bajo de activación emocional mejora el rendimiento. "
            "El enojo descontrolado lo destruye. Los pros no tienen menos emociones — "
            "tienen mejor regulación emocional.\n\n"
            "¿Qué pasó? Puedes contarme. 💬"
        ),
    },
    "triste": {
        "respuesta": (
            "Gracias por confiarme cómo te sientes. Eso importa mucho. 💙\n\n"
            "La tristeza en el deporte y en el gaming es más común de lo que parece. "
            "Las derrotas, la presión de mejorar, los conflictos de equipo, o lo que pasa "
            "fuera de la pantalla — todo eso pesa.\n\n"
            "Lo que sientes es completamente humano y válido.\n\n"
            "💙 *Para este momento:*\n"
            "→ Date permiso de sentirte así — resistir la tristeza la hace más intensa\n"
            "→ Si puedes, habla con alguien de confianza (amigo, familiar)\n"
            "→ Descansa de la pantalla 20-30 minutos\n"
            "→ Haz algo pequeño que te guste: música, comida, aire fresco\n\n"
            "🧠 *Desde la psicología:*\n"
            "La tristeza persistente que no mejora después de unos días, "
            "que afecta el sueño, el apetito o las ganas de hacer cosas que antes disfrutabas, "
            "puede ser señal de que vale la pena hablar con un profesional. "
            "Eso no es debilidad — es cuidarse.\n\n"
            "Estoy aquí si quieres seguir hablando. 🤝"
        ),
    },
    "cansado": {
        "respuesta": (
            "El cansancio que sientes es real y merece ser atendido. 😴\n\n"
            "En el esports hay un mito peligroso: 'grindea más para mejorar'. "
            "La neurociencia dice lo contrario — *el descanso ES parte del entrenamiento*. "
            "Tu cerebro consolida lo aprendido mientras duermes (memoria procedural). "
            "Sin descanso, no hay mejora real.\n\n"
            "😴 *Lo que el cansancio le hace a tu juego:*\n"
            "→ Tiempo de reacción +20-30% más lento\n"
            "→ Peor toma de decisiones tácticas\n"
            "→ Menor control emocional (más tilt)\n"
            "→ Aim inconsistente\n\n"
            "🌿 *Protocolo de recuperación:*\n"
            "→ 8 horas de sueño mínimo — no es opcional, es entrenamiento\n"
            "→ No juegues ranked o scrims importantes hoy\n"
            "→ Come algo nutritivo — el azúcar da energía falsa que cae rápido\n"
            "→ 15 min de caminata activa el cerebro mejor que una energética\n\n"
            "El equipo te necesita en tu mejor versión. Descansar es profesional. 💙"
        ),
    },
    "nervioso": {
        "respuesta": (
            "Estar nervioso antes de algo importante es completamente normal. 😅\n\n"
            "Te cuento algo que cambia todo: los nervios NO son el enemigo. "
            "La psicología deportiva lo llama 'activación óptima' — un nivel medio de activación "
            "emocional MEJORA el rendimiento. Los atletas de élite no van en 0 — van en 7/10.\n\n"
            "El problema no son los nervios — es interpretarlos como amenaza en lugar de preparación.\n\n"
            "🎯 *Reencuadre cognitivo:*\n"
            "❌ 'Estoy nervioso, voy a jugar mal'\n"
            "✅ 'Mi cuerpo se está preparando para rendir al máximo'\n\n"
            "🎮 *Ritual pre-partido (5 minutos):*\n"
            "1. 3 respiraciones profundas — activa el sistema parasimpático\n"
            "2. Visualiza 1 jugada exitosa tuya específica\n"
            "3. Di internamente: 'Entrené para esto. Confío en mi equipo'\n"
            "4. Warm-up en training mode: 2-3 minutos de aim tranquilo\n\n"
            "Los pro-players tienen rituales pre-partido por esto exactamente. "
            "Con el tiempo, los nervios se convierten en combustible. 🔥"
        ),
    },
    "motivado": {
        "respuesta": (
            "¡Esa energía es poderosa! 🔥\n\n"
            "La motivación es el motor del rendimiento. Pero hay algo importante que la psicología "
            "deportiva enseña: *la motivación fluctúa, los hábitos permanecen*.\n\n"
            "Hoy tienes ganas — perfecto. Aprovéchalo para construir un hábito que te mantenga "
            "mejorando incluso en los días que la motivación no esté.\n\n"
            "💡 *Tipos de motivación (psicología del deporte):*\n"
            "→ Motivación intrínseca: mejorar porque disfrutas el proceso → MÁS duradera\n"
            "→ Motivación extrínseca: ganar, reconocimiento → útil pero frágil\n\n"
            "El objetivo es que tu motivación venga de adentro — del amor al juego y al proceso "
            "de mejorar. Eso no desaparece con una racha de derrotas.\n\n"
            "¿En qué vas a enfocar esta energía hoy? 🎯"
        ),
    },
    "presionado": {
        "respuesta": (
            "Sentir presión es señal de que estás en algo que importa. 💙\n\n"
            "La presión no es el problema — la *percepción* de la presión lo es. "
            "La misma situación que paraliza a un jugador, energiza a otro. "
            "La diferencia está en cómo interpretan esa presión.\n\n"
            "🧠 *La ciencia de la presión (psicología cognitiva):*\n"
            "Bajo presión, el cerebro activa el sistema de amenaza. "
            "Si lo reencuadras como 'desafío' en lugar de 'amenaza', "
            "activas el sistema de enfrentamiento — que da más energía y claridad.\n\n"
            "⚡ *Técnica de reencuadre bajo presión:*\n"
            "❌ 'Tengo que ganar o todo se derrumba'\n"
            "✅ 'Tengo la oportunidad de demostrar lo que entrené'\n\n"
            "❌ 'Si fallo, el equipo me va a odiar'\n"
            "✅ 'Este duelo es información — gane o pierda, aprendo'\n\n"
            "Respira, confía en tu entrenamiento, y ejecuta. 🎯"
        ),
    },
    "solo": {
        "respuesta": (
            "Gracias por decirme que te sientes solo. Eso requiere mucha honestidad. 💙\n\n"
            "La soledad en el gaming es más común de lo que parece — "
            "especialmente cuando el equipo no conecta emocionalmente o cuando "
            "el juego es el único espacio social disponible.\n\n"
            "Lo que sientes es real y válido.\n\n"
            "💙 *Algo importante:*\n"
            "Un equipo de esports no es solo táctica y habilidad — es también conexión humana. "
            "Los mejores equipos del mundo son los que se cuidan entre sí.\n\n"
            "Si la soledad va más allá del gaming y afecta tu día a día, "
            "hablar con alguien de confianza — un familiar, amigo, o profesional — "
            "siempre es una opción válida y valiente.\n\n"
            "¿Quieres hablar más sobre cómo te sientes? Aquí estoy. 🤝"
        ),
    },
}

# ═══════════════════════════════════════════════════════
# PSICOLOGÍA DEPORTIVA PROFESIONAL
# ═══════════════════════════════════════════════════════

PSICOLOGIA_DEPORTIVA = {
    "concentracion": {
        "titulo": "🎯 Concentración y Foco",
        "contenido": (
            "*¿Por qué te desconcentras en partida?*\n\n"
            "Según la psicología cognitiva, la atención tiene recursos limitados. "
            "Se pierde cuando procesamos pensamientos del pasado (error de la ronda anterior) "
            "o del futuro (¿y si perdemos?), en lugar del presente (¿qué hago AHORA?).\n\n"
            "🎯 *Técnica del Objetivo Micro (por ronda):*\n"
            "Antes de cada ronda elige UN solo foco:\n"
            "→ 'Esta ronda: centering perfecto'\n"
            "→ 'Esta ronda: comunicar cada enemigo que vea'\n"
            "→ 'Esta ronda: no salir a duelos innecesarios'\n"
            "Micro-objetivos = foco máximo. El marcador desaparece.\n\n"
            "🧠 *Mindfulness aplicado al gaming:*\n"
            "5 minutos antes de jugar:\n"
            "1. Siéntate, pon un timer de 5 min\n"
            "2. Enfoca toda la atención en la respiración\n"
            "3. Cuando la mente se vaya, regresa sin juzgarte\n"
            "Esto entrena el músculo de la concentración — literalmente. "
            "Los estudios muestran mejoras en 2-4 semanas de práctica diaria."
        ),
    },
    "presion": {
        "titulo": "⚡ Manejo de Presión",
        "contenido": (
            "*La presión no es el enemigo — la percepción lo es.*\n\n"
            "La psicología deportiva distingue dos respuestas ante la presión:\n"
            "🔴 *Respuesta de amenaza:* cortisol alto, vasos sanguíneos se contraen, rendimiento baja\n"
            "🟢 *Respuesta de desafío:* adrenalina+cortisol equilibrados, mayor flujo sanguíneo, rendimiento mejora\n\n"
            "La diferencia está en la interpretación, no en la situación.\n\n"
            "⚡ *Reencuadres para momentos de alta presión:*\n"
            "❌ 'Tengo que ganar o quedo mal' → ✅ 'Tengo la oportunidad de mostrar lo que entrené'\n"
            "❌ 'Si fallo, el equipo me odia' → ✅ 'El duelo es información, gane o pierda'\n"
            "❌ 'No puedo con esto' → ✅ 'He enfrentado situaciones difíciles antes y salí'\n\n"
            "🎯 *Protocolo de 3 segundos bajo presión:*\n"
            "1. Respira — 1 segundo\n"
            "2. Di internamente: 'Yo decidí estar aquí'\n"
            "3. Ejecuta lo que entrenaste — tu cuerpo sabe hacerlo\n\n"
            "La presión es privilegio. Significa que estás en algo que importa. 🏆"
        ),
    },
    "tilt": {
        "titulo": "🎮 Anti-Tilt",
        "contenido": (
            "*Tilt = estado emocional negativo que deteriora el rendimiento.*\n\n"
            "Desde la neurociencia: el tilt activa la amígdala (centro emocional) "
            "y desactiva el córtex prefrontal (razonamiento). Literalmente piensas peor.\n\n"
            "⚠️ *Señales de que estás en tilt:*\n"
            "→ Rusheas sin razón táctica\n"
            "→ Culpas al equipo o al juego por todo\n"
            "→ Juegas más rápido y con menos cuidado\n"
            "→ Sientes que 'el juego está buggeado' o 'hay trampa'\n\n"
            "🛑 *Protocolo Anti-Tilt (5 pasos):*\n"
            "1. RECONOCE que estás en tilt — el 80% no lo hace\n"
            "2. PARA — sal del lobby, no es rendirse\n"
            "3. CAMBIA el ambiente: levántate, agua, 5 min fuera\n"
            "4. PREGÚNTATE: ¿Qué puedo controlar yo en esto?\n"
            "5. VUELVE solo cuando estés emocionalmente en 0\n\n"
            "Perder 1 partida por tilt → seguir tilteado → perder 5 partidas. "
            "Vale más parar que perder en cascada. 🛑"
        ),
    },
    "confianza": {
        "titulo": "💪 Confianza y Autoeficacia",
        "contenido": (
            "*La confianza no es arrogancia — es la creencia de que puedes ejecutar lo que sabes hacer.*\n\n"
            "Albert Bandura (psicólogo) llama a esto 'autoeficacia': "
            "la convicción de que tienes la capacidad de lograr un resultado específico. "
            "Los jugadores con alta autoeficacia rinden mejor bajo presión.\n\n"
            "💪 *Cómo construir confianza real (no falsa):*\n"
            "1. *Logros pasados:* recuerda momentos específicos donde lo hiciste bien\n"
            "2. *Modelado:* observa jugadores que admiras — tu cerebro aprende viendo\n"
            "3. *Persuasión verbal:* el coach y el equipo dicen 'puedes' — y funciona\n"
            "4. *Estado físico:* postura erguida, respiración tranquila = más confianza\n\n"
            "🧠 *Técnica del Archivo de Éxitos:*\n"
            "Guarda en tu mente (o anota) 3-5 momentos donde jugaste bien. "
            "Antes de partidas importantes, repasa esos momentos. "
            "Tu cerebro no distingue bien entre recuerdo vívido y realidad — "
            "usa eso a tu favor.\n\n"
            "La confianza se entrena igual que el aim. 💪"
        ),
    },
    "comunicacion": {
        "titulo": "🗣️ Comunicación de Equipo",
        "contenido": (
            "*El equipo con mejor comunicación supera al equipo con mejor aim.*\n\n"
            "Esto no es una opinión — está respaldado por investigaciones en psicología de equipos deportivos. "
            "La comunicación efectiva reduce la 'carga cognitiva' de cada jugador: "
            "no tienes que procesar todo solo si tu equipo te da info.\n\n"
            "✅ *Comunicación profesional:*\n"
            "→ Info específica: 'Enemigo Prisión, MP7, poca vida' — NO 'hay uno ahí'\n"
            "→ Una persona habla a la vez en momentos de acción intensa\n"
            "→ Feedback positivo en el micrófono: 'Buen cover', 'Bien jugado'\n"
            "→ Crítica constructiva DESPUÉS de la ronda, nunca durante\n"
            "❌ Sin insultos, sin 'sos un inútil', sin tóxico\n\n"
            "🗣️ *Roles de comunicación:*\n"
            "• IGL: dicta timing y estrategia (voz principal)\n"
            "• Todos: info de posición de enemigos visible\n"
            "• Soporte: reporta utilidad disponible\n"
            "• Ancla: reporta estado de su zona\n\n"
            "La comunicación se entrena igual que el aim. Practíquela intencionalmente. 🎙️"
        ),
    },
    "objetivos": {
        "titulo": "🎯 Establecimiento de Objetivos",
        "contenido": (
            "*Sin objetivos claros, el entrenamiento es solo jugar.*\n\n"
            "La psicología del deporte diferencia tres tipos de objetivos:\n"
            "→ *Resultado:* ganar el torneo (poco control)\n"
            "→ *Rendimiento:* hacer X mecánica bien (más control)\n"
            "→ *Proceso:* enfocarme en centering cada ronda (control total)\n\n"
            "Los jugadores de élite enfocan el 80% en proceso y rendimiento, "
            "no en resultado. El resultado es consecuencia.\n\n"
            "📅 *Sistema de objetivos SMART para esports:*\n"
            "Semanal: 'Esta semana domino el peek con SMG en Valle'\n"
            "Mensual: 'Este mes mi centering es automático'\n"
            "Trimestral: 'En 3 meses somos el mejor equipo de la región'\n\n"
            "🔑 *Escribe tus objetivos.* Los estudios muestran que quienes escriben "
            "sus metas las logran hasta 3 veces más que quienes no lo hacen. ✍️"
        ),
    },
    "equipo": {
        "titulo": "🤝 Psicología de Equipo y Cohesión",
        "contenido": (
            "*Un equipo no es jugadores individuales — es un organismo.*\n\n"
            "La psicología del deporte estudia la 'cohesión de equipo': "
            "la fuerza que mantiene a un grupo unido hacia una meta. "
            "Los equipos con alta cohesión rinden mejor bajo presión.\n\n"
            "🤝 *Los 5 pilares de un equipo sólido:*\n\n"
            "1️⃣ *Confianza mutua:* cuando confías en tu compañero, no lo microgestiones. "
            "El IGL ordena, el fragger ejecuta con confianza.\n\n"
            "2️⃣ *Respeto en el error:* todos fallan. "
            "'Todos hemos estado ahí' > 'sos un inútil'.\n\n"
            "3️⃣ *Roles claros:* cada uno sabe qué debe hacer. "
            "La confusión de roles genera parálisis en momentos clave.\n\n"
            "4️⃣ *Celebración colectiva:* ganar juntos, perder juntos. "
            "Los equipos que se celebran entre sí tienen mejor química.\n\n"
            "5️⃣ *Review sin culpas:* la derrota más importante es la que más enseña. "
            "'¿Qué pudimos hacer mejor?' no '¿Por qué fallaste eso?'"
        ),
    },
    "visualizacion": {
        "titulo": "🧠 Visualización Mental",
        "contenido": (
            "*Los atletas de élite usan la visualización como entrenamiento — y funciona.*\n\n"
            "La neurociencia confirma que el cerebro activa los mismos circuitos neuronales "
            "cuando visualizas una acción que cuando la ejecutas. "
            "Es entrenamiento mental real, no solo motivación.\n\n"
            "🧠 *Ejercicio de visualización para Blood Strike (10 min):*\n\n"
            "1. Siéntate cómodo, cierra los ojos\n"
            "2. Visualiza el mapa donde van a jugar hoy\n"
            "3. Imagina en DETALLE una jugada tuya exitosa:\n"
            "   → El entry limpio\n"
            "   → El centering perfecto\n"
            "   → La comunicación exacta al equipo\n"
            "4. Siente la confianza de ejecutarla bien\n"
            "5. Repite 3 veces la misma jugada\n\n"
            "🎯 *Cuándo usarlo:*\n"
            "→ Noche antes de un torneo\n"
            "→ 10 min antes de una scrim importante\n"
            "→ Cuando estés en una racha de derrotas\n\n"
            "Los pro-players como los del equipo T1 (LoL) y top equipos de PUBG Mobile "
            "usan visualización como parte de su rutina. No es casualidad. 🏆"
        ),
    },
}

# ═══════════════════════════════════════════════════════
# PSIQUIATRÍA — SALUD MENTAL PROFUNDA
# ═══════════════════════════════════════════════════════

PSIQUIATRIA = {
    "que_es": {
        "titulo": "🏥 ¿Qué es la Psiquiatría?",
        "contenido": (
            "*La psiquiatría es la especialidad médica que estudia, diagnostica, previene y trata "
            "los trastornos mentales, emocionales y del comportamiento.*\n\n"
            "A diferencia del psicólogo (que trabaja con terapia), el psiquiatra es médico "
            "y puede prescribir medicación cuando es necesario.\n\n"
            "🧠 *¿Cuándo considerar ayuda psiquiátrica?*\n"
            "→ Tristeza o vacío que dura más de 2 semanas sin razón clara\n"
            "→ Ansiedad que afecta las actividades diarias (no solo el gaming)\n"
            "→ Problemas severos de sueño persistentes\n"
            "→ Pensamientos que no puedes controlar o que te asustan\n"
            "→ Cambios bruscos de humor sin causa aparente\n"
            "→ Dificultad para concentrarse que afecta tu vida\n\n"
            "⚠️ *Importante:* buscar ayuda psiquiátrica NO significa estar 'loco'. "
            "Significa que te cuidas. Igual que ir al médico por una lesión física.\n\n"
            "Si algo de lo anterior resuena contigo, habla con un adulto de confianza "
            "o busca un profesional. Es un acto de valentía. 💙"
        ),
    },
    "ansiedad_trastorno": {
        "titulo": "😰 Ansiedad — Más allá del nerviosismo normal",
        "contenido": (
            "*La ansiedad normal es adaptativa. La ansiedad como trastorno interfiere con la vida.*\n\n"
            "📋 *Diferencia clave:*\n"
            "→ Ansiedad normal: nerviosa antes de un torneo, se va al empezar\n"
            "→ Trastorno de ansiedad: la ansiedad es frecuente, intensa, difícil de controlar, "
            "y afecta el rendimiento y la vida diaria\n\n"
            "🔍 *Señales de alerta (según DSM-5):*\n"
            "→ Preocupación excesiva la mayoría de los días por 6+ meses\n"
            "→ Dificultad para controlar la preocupación\n"
            "→ Tensión muscular constante\n"
            "→ Problemas para dormir\n"
            "→ Irritabilidad\n"
            "→ Dificultad para concentrarse\n\n"
            "🛠️ *Qué ayuda (evidencia científica):*\n"
            "→ Terapia cognitivo-conductual (TCC) — gold standard\n"
            "→ Técnicas de relajación y mindfulness\n"
            "→ En casos moderados-severos: medicación (ansiolíticos) bajo supervisión médica\n"
            "→ Ejercicio regular — reduce ansiedad comprobadamente\n\n"
            "Si te identificas con varias de estas señales, habla con un profesional. 💙"
        ),
    },
    "depresion": {
        "titulo": "💙 Depresión — Más que tristeza",
        "contenido": (
            "*La depresión no es 'estar triste' — es un trastorno del estado de ánimo.*\n\n"
            "Es una de las condiciones más comunes y más tratables que existen. "
            "Afecta a millones de personas, incluidos atletas de alto rendimiento.\n\n"
            "🔍 *Señales de alerta (criterios DSM-5 — 5+ por 2 semanas):*\n"
            "→ Estado de ánimo deprimido la mayor parte del día\n"
            "→ Pérdida de interés en cosas que antes disfrutabas (¿el gaming ya no te da alegría?)\n"
            "→ Cambios en el peso o apetito\n"
            "→ Problemas para dormir o dormir demasiado\n"
            "→ Fatiga o pérdida de energía casi todos los días\n"
            "→ Sentimientos de inutilidad o culpa excesiva\n"
            "→ Dificultad para pensar o concentrarse\n"
            "→ Pensamientos de muerte o de hacerse daño\n\n"
            "🛠️ *Qué ayuda:*\n"
            "→ Terapia psicológica (TCC, terapia interpersonal)\n"
            "→ Antidepresivos bajo supervisión psiquiátrica (muy efectivos)\n"
            "→ Ejercicio físico regular — impacto comprobado\n"
            "→ Red de apoyo social\n\n"
            "⚠️ *Si tienes pensamientos de hacerte daño:* "
            "habla con alguien de confianza ahora mismo. "
            "En muchos países hay líneas de crisis disponibles 24/7. Pide ayuda. 💙"
        ),
    },
    "tdah": {
        "titulo": "⚡ TDAH y Gaming",
        "contenido": (
            "*El TDAH (Trastorno por Déficit de Atención e Hiperactividad) es muy común en gamers.*\n\n"
            "Paradójicamente, muchas personas con TDAH rinden muy bien en videojuegos "
            "porque la estimulación constante mantiene activo su sistema de dopamina. "
            "Pero fuera del juego, los desafíos son reales.\n\n"
            "🔍 *Señales de posible TDAH:*\n"
            "→ Dificultad para concentrarse en tareas que no son estimulantes\n"
            "→ Olvidar cosas frecuentemente\n"
            "→ Impulsividad (actúas antes de pensar)\n"
            "→ Dificultad para esperar tu turno o para escuchar\n"
            "→ Empezar muchas cosas pero no terminarlas\n"
            "→ Sensación de que tu mente 'corre' constantemente\n\n"
            "🎮 *TDAH en el gaming competitivo:*\n"
            "→ Puede afectar la toma de decisiones táctica (impulsividad)\n"
            "→ Puede dificultar seguir órdenes del IGL bajo presión\n"
            "→ Con el manejo adecuado, muchos pros tienen TDAH\n\n"
            "🛠️ *Qué ayuda:*\n"
            "→ Diagnóstico profesional (psicólogo o psiquiatra)\n"
            "→ Terapia conductual\n"
            "→ En muchos casos: medicación (metilfenidato, atomoxetina) muy efectiva\n"
            "→ Rutinas estructuradas y descansos programados\n\n"
            "El TDAH no es un obstáculo para ser pro — es un factor a manejar. 💙"
        ),
    },
    "burnout": {
        "titulo": "🔥 Burnout en Esports",
        "contenido": (
            "*El burnout es el agotamiento total — mental, emocional y físico — "
            "causado por el estrés crónico del entrenamiento y la competencia.*\n\n"
            "Es reconocido como un síndrome por la OMS (CIE-11) y es muy común en esports "
            "donde los jugadores 'grindean' muchas horas sin descanso adecuado.\n\n"
            "🔍 *3 dimensiones del burnout (Maslach):*\n"
            "1. *Agotamiento:* sin energía para nada, ni para jugar\n"
            "2. *Despersonalización:* cinismo, 'da igual ganar o perder'\n"
            "3. *Baja eficacia personal:* 'nada de lo que hago importa'\n\n"
            "⚠️ *Señales de alerta temprana:*\n"
            "→ El juego ya no te da alegría\n"
            "→ Irritabilidad constante con el equipo\n"
            "→ Fatiga que no mejora con dormir\n"
            "→ Rendimiento bajando a pesar de entrenar más\n\n"
            "🛠️ *Prevención y recuperación:*\n"
            "→ Descanso PLANIFICADO — 1-2 días sin gaming por semana\n"
            "→ Actividades fuera del gaming (deporte, amigos, hobbies)\n"
            "→ Comunicación abierta con el coach sobre el estado mental\n"
            "→ Si es severo: pausa del equipo y apoyo psicológico profesional\n\n"
            "Los equipos pro más exitosos del mundo tienen días de descanso obligatorios. "
            "No es debilidad — es estrategia. 🧠"
        ),
    },
}
