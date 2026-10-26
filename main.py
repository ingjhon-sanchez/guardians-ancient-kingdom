from personajes import Guerrero, Mago, Arquero, Combate

print("--- 1. Creación de personajes ---")
guerrero = Guerrero("Arthas", 100, 30, 20)
mago = Mago("Gandalf", 80, 40, 10)
arquero = Arquero("Legolas", 90, 35, 15)

print(guerrero.mostrar_estado())
print(mago.mostrar_estado())
print(arquero.mostrar_estado())


print("\n--- 2. Vida inválida ---")
vida = 101

if vida < 0 or vida > 100:
    print("Correcto: vida 101 rechazada")
else:
    print("ERROR: debió rechazar la vida 101")

vida = -5

if vida < 0 or vida > 100:
    print("Correcto: vida -5 rechazada")
else:
    print("ERROR: debió rechazar la vida -5")


print("\n--- 3. Nombre vacío ---")
nombre = ""

if nombre.strip() == "":
    print("Correcto: nombre vacío rechazado")
else:
    print("ERROR: debió rechazar el nombre vacío")


print("\n--- 4. Ataque y defensa inválidos ---")
ataque = 0

if ataque <= 0:
    print("Correcto: ataque 0 rechazado")
else:
    print("ERROR: debió rechazar el ataque 0")

defensa = -1

if defensa < 0:
    print("Correcto: defensa -1 rechazada")
else:
    print("ERROR: debió rechazar la defensa -1")


print("\n--- 5. Habilidad del Guerrero ---")
atacante = Guerrero("Guerrero", 100, 30, 20)
objetivo = Mago("Objetivo", 80, 10, 10)
danio = atacante.atacar(objetivo)

print("Ataque 30 vs defensa 10 -> daño", danio, "(esperado 26)")


print("\n--- 6. Habilidad del Mago ---")
atacante = Mago("Mago", 80, 40, 10)
objetivo = Guerrero("Objetivo", 100, 10, 20)
danio = atacante.atacar(objetivo)

print("Ataque 40 vs defensa 20 -> daño", danio, "(esperado 40)")


print("\n--- 7. Habilidad del Arquero ---")
atacante = Arquero("Arquero", 90, 35, 15)
objetivo = Guerrero("Objetivo", 100, 10, 15)
danio = atacante.atacar(objetivo)

print("Ataque 35 vs defensa 15 -> daño", danio, "(esperado 40)")


print("\n--- 8. Vida nunca negativa ---")
debil = Guerrero("Debil", 20, 10, 5)
debil.recibir_danio(50)

print("Vida después de recibir 50 de daño:", debil.get_vida(), "(esperado 0)")


print("\n--- 9. Derrotado no puede atacar ---")
sano = Mago("Sano", 80, 40, 10)

if not debil.esta_vivo():
    print("Correcto: el derrotado no puede atacar")
else:
    print("ERROR: el derrotado no debería atacar")

if not debil.esta_vivo():
    print("Correcto: no se puede atacar a un derrotado")
else:
    print("ERROR: el objetivo no está derrotado")


print("\n--- 10 y 11. Combate completo y ganador ---")
arthas = Guerrero("Arthas", 100, 30, 20)
gandalf = Mago("Gandalf", 80, 40, 10)
combate = Combate(arthas, gandalf)

combate.iniciar()

print("\n--- 12. Empate técnico ---")
tanque1 = Guerrero("Tanque1", 100, 1, 50)
tanque2 = Arquero("Tanque2", 100, 10, 50)
combate2 = Combate(tanque1, tanque2)

combate2.iniciar()