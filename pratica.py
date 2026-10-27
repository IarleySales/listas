import random # Importa a biblioteca random, que permite gerar números aleatórios e escolher elementos aleatórios de uma lista.

nome = ["Ana", "Bruno", "Carlos", "José", "Caio"] # Cria a lista

print(nome[0])  # Puxa alguma posição da lista, começando por 0, No caso, puxando a posição 0, que é Ana.

cidades = ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte", "Salvador", "Fortaleza", "Recife"]

print(cidades[3])

times = ["Flamengo", "Botafogo", "Vasco", "Fluminense"]
print(times[0])

nome.append("Marcos") # Adiciona um elemento no final da lista
nome.append("Lucas")

nome.remove("Ana") # Remove um elemento da lista

print(nome[0])

print(random.choice(nome)) # Puxa um elemento aleatório da lista