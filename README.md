# Juego: Tragamonedas (Slot Machine)

Programa interactivo desarrollado en Python que simula una máquina tragamonedas clásica de casino utilizando emojis en la terminal.

## Descripción

El juego interactúa con el usuario permitiéndole girar los rodillos de la máquina de forma continua. El sistema selecciona tres símbolos al azar y verifica si coinciden para otorgar el premio mayor, ofreciendo al jugador la opción de seguir jugando o salir en cualquier momento.

## Características

* Simulación de giros aleatorios con emojis representativos.
* Sistema de detección de premio mayor (Jackpot) al alinear tres "7️⃣".
* Ciclo de juego continuo controlado por el usuario.
* Conversión automática de respuestas a minúsculas para evitar errores de entrada.

## Tecnologías

* Python 3
* Módulo `random` (Librería nativa)

## Cómo ejecutar

1. Clona este repositorio o descarga el archivo.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta:
   python juego_tragamonedas_random.py

## Ejemplo de salida

==================================================
🎰 Máquina Tragamonedas 🎰
==================================================

Presiona enter para Jugar:

🍉 | 🍇 | 🍒 
¡Gracias por jugar! 

¿Quieres seguir jugando? y(si)/n(no): y

Presiona enter para Jugar:

7️⃣ | 7️⃣ | 7️⃣ 
¡Jackpot! 💰 

...

## Lo que practiqué

En este proyecto utilicé:
* Importación y uso de módulos nativos (`random.choices`)
* Definición y llamado de funciones (`def`)
* Bucles `while` para ciclos continuos
* Validación y transformación de entradas de texto (`.lower()`)
* Manejo de listas e índices
* Condicionales lógicas múltiples (`==`)

## Próximas mejoras

* **Sistema de apuestas y saldo:** Agregar un sistema de monedas o créditos iniciales para que el jugador gane o pierda saldo en cada tirada, terminando el juego automáticamente si se queda sin fondos.
* **Personalización de apuestas:** Permitir al usuario elegir cuánto apostar en cada tiro (por ejemplo: apuesta baja, media o alta) y que el premio del Jackpot se multiplique según esa decisión.

## Estado del proyecto

Proyecto finalizado como práctica de Python.