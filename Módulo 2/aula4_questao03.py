## 3 - Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. 
# O preço dos produtos é calculado multiplicando a quantidade pelo preço unitário. 
# Escreva um programa em Python que solicite do usuário o nome, 
# o preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra.
# Note no exemplo a seguir que:

# Cada entrada de dados tem uma mensagem indicando o dado solicitado (mensagens em itálico, dado de entrada em negrito)

# A saída deve estar formatada exatamente como indicado (a string "Total: R$" e o preço com um separador de milhar e duas casas decimais).


#Entrada

#Digite o nome do produto 1:calça
nome1 = input("Digite o nome do produto1:  ")
#Digite o preço unitário do produto 1:199.90 
preco1 = float(input("Digite o preço unitário do produto 1:  "))
#Digite a quantidade do produto 1: 3
qtd1= int(input("Digite a quantidade do produto 1:  "))
#Digite o nome do produto 2:camisa
nome2 = input("Digite o nome do produto 2:  ")
#Digite o preço unitário do produto 2:49.95
preco2 = float(input("Digite o preço unitário do produto 2:  "))
#Digite a quantidade do produto 2:10
qtd2 = int(input("Digite a quantidade do produto 2:  "))
#Digite o nome do produto 3:cinto
nome3 = input("Digite o nome do produto 3:  ")
#Digite o preço unitário do produto 3:25
preco3 = float(input("Digite o preço unitário do produto 3:  "))
#Digite a quantidade do produto 3:3                             
qtd3 = int(input("Digite a quantidade do produto 3 :  "))



#Saída
#calcule o total da compra com base nos 3 produtos
total = (preco1 * qtd1) + (preco2 * qtd2) + (preco3 * qtd3)
#Imprime o valor com 2 casas decimais
print(f"Total: R${total:.2f}")
#Total: R$1,174.20




