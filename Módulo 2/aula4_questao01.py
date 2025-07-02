##1 - Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), 
# bem como o preço do metro quadrado da região em ponto flutuante. 
# Calcule o valor do terreno e imprima o resultado como mostra o exemplo a seguir:

# - O terreno possui 250m2 e custa R$512,490.50

 
# - Comente na linha acima de cada instrução uma breve descrição da instrução.

#Fórmulas:

# area_m2     = comprimento * largura
# preco_total = preco_m2    * area_m2

# Solicite o comprimento do terreno

comprimento   = int(input("Digite o comprimento do terreno em metros:  ")) 

# Solicite a largura do terreno

largura       = int(input("Digite a largura do terreno em metros:  "))

# Solicite o valor do metro quadrado

preco_m2      = float(input("Digite o preço do metro quadrado:  "))

# Calcule a área do terreno em m2

area_m2       = comprimento * largura

# Calcule o valor total do terreno

preco_total    = preco_m2   * area_m2

# Imprime o resultado formatado com duas casas decimais

print(f"O terreno possui: {area_m2}m² e custa: R${preco_total:,.2f}")
