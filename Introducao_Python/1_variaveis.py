# Existem 3 tipos de Variâveis: Texto, Números Inteiros e Decimais
nome = "joao"  # String - Texto
idade = 99  # Int - Números Inteiros
altura = 1.83  # Float - Decimais

# Para ser reproduzido, é necessario que todas as variâveis sejam do mesmo tipo

print("O " + nome + " têm " + str(idade) + " anos e mede " + str(altura) + "m")

# Em python3.7 ou superior, foram introduzidas as f-Strings
# tornam possivel usar vários tipos de variâveis sem ser necessário converter.

print(f"O {nome} têm {idade} anos e mede {altura}m")
