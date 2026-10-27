import random

times = ["Flamengo", "Palmeiras", "Cruzeiro", "Athletico-PR", "Corinthians", "Santos", "São Paulo", "Grêmio", "Internacional", "Vasco da Gama", "Botafogo", "Fluminense", "Bahia", "Coritiba", "Atlético-MG", "Vitória", "Chapecoense", "RB Bragantino", "Mirassol", "Remo"]

random.shuffle(times) # Embaralha a lista

print("Classificação do Brasileirão 2026:")
print()

for posicao, time in enumerate(times, start=1): # Enumerate é uma função que permite percorrer uma lista e obter o índice (posição) e o valor (elemento) ao mesmo tempo. O parâmetro start=1 indica que a contagem deve começar em 1, em vez de 0.
    print(f"{posicao}° Lugar - {time}")