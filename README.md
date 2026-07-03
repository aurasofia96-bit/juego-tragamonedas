# 🎰 Juego: Tragamonedas (Slot Machine)

## 📌 ¿De qué trata esto?
Este es un pequeño juego interactivo para la terminal de comandos que simula una máquina tragamonedas clásica de casino. El programa elige tres frutas o símbolos al azar y, si logras sacar el triple **7️⃣**, ¡te llevas el premio mayor!

Es un proyecto divertido que creé para practicar el uso de funciones y la generación de datos aleatorios en Python.

---

## 🎮 ¿Cómo se juega?
1. Al arrancar el programa, solo debes presionar **Enter** para hacer girar la máquina.
2. El sistema te mostrará los 3 símbolos resultantes en pantalla.
3. Si los tres símbolos son el número 7, aparecerá el mensaje de **¡Jackpot! 💰**.
4. Al final de cada ronda, el juego te preguntará si quieres seguir jugando o si prefieres salir.

---

## 🛠️ Lo que aprendí y apliqué aquí
* **🎲 Azar en Python:** Utilicé el módulo `random` (específicamente `random.choices`) para que la máquina elija los emojis de forma completamente aleatoria cada vez.
* **⚙️ Funciones reutilizables:** Creé una función llamada `play()` para ordenar el código y hacer que toda la lógica del juego se ejecute limpiamente con un solo llamado.
* **🔄 Bucles infinitos controlados:** Usé un ciclo `while` para que puedas jugar todas las veces que quieras hasta que decidas escribir `n` para salir.

---

## 🚀 Cómo probarlo
Para jugar en tu computador, asegúrate de tener Python instalado, descarga el archivo del juego y ejecútalo en tu terminal:

```bash
python juego_tragamonedas_random.py