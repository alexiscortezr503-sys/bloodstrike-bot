"""
data/entrenamiento.py — Planes de entrenamiento individuales y colectivos
"""

PLANES_INDIVIDUALES = {
    "anderson1": {  # IGL, 15 años, SMG corta
        "nombre": "Anderson (IGL)",
        "fase_actual": 1,
        "fases": {
            1: {
                "titulo": "Fase 1: Fundamentos de SMG (Semanas 1-2)",
                "ejercicios": [
                    {
                        "nombre": "Control de recoil MP5",
                        "descripcion": "En training mode, dispara cargadores completos contra pared a 10m. Observa el patrón y aprende a compensar hacia abajo+izquierda.",
                        "duracion": "15 min/día",
                        "dias": "Lunes, Miércoles, Viernes",
                    },
                    {
                        "nombre": "Duelos cortos 1v1",
                        "descripcion": "Practica 1v1 en modo personalizado contra un compañero a distancias 0-15m. Foco en no perder el duelo, no en kills.",
                        "duracion": "20 min",
                        "dias": "Martes, Jueves",
                    },
                    {
                        "nombre": "IGL timing training",
                        "descripcion": "En scrims, practica dar solo UNA orden clara antes de cada push. Elimina el ruido en el micrófono.",
                        "duracion": "Durante scrims",
                        "dias": "Todos los días de scrim",
                    },
                ],
                "meta": "Ganar 6/10 duelos a corta con MP5 antes de pasar a Fase 2",
            },
            2: {
                "titulo": "Fase 2: Toma de Decisiones (Semanas 3-4)",
                "ejercicios": [
                    {
                        "nombre": "Mapa mental pre-ronda",
                        "descripcion": "Antes de cada ronda, di en voz alta al equipo: qué estrategia van a usar y por qué. 10 segundos máximo.",
                        "duracion": "Cada ronda",
                        "dias": "Todos",
                    },
                    {
                        "nombre": "VOD review personal",
                        "descripcion": "Graba 2 scrims por semana. Observa específicamente tus órdenes: ¿fueron claras? ¿el equipo las siguió? ¿funcionaron?",
                        "duracion": "30 min x2 por semana",
                        "dias": "Fin de semana",
                    },
                ],
                "meta": "El equipo ejecuta el 80% de las órdenes del IGL correctamente",
            },
            3: {
                "titulo": "Fase 3: SMG Elite + Liderazgo Completo (Semanas 5-8)",
                "ejercicios": [
                    {
                        "nombre": "Aim training avanzado",
                        "descripcion": "Sesión diaria en training mode: 5 min recoil, 5 min tracking en movimiento, 5 min micro-adjust.",
                        "duracion": "15 min/día",
                        "dias": "Lunes a Viernes",
                    },
                    {
                        "nombre": "Mid-game adaptation",
                        "descripcion": "En scrims, practica cambiar la estrategia a la mitad si el plan A falla. Practica el reset táctico.",
                        "duracion": "Durante scrims",
                        "dias": "Todos los días de scrim",
                    },
                ],
                "meta": "IGL capaz de adaptar estrategia en tiempo real + duelo SMG consistente",
            },
        },
    },

    "jose": {  # Fragger, 14 años, SMG corta
        "nombre": "Jose (Fragger)",
        "fase_actual": 1,
        "fases": {
            1: {
                "titulo": "Fase 1: Mecánicas SMG Base (Semanas 1-2)",
                "ejercicios": [
                    {
                        "nombre": "Recoil mastery PP-19/MP5",
                        "descripcion": "Training mode: 200 balas contra pared por sesión. Patrón aprendido → empezar en bots estáticos → bots en movimiento.",
                        "duracion": "20 min/día",
                        "dias": "Lunes a Viernes",
                    },
                    {
                        "nombre": "Strafe training básico",
                        "descripcion": "Practica moverse izquierda-derecha mientras disparas a un blanco estático. El objetivo es mantener precisión mientras te mueves.",
                        "duracion": "10 min/día",
                        "dias": "Todos los días",
                    },
                    {
                        "nombre": "Entry simulation",
                        "descripcion": "Con un compañero: practica entrar a una habitación como si hubiera enemigo. Flash → entrada pegado a pared → limpiar ángulos.",
                        "duracion": "15 min",
                        "dias": "Martes, Jueves, Sábado",
                    },
                ],
                "meta": "Controlar recoil del SMG principal en menos de 10 días",
            },
            2: {
                "titulo": "Fase 2: Duelos Reales (Semanas 3-4)",
                "ejercicios": [
                    {
                        "nombre": "1v1 scrims cortos",
                        "descripcion": "Modo 1v1 solo con SMG, distancias 0-15m. Objetivo: entender ángulos óptimos de peekeo.",
                        "duracion": "25 min",
                        "dias": "Lunes, Miércoles, Viernes",
                    },
                    {
                        "nombre": "Jiggle peek training",
                        "descripcion": "Practica el peek rápido (salir 0.5 seg y volver) para obtener info sin morir. En cada duelo, primero jiggle, luego peek decisivo.",
                        "duracion": "15 min/día",
                        "dias": "Martes, Jueves",
                    },
                ],
                "meta": "Hacer 7/10 entries exitosos en simulación antes de Fase 3",
            },
        },
    },

    "xavier": {  # Ancla, 16 años, movimiento + aim todo rangos
        "nombre": "Xavier (Ancla)",
        "fase_actual": 1,
        "fases": {
            1: {
                "titulo": "Fase 1: Movimiento Base (Semanas 1-2)",
                "ejercicios": [
                    {
                        "nombre": "Crouch spam drill",
                        "descripcion": "En training mode, practica agacharte/levantarte mientras disparas. El objetivo es que sea fluido y natural, no robótico.",
                        "duracion": "10 min/día",
                        "dias": "Todos los días",
                    },
                    {
                        "nombre": "Strafe a distancias mixtas",
                        "descripcion": "Practica strafe tanto en corta (vs bots SMG) como en larga (vs bots AR). El movimiento debe adaptarse al arma que portas.",
                        "duracion": "20 min/día",
                        "dias": "Lunes, Miércoles, Viernes",
                    },
                    {
                        "nombre": "Peek angles en Aldea y Puerto",
                        "descripcion": "Explora cada ángulo de peekeo en estos mapas. Memorizalos. Saber el ángulo ANTES del duelo es una ventaja enorme.",
                        "duracion": "15 min",
                        "dias": "Martes, Jueves",
                    },
                ],
                "meta": "Ejecutar crouch-strafe de forma natural sin pensar en 10 días",
            },
            2: {
                "titulo": "Fase 2: Aim Multi-Rango (Semanas 3-5)",
                "ejercicios": [
                    {
                        "nombre": "Aim corta con SMG",
                        "descripcion": "Tracking de bots en movimiento a 0-15m. 100 eliminaciones de bots por sesión.",
                        "duracion": "15 min/día",
                        "dias": "Lunes, Miércoles, Viernes",
                    },
                    {
                        "nombre": "Aim larga con AR/DMR",
                        "descripcion": "Bots estáticos a 40-80m. Foco en centering (crosshair a cabeza) y disparo en pausa de strafe.",
                        "duracion": "15 min/día",
                        "dias": "Martes, Jueves, Sábado",
                    },
                ],
                "meta": "Ganar duelos en ambos rangos en 1v1 scrims",
            },
        },
    },

    "alejandro": {  # Soporte M+L, 18 años, centering + tracking
        "nombre": "Alejandro (Soporte Media y Larga)",
        "fase_actual": 1,
        "fases": {
            1: {
                "titulo": "Fase 1: Centering Profesional (Semanas 1-3)",
                "ejercicios": [
                    {
                        "nombre": "Crosshair placement consciencia",
                        "descripcion": "En cada partida, hay UN objetivo: tu crosshair debe estar a altura de cabeza AL ACERCARTE a cada esquina, pared o ángulo. No después — ANTES.",
                        "duracion": "Toda la partida",
                        "dias": "Todos",
                    },
                    {
                        "nombre": "Pre-aim training",
                        "descripcion": "En training mode, práctica llegar a cada ángulo con el crosshair EXACTAMENTE donde aparecerá el enemigo. Sin ajustar — ya debe estar ahí.",
                        "duracion": "15 min/día",
                        "dias": "Lunes a Viernes",
                    },
                    {
                        "nombre": "VOD review de centering",
                        "descripcion": "Graba partidas. Revisa específicamente: ¿cuántas veces tuviste que ajustar el crosshair al ver al enemigo? Reduce ese número.",
                        "duracion": "20 min x2/semana",
                        "dias": "Fin de semana",
                    },
                ],
                "meta": "Centering automático — sin pensar conscientemente en ello",
            },
            2: {
                "titulo": "Fase 2: Tracking Suave (Semanas 4-6)",
                "ejercicios": [
                    {
                        "nombre": "Tracking con SKS",
                        "descripcion": "Bots en movimiento lateral a 30-60m. El objetivo es seguir al bot SUAVEMENTE con el crosshair — sin micro-correcciones bruscas.",
                        "duracion": "20 min/día",
                        "dias": "Lunes, Miércoles, Viernes",
                    },
                    {
                        "nombre": "Flick + tracking combinado",
                        "descripcion": "Primero flick al objetivo (centering), luego tracking mientras se mueve. Simula el escenario real de combate.",
                        "duracion": "15 min",
                        "dias": "Martes, Jueves",
                    },
                ],
                "meta": "Tracking suave consistente en scrims de mediana distancia",
            },
        },
    },

    "maximiliano": {  # Soporte M+L, 14 años, todo desde cero
        "nombre": "Maximiliano (Jugador en Desarrollo)",
        "fase_actual": 1,
        "fases": {
            1: {
                "titulo": "Fase 1: Fundamentos Totales (Semanas 1-4)",
                "ejercicios": [
                    {
                        "nombre": "Sensibilidad base — ajuste progresivo",
                        "descripcion": "Empieza con la sensi recomendada para tu celular. No la cambies por 5 días. Luego ajusta solo 5 puntos si es necesario.",
                        "duracion": "Primeros 5 días sin cambiar",
                        "dias": "Semana 1",
                    },
                    {
                        "nombre": "Aim básico — bots estáticos",
                        "descripcion": "Training mode: 50 eliminaciones de bots ESTÁTICOS por sesión. Foco en impactar a la cabeza, no en velocidad.",
                        "duracion": "15 min/día",
                        "dias": "Lunes a Viernes",
                    },
                    {
                        "nombre": "Movimiento básico (Profeta-style)",
                        "descripcion": "Estudia videos de Profeta (pro player móvil) y practica: peek, retreat, strafe básico. UN movimiento nuevo por semana.",
                        "duracion": "10 min/día",
                        "dias": "Martes, Jueves, Sábado",
                    },
                    {
                        "nombre": "Conocer el mapa",
                        "descripcion": "Entra solo a partida personalizada y recorre los 3 mapas. Aprende todas las rutas, coberturas y ángulos antes de scrimmear.",
                        "duracion": "20 min",
                        "dias": "Semana 1-2",
                    },
                ],
                "meta": "Completar 1 semana de entrenamiento consistente = primera evaluación",
            },
            2: {
                "titulo": "Fase 2: Aim en Movimiento (Semanas 5-8)",
                "ejercicios": [
                    {
                        "nombre": "Aim corta distancia — bots en movimiento",
                        "descripcion": "Bots moviéndose a 0-15m. 80 eliminaciones por sesión. Permite que la mano 'sienta' el tracking.",
                        "duracion": "20 min/día",
                        "dias": "Lunes, Miércoles, Viernes",
                    },
                    {
                        "nombre": "Aim larga distancia — bots estáticos/lentos",
                        "descripcion": "A 40-70m, practica disparar entre respiraciones (pausa del movimiento). Centering perfecto antes de disparar.",
                        "duracion": "15 min",
                        "dias": "Martes, Jueves",
                    },
                    {
                        "nombre": "Movimiento profesional — aplicación real",
                        "descripcion": "En partidas normales, aplica conscientemente 1 técnica de movimiento por partida. No todas — una por vez.",
                        "duracion": "Durante partidas",
                        "dias": "Todos",
                    },
                ],
                "meta": "Eliminar 5 bots en movimiento consecutivos sin fallar a corta distancia",
            },
            3: {
                "titulo": "Fase 3: Integración Soporte (Semanas 9-12)",
                "ejercicios": [
                    {
                        "nombre": "Role training — soporte real",
                        "descripcion": "En scrims, tu único objetivo es: cubrir a tus compañeros, dar info de posición y curar. NO busques kills — vienen solos con el posicionamiento.",
                        "duracion": "Durante scrims",
                        "dias": "Todos los días de scrim",
                    },
                ],
                "meta": "Ser soporte confiable en el roster secundario",
            },
        },
    },

    "antonio": {  # Fragger Secundario, 18 años
        "nombre": "Antonio (Fragger Secundario)",
        "fase_actual": 1,
        "fases": {
            1: {
                "titulo": "Fase 1: Entry Agresivo (Semanas 1-3)",
                "ejercicios": [
                    {
                        "nombre": "Duelos puros 1v1",
                        "descripcion": "Modo 1v1 con compañeros. 20 duelos por sesión. Registra cuántos ganas. Objetivo: 60% de win rate en duelos.",
                        "duracion": "20 min",
                        "dias": "Lunes, Miércoles, Viernes",
                    },
                    {
                        "nombre": "Entry limpio sin morir innecesariamente",
                        "descripcion": "En scrims, si vas a entrar, ENTRA — sin detenerte. La duda en el entry es peor que el entry mismo.",
                        "duracion": "Durante scrims",
                        "dias": "Todos los días de scrim",
                    },
                ],
                "meta": "Hacer 3+ entries exitosos por partida en scrims",
            },
        },
    },

    "anderson2": {  # Sin rol definido, 16 años
        "nombre": "Anderson 2 (Rol en Evaluación)",
        "fase_actual": 1,
        "fases": {
            1: {
                "titulo": "Fase 1: Evaluación de Rol Natural (Semanas 1-2)",
                "ejercicios": [
                    {
                        "nombre": "Semana 1 — Fragger",
                        "descripcion": "Esta semana juega como Fragger. Tu objetivo es duelos y entries. Registra cómo te sientes — ¿es natural o forzado?",
                        "duracion": "Todas las partidas",
                        "dias": "Semana 1",
                    },
                    {
                        "nombre": "Semana 2 — Soporte",
                        "descripcion": "Esta semana juega como Soporte. Cubre, da info, mantente seguro. ¿Se siente más cómodo?",
                        "duracion": "Todas las partidas",
                        "dias": "Semana 2",
                    },
                    {
                        "nombre": "Aim multi-rango base",
                        "descripcion": "Training mode: 20 min entre corta y larga distancia. Esto sirve para cualquier rol que tome.",
                        "duracion": "20 min/día",
                        "dias": "Todos los días",
                    },
                ],
                "meta": "Definir rol con el coach al final de la semana 2 según resultados y preferencia",
            },
        },
    },
}

RUTINA_EQUIPO = {
    "titulo": "Rutina de Entrenamiento de Equipo",
    "frecuencia": "5 días/semana",
    "estructura": [
        {"bloque": "Warm-up individual", "duracion": "15 min", "descripcion": "Cada jugador hace aim training solo en training mode"},
        {"bloque": "Comunicación drill", "duracion": "10 min", "descripcion": "IGL practica dar órdenes, resto practica responder rápido"},
        {"bloque": "Táctica del día", "duracion": "10 min", "descripcion": "Coach explica 1 concepto táctico nuevo o repasa uno viejo"},
        {"bloque": "Scrim interno (2v2 o 4v4)", "duracion": "30 min", "descripcion": "Aplicar la táctica del día en scrim controlado"},
        {"bloque": "Review post-scrim", "duracion": "15 min", "descripcion": "Análisis sin culpas: ¿qué funcionó? ¿qué mejorar?"},
    ],
}
