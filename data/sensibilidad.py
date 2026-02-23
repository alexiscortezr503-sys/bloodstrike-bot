"""
data/sensibilidad.py — Base de sensibilidades avanzadas (X)(Y) por celular y rol
"""

# Referencia de sensibilidades avanzadas Blood Strike
# Formato: {"x": valor, "y": valor} — se ajusta según el jugador
# Escala 0-100 donde 50 es media

SENSI_POR_DISPOSITIVO = {
    # ─────────────── SAMSUNG ───────────────────────────────────────────────
    "Samsung Galaxy A54": {
        "pantalla": "6.4 pulgadas | FHD+ | 120Hz",
        "nota": "Buen equilibrio, 120Hz ayuda la fluidez del aim",
        "sensi": {
            "IGL":                  {"x": 82, "y": 82, "giro": 90},
            "Fragger":              {"x": 90, "y": 90, "giro": 100},
            "Entry Fragger":        {"x": 95, "y": 95, "giro": 100},
            "Ancla":                {"x": 78, "y": 78, "giro": 85},
            "Soporte Media":        {"x": 70, "y": 68, "giro": 78},
            "Soporte Larga":        {"x": 60, "y": 58, "giro": 65},
            "Soporte Media y Larga":{"x": 65, "y": 63, "giro": 70},
            "Sin definir":          {"x": 80, "y": 80, "giro": 85},
        },
    },
    "Samsung Galaxy A34": {
        "pantalla": "6.6 pulgadas | FHD+ | 120Hz",
        "nota": "Pantalla grande — reducir un poco la sensi respecto a A54",
        "sensi": {
            "IGL":                  {"x": 78, "y": 78, "giro": 88},
            "Fragger":              {"x": 87, "y": 87, "giro": 98},
            "Entry Fragger":        {"x": 92, "y": 92, "giro": 100},
            "Ancla":                {"x": 75, "y": 75, "giro": 82},
            "Soporte Media":        {"x": 67, "y": 65, "giro": 75},
            "Soporte Larga":        {"x": 57, "y": 55, "giro": 62},
            "Soporte Media y Larga":{"x": 62, "y": 60, "giro": 68},
            "Sin definir":          {"x": 78, "y": 78, "giro": 82},
        },
    },
    "Samsung Galaxy A14": {
        "pantalla": "6.6 pulgadas | FHD+ | 90Hz",
        "nota": "90Hz — puede sentirse menos fluido, subir ligeramente la sensi",
        "sensi": {
            "IGL":                  {"x": 85, "y": 85, "giro": 92},
            "Fragger":              {"x": 93, "y": 93, "giro": 100},
            "Entry Fragger":        {"x": 97, "y": 97, "giro": 100},
            "Ancla":                {"x": 80, "y": 80, "giro": 88},
            "Soporte Media":        {"x": 72, "y": 70, "giro": 80},
            "Soporte Larga":        {"x": 62, "y": 60, "giro": 68},
            "Soporte Media y Larga":{"x": 67, "y": 65, "giro": 73},
            "Sin definir":          {"x": 83, "y": 83, "giro": 87},
        },
    },
    "Samsung Galaxy S23": {
        "pantalla": "6.1 pulgadas | FHD+ | 120Hz",
        "nota": "Premium, pantalla chica = sensi más controlable, ideal para fragmentación",
        "sensi": {
            "IGL":                  {"x": 80, "y": 80, "giro": 88},
            "Fragger":              {"x": 88, "y": 88, "giro": 98},
            "Entry Fragger":        {"x": 93, "y": 93, "giro": 100},
            "Ancla":                {"x": 76, "y": 76, "giro": 83},
            "Soporte Media":        {"x": 68, "y": 66, "giro": 76},
            "Soporte Larga":        {"x": 58, "y": 56, "giro": 63},
            "Soporte Media y Larga":{"x": 63, "y": 61, "giro": 69},
            "Sin definir":          {"x": 80, "y": 80, "giro": 84},
        },
    },

    # ─────────────── XIAOMI / REDMI ────────────────────────────────────────
    "Redmi Note 12": {
        "pantalla": "6.67 pulgadas | FHD+ | 120Hz",
        "nota": "Pantalla grande fluida, buen para gaming, sensi media-baja",
        "sensi": {
            "IGL":                  {"x": 77, "y": 77, "giro": 86},
            "Fragger":              {"x": 86, "y": 86, "giro": 96},
            "Entry Fragger":        {"x": 91, "y": 91, "giro": 100},
            "Ancla":                {"x": 74, "y": 74, "giro": 81},
            "Soporte Media":        {"x": 66, "y": 64, "giro": 73},
            "Soporte Larga":        {"x": 56, "y": 54, "giro": 61},
            "Soporte Media y Larga":{"x": 61, "y": 59, "giro": 67},
            "Sin definir":          {"x": 77, "y": 77, "giro": 81},
        },
    },
    "Redmi Note 13": {
        "pantalla": "6.67 pulgadas | FHD+ | 120Hz AMOLED",
        "nota": "AMOLED con mejor respuesta táctil, ligeramente más sensi que Note 12",
        "sensi": {
            "IGL":                  {"x": 79, "y": 79, "giro": 88},
            "Fragger":              {"x": 88, "y": 88, "giro": 97},
            "Entry Fragger":        {"x": 93, "y": 93, "giro": 100},
            "Ancla":                {"x": 76, "y": 76, "giro": 83},
            "Soporte Media":        {"x": 68, "y": 66, "giro": 75},
            "Soporte Larga":        {"x": 58, "y": 56, "giro": 63},
            "Soporte Media y Larga":{"x": 63, "y": 61, "giro": 69},
            "Sin definir":          {"x": 79, "y": 79, "giro": 83},
        },
    },
    "Xiaomi 12": {
        "pantalla": "6.28 pulgadas | FHD+ | 120Hz AMOLED",
        "nota": "Pantalla compacta premium — ideal para sensi más alta y aim preciso",
        "sensi": {
            "IGL":                  {"x": 83, "y": 83, "giro": 91},
            "Fragger":              {"x": 91, "y": 91, "giro": 100},
            "Entry Fragger":        {"x": 96, "y": 96, "giro": 100},
            "Ancla":                {"x": 79, "y": 79, "giro": 86},
            "Soporte Media":        {"x": 71, "y": 69, "giro": 78},
            "Soporte Larga":        {"x": 61, "y": 59, "giro": 66},
            "Soporte Media y Larga":{"x": 66, "y": 64, "giro": 72},
            "Sin definir":          {"x": 83, "y": 83, "giro": 87},
        },
    },
    "POCO X5 Pro": {
        "pantalla": "6.67 pulgadas | FHD+ | 120Hz AMOLED",
        "nota": "Gaming phone económico, muy popular en esports móvil LatAm",
        "sensi": {
            "IGL":                  {"x": 80, "y": 80, "giro": 89},
            "Fragger":              {"x": 89, "y": 89, "giro": 98},
            "Entry Fragger":        {"x": 94, "y": 94, "giro": 100},
            "Ancla":                {"x": 77, "y": 77, "giro": 84},
            "Soporte Media":        {"x": 69, "y": 67, "giro": 76},
            "Soporte Larga":        {"x": 59, "y": 57, "giro": 64},
            "Soporte Media y Larga":{"x": 64, "y": 62, "giro": 70},
            "Sin definir":          {"x": 80, "y": 80, "giro": 84},
        },
    },

    # ─────────────── MOTOROLA ──────────────────────────────────────────────
    "Motorola Moto G84": {
        "pantalla": "6.55 pulgadas | FHD+ | 120Hz",
        "nota": "Buen pantalla/precio, respuesta táctil sólida",
        "sensi": {
            "IGL":                  {"x": 81, "y": 81, "giro": 89},
            "Fragger":              {"x": 90, "y": 90, "giro": 99},
            "Entry Fragger":        {"x": 95, "y": 95, "giro": 100},
            "Ancla":                {"x": 78, "y": 78, "giro": 85},
            "Soporte Media":        {"x": 70, "y": 68, "giro": 77},
            "Soporte Larga":        {"x": 60, "y": 58, "giro": 65},
            "Soporte Media y Larga":{"x": 65, "y": 63, "giro": 71},
            "Sin definir":          {"x": 81, "y": 81, "giro": 85},
        },
    },
    "Motorola Moto G52": {
        "pantalla": "6.6 pulgadas | FHD+ | 90Hz OLED",
        "nota": "90Hz — subir sensi para compensar, OLED da buena respuesta",
        "sensi": {
            "IGL":                  {"x": 84, "y": 84, "giro": 92},
            "Fragger":              {"x": 93, "y": 93, "giro": 100},
            "Entry Fragger":        {"x": 97, "y": 97, "giro": 100},
            "Ancla":                {"x": 81, "y": 81, "giro": 88},
            "Soporte Media":        {"x": 73, "y": 71, "giro": 80},
            "Soporte Larga":        {"x": 63, "y": 61, "giro": 69},
            "Soporte Media y Larga":{"x": 68, "y": 66, "giro": 74},
            "Sin definir":          {"x": 84, "y": 84, "giro": 88},
        },
    },

    # ─────────────── REALME / OPPO ─────────────────────────────────────────
    "Realme C55": {
        "pantalla": "6.72 pulgadas | FHD+ | 90Hz",
        "nota": "Pantalla grande 90Hz, buen gama media, sensi moderada",
        "sensi": {
            "IGL":                  {"x": 82, "y": 82, "giro": 90},
            "Fragger":              {"x": 91, "y": 91, "giro": 100},
            "Entry Fragger":        {"x": 96, "y": 96, "giro": 100},
            "Ancla":                {"x": 79, "y": 79, "giro": 86},
            "Soporte Media":        {"x": 71, "y": 69, "giro": 78},
            "Soporte Larga":        {"x": 61, "y": 59, "giro": 66},
            "Soporte Media y Larga":{"x": 66, "y": 64, "giro": 72},
            "Sin definir":          {"x": 82, "y": 82, "giro": 86},
        },
    },

    # ─────────────── IPHONE ────────────────────────────────────────────────
    "iPhone 11": {
        "pantalla": "6.1 pulgadas | LCD | 60Hz",
        "nota": "60Hz — subir sensibilidad considerablemente, táctil muy preciso",
        "sensi": {
            "IGL":                  {"x": 92, "y": 92, "giro": 100},
            "Fragger":              {"x": 100, "y": 100, "giro": 100},
            "Entry Fragger":        {"x": 100, "y": 100, "giro": 100},
            "Ancla":                {"x": 88, "y": 88, "giro": 95},
            "Soporte Media":        {"x": 80, "y": 78, "giro": 87},
            "Soporte Larga":        {"x": 70, "y": 68, "giro": 76},
            "Soporte Media y Larga":{"x": 75, "y": 73, "giro": 82},
            "Sin definir":          {"x": 92, "y": 92, "giro": 95},
        },
    },
    "iPhone 12": {
        "pantalla": "6.1 pulgadas | OLED | 60Hz",
        "nota": "60Hz OLED — táctil preciso, misma lógica que iPhone 11",
        "sensi": {
            "IGL":                  {"x": 91, "y": 91, "giro": 99},
            "Fragger":              {"x": 99, "y": 99, "giro": 100},
            "Entry Fragger":        {"x": 100, "y": 100, "giro": 100},
            "Ancla":                {"x": 87, "y": 87, "giro": 94},
            "Soporte Media":        {"x": 79, "y": 77, "giro": 86},
            "Soporte Larga":        {"x": 69, "y": 67, "giro": 75},
            "Soporte Media y Larga":{"x": 74, "y": 72, "giro": 81},
            "Sin definir":          {"x": 91, "y": 91, "giro": 94},
        },
    },
    "iPhone 13": {
        "pantalla": "6.1 pulgadas | OLED | 60Hz",
        "nota": "Similar a iPhone 12 pero con mejor procesador",
        "sensi": {
            "IGL":                  {"x": 90, "y": 90, "giro": 98},
            "Fragger":              {"x": 98, "y": 98, "giro": 100},
            "Entry Fragger":        {"x": 100, "y": 100, "giro": 100},
            "Ancla":                {"x": 86, "y": 86, "giro": 93},
            "Soporte Media":        {"x": 78, "y": 76, "giro": 85},
            "Soporte Larga":        {"x": 68, "y": 66, "giro": 74},
            "Soporte Media y Larga":{"x": 73, "y": 71, "giro": 80},
            "Sin definir":          {"x": 90, "y": 90, "giro": 93},
        },
    },
}

LISTA_DISPOSITIVOS = list(SENSI_POR_DISPOSITIVO.keys())

CONSEJOS_SENSI = """
📐 *CÓMO AJUSTAR TU SENSIBILIDAD*

1️⃣ *Empieza con la base recomendada* y juega 3-5 partidas sin tocarla.

2️⃣ Si el aim se siente *demasiado rápido* (te pasas del objetivo):
   → Baja X e Y en 5 puntos

3️⃣ Si el aim se siente *demasiado lento* (llegas tarde al objetivo):
   → Sube X e Y en 5 puntos

4️⃣ Ajusta *primero el eje Y* (vertical) ya que la mayoría tiene más dificultad vertical.

5️⃣ Una vez estable por 1 semana, empieza micro-ajustes de 2-3 puntos.

⚠️ *NO cambies la sensi después de cada partida* — dale tiempo a tu músculo-memoria.
"""
