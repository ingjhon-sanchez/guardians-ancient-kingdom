# Guardians of the Ancient Kingdom

## 1. Descripción

Es un juego de combate por turnos hecho en Python. Dos guardianes (Guerrero, Mago o Arquero) se atacan por turnos hasta que uno se queda sin vida, y el programa dice quién ganó o si hubo empate. Resuelve el problema de tener personajes parecidos que atacan de forma distinta.

## 2. Estructura

- `personajes.py`: tiene todas las clases del juego.
- `main.py`: crea los personajes, hace los combates y muestra las pruebas.
- `README.md`: este documento.

## 3. Clases

- **Personaje**: clase base abstracta. Guarda nombre, vida, ataque y defensa, y sabe recibir daño. Obliga a que cada hijo tenga su método `atacar()`.
- **Guerrero**: su ataque sube un 20 % antes de restar la defensa del enemigo.
- **Mago**: su ataque ignora la defensa del enemigo.
- **Arquero**: si su ataque es mayor que la defensa, hace el doble de daño.
- **Combate**: maneja los turnos y dice quién gana. Recibe dos personajes ya creados.

## 4. Relaciones

- **Herencia**: Guerrero, Mago y Arquero son personajes, por eso usan lo que ya tiene la clase base.
- **Asociación**: cuando un personaje ataca a otro, los dos interactúan mediante `atacar()` y `recibir_danio()`.
- **Agregación**: Combate tiene dos personajes, pero no los crea; se crean aparte en `main.py`.

## 5. Conceptos de POO

- **Abstracción**: `Personaje` establece que todos deben atacar, pero no define cómo lo hace cada uno.
- **Encapsulamiento**: los atributos como `_vida` se manejan como datos internos y se utilizan métodos como `get_vida()` y `set_vida()` para consultar y validar sus valores.
- **Herencia**: las clases hijas reutilizan el constructor y `recibir_danio()` de `Personaje`.
- **Polimorfismo**: en `Combate` se utiliza `atacar()` para todos los personajes, pero cada uno ataca a su manera.

## 6. Lógica del combate

El daño se calcula así:

- **Guerrero**: `ataque × 1.20 − defensa`. El resultado se redondea hacia abajo y nunca es menor que 0.
- **Mago**: el daño es igual a su ataque.
- **Arquero**: `(ataque − defensa) × 2` si el ataque es mayor que la defensa; si no, causa 0 de daño.

Primero ataca el primer personaje y luego el segundo. Esos dos ataques forman una ronda. Después de cada ataque se muestra la vida de los dos personajes.

El combate termina cuando:

1. Uno llega a 0 de vida y el otro gana.
2. Una ronda no causa daño y se produce un empate técnico.
3. Se completan 50 rondas sin ganador y se produce un empate.

## 7. Ejecución

1. Descargar el repositorio de GitHub mediante el botón verde **Code > Download ZIP** y descomprimirlo.
2. Abrir una terminal dentro de la carpeta del proyecto.
3. Ejecutar el siguiente comando:

```bash
python main.py
```

## 8. Pruebas

Al ejecutar `main.py` se realizan las siguientes comprobaciones:

1. Se crean un Guerrero, un Mago y un Arquero.
2. Se comprueban las condiciones de vida mayor a 100 o negativa.
3. Se comprueba la condición de nombre vacío.
4. Se comprueban las condiciones de ataque igual a 0 y defensa negativa.
5. **Guerrero**: ataque 30 contra defensa 10, causa 26 de daño.
6. **Mago**: ataque 40 contra defensa 20, causa 40 de daño.
7. **Arquero**: ataque 35 contra defensa 15, causa 40 de daño.
8. La vida no baja de 0: con 20 de vida y 50 de daño queda en 0.
9. Se comprueba que un personaje derrotado no pueda atacar ni ser atacado.
10. Se realiza un combate completo entre Arthas (Guerrero) y Gandalf (Mago).
11. Se muestra el ganador del combate. Con las estadísticas indicadas, gana Arthas con 10 de vida restante.
12. Dos personajes que no se hacen daño terminan en empate técnico.