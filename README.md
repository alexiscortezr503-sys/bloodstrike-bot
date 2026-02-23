# ⚔️ BloodStrike Elite Bot

Bot de Telegram profesional para equipo competitivo de **Blood Strike Móvil**.  
Coach: **Alexis Cortez** | Deploy: **Railway** | Sistema: **Arch Linux**

---

## 🚀 DESPLIEGUE RÁPIDO EN RAILWAY

### Paso 1: Crear el bot en Telegram
1. Abre Telegram → busca `@BotFather`
2. Escribe `/newbot`
3. Dale un nombre, por ejemplo: `BloodStrike Elite`
4. Dale un username, por ejemplo: `bloodstrike_elite_bot`
5. **Copia el TOKEN que te da** (algo como `7123456789:AAHxyz...`)

### Paso 2: Subir al repositorio de GitHub
```bash
# En tu Arch Linux (terminal)
cd /ruta/donde/guardaste/el/proyecto

git init
git add .
git commit -m "Initial: BloodStrike Elite Bot"
git remote add origin https://github.com/alexiscortezr503-sys/bloodstrike-bot.git
git push -u origin main
```

### Paso 3: Configurar Railway
1. Ve a [railway.app](https://railway.app) → ya estás logueado ✅
2. Clic en **"New Project"**
3. Selecciona **"Deploy from GitHub repo"**
4. Escoge el repositorio `bloodstrike-bot`
5. Railway detectará el `requirements.txt` automáticamente

### Paso 4: Variables de entorno en Railway
En tu proyecto Railway → **Variables** → Agregar:

| Variable | Valor |
|----------|-------|
| `BOT_TOKEN` | El token de @BotFather |
| `COACH_ID` | Tu ID de Telegram (opcional — ver abajo cómo obtenerlo) |

#### ¿Cómo obtienes tu COACH_ID?
1. Busca `@userinfobot` en Telegram
2. Envíale cualquier mensaje
3. Te responde con tu ID numérico

### Paso 5: Deploy
- Railway hace el deploy automáticamente al hacer push
- Ve a **Deployments** para ver los logs
- ¡Listo! El bot corre 24/7 🎮

---

## 📁 ESTRUCTURA DEL PROYECTO

```
bloodstrike_bot/
├── bot.py                    # Archivo principal — arranque del bot
├── requirements.txt          # Dependencias Python
├── railway.toml              # Configuración Railway
├── Procfile                  # Comando de inicio
│
├── data/                     # Base de datos estática (JSON/Python)
│   ├── jugadores.py          # Roster + perfiles de jugadores
│   ├── meta.py               # META armas, habilidades, combinaciones
│   ├── sensibilidad.py       # Sensi por celular y rol
│   ├── examenes.py           # Banco de preguntas y sistema de puntos
│   ├── entrenamiento.py      # Planes individuales y rutina de equipo
│   ├── psicologia.py         # Respuestas de psicología
│   └── ranking.json          # Generado automáticamente
│
└── modules/                  # Módulos funcionales del bot
    ├── menu.py               # Menú principal
    ├── psicologia.py         # Módulo ¿Cómo te sientes? + Psico deportiva
    ├── examenes.py           # Sistema de exámenes y ranking
    ├── jugadores.py          # Perfiles de jugadores
    ├── sensi.py              # Sensibilidades por celular
    ├── meta.py               # META armas y tácticas
    ├── entrenamiento.py      # Planes de entrenamiento
    ├── ranking.py            # Ranking global
    └── coach.py              # Panel del coach
```

---

## ✅ FUNCIONES DEL BOT

| Función | Descripción |
|---------|-------------|
| 😊 ¿Cómo te sientes? | Psicología general — el jugador se desahoga y recibe apoyo |
| 🧠 Psicología Deportiva | Concentración, presión, anti-tilt, comunicación, objetivos |
| 🏋️ Plan de Entrenamiento | Plan individual por jugador con fases y ejercicios |
| 📚 Exámenes y Ranking | Preguntas por rol y mapa, sistema de puntos y niveles |
| 🔫 META Armas | Armas meta con tier, ventajas, contras y accesorios |
| 📐 Sensibilidad | Sensi (X)(Y) por celular y rol |
| 👥 Jugadores | Perfiles completos del roster |
| 🏆 Ranking | Leaderboard del equipo |
| 🗺️ Táctica por Mapa | Aldea, Desierto y Puerto con estrategia |
| 🎯 Combinaciones | Rush, tanqueo, defensiva para BE y TCT |
| 📋 Coach Panel | Panel exclusivo con estadísticas y gestión |

---

## 🎮 ROSTER CARGADO

### Principal (4/4)
| Jugador | Edad | Rol | Mejora Principal |
|---------|------|-----|-----------------|
| Anderson | 15 | IGL | SMG corta distancia |
| Jose | 14 | Fragger | SMG corta distancia |
| Xavier | 16 | Ancla | Movimiento + aim multi-rango |
| Alejandro | 18 | Soporte M+L | Centering y tracking |

### Secundario (3/4 — buscando jugador)
| Jugador | Edad | Rol | Mejora Principal |
|---------|------|-----|-----------------|
| Antonio | 18 | Fragger | Entry agresivo |
| Anderson 2 | 16 | Sin definir | Todo rango |
| Maximiliano | 14 | Soporte M+L | Todo desde base |

---

## 🔧 ACTUALIZAR META

Cuando haya un nuevo parche de Blood Strike:

1. Edita `data/meta.py`
2. Actualiza las armas, habilidades o combinaciones
3. Haz commit y push a GitHub
4. Railway hace el redeploy automáticamente ✅

```bash
git add data/meta.py
git commit -m "Update: nuevo meta parche X.X"
git push
```

---

## 📦 GUARDAR MÚLTIPLES BOTS EN UN REPOSITORIO

Sí puedes guardar todos tus bots en un repo:

```
alexiscortezr503-sys/
├── bloodstrike-bot/      ← Este bot
├── otro-bot/
└── otro-proyecto/
```

Para este bot en específico, crea el repo `bloodstrike-bot` dentro de tu cuenta GitHub.

---

## 🆘 SOLUCIÓN DE PROBLEMAS

**Bot no responde:**
- Verifica que `BOT_TOKEN` esté bien en Railway → Variables
- Revisa los logs en Railway → Deployments

**Error de módulo:**
- Asegúrate que `requirements.txt` tenga `python-telegram-bot==20.7`
- Railway lo instala automáticamente

**¿Quieres que el bot reconozca a cada jugador individualmente?**
- Pide a cada jugador que inicie el bot y haga un examen
- El sistema los reconoce por su Telegram ID automáticamente
