"""
    Ciclos permitem que uma secção do seu codigo seja repetido
    em função de uma condição establecida
"""

# While Loop
print("While Loop")
count = 0  # variavel contadora
while count <= 10:  # Enquanto x for menor ou igual a 10
    calculo = 2 * count  # calculo = valor de count [0, 1, 2, 3... 10] x 2
    print(f"2 x {count} = {calculo}")  # mostra o valor de calc
    count = count + 1  # count aumenta por ciclo até satisfazer a condição de ciclo


# For Loop
print("\nFor Loop")
for x in range(11):  # Enquanto X estiver dentro da range (0 - 10)
    calculo = 7 * x
    print(f"2 x {x} = {calculo}")
