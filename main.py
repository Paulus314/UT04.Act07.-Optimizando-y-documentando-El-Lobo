from partes import gestorPartida

# --- Ejecución caótica ---
juego=gestorPartida()
juego.anadirJugador("Nacho", "lobo")
juego.anadirJugador("Elena", "vidente")
juego.anadirJugador("Carlos","aldeano")
juego.anadirJugador("Pepe", "aldeano")

print(juego.jugadores[0].AccionNocturna(juego.jugadores[2]))
print(juego.ComprobarVictoria())


# Intenta estructurar el main.py con el siguiente orden.
# --- FASE 1: LA NOCHE 🌙 ---
# Comprobamos estado antes de que amanezca
# --- FASE 2: EL DÍA ☀️ ---
# El motor de la partida ejecuta el linchamiento
# --- FINAL DE LA PARTIDA ---