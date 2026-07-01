#Juego: Traga monedas
# importar bibliotecas
import random
# definir valiables y listas
symbols = ['🍒', ' 🍇', '🍉', '7️⃣']
jugar = 'y'
# definir funciones 
def play():
  results = random.choices(symbols, k=3)
  print(f'{results[0]} | {results[1]} | {results[1]} \n' )
  if results[0] == results[1] == results[1]== '7️⃣':
    print('¡Jackpot! 💰 \n')
  else:
    print('¡Gracias por jugar! \n')
while jugar == 'y':
  enter = input('Preciona enter para Jugar:\n')
  play()
  jugar = input('¿Quieres seguir jugando? y(si)/n(no): \n').lower()