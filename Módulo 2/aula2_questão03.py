#3 - Dadas duas variáveis v1 = 10 e v2 = 20, utilize uma terceira variável para trocar os valores entre as duas variáveis. 
# Ou seja, ao final v1 terá o valor de v2, e v2 o valor de v1.
# Você deve usar uma variável auxiliar de troca, não podendo atribuir os novos valores diretamente. 

v1 = 10

v2 = 20


#Complete o código aqui.

#Variável Auxiliar

Va = v1
v1 = v2
v2 = Va 


print(v1) #Imprime 20

print(v2) #Imprime 10