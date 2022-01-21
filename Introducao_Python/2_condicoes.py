# Condicoes são usadas para condicionar o fluxo do código

dinheiro_atual = 20.00
banana = 1.20
computador = 500

# Se dinheiro inicial for maior ou igual ao valor da banana
if(dinheiro_atual >= banana):
    dinheiro_atual = dinheiro_atual - banana
    print(f"Banana comprada!\nSaldo Atual: {dinheiro_atual}€")
else:  # Caso nao seja possivel comprar banana
    print(f"Não é possivel comprar banana")

# Se dinheiro inicial for maior ou igual ao valor do computador
if(dinheiro_atual >= computador):
    dinheiro_atual = dinheiro_atual - computador
    print(f"Computador comprado!\nSaldo Atual: {dinheiro_atual}€")
else:  # Caso nao seja possivel comprar computador
    print(f"Não é possivel comprar computador")
