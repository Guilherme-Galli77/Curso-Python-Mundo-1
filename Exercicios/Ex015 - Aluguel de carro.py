# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
# e R$0,15 por Km rodado.

dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos Km rodados? "))

custo_dia = 60*dias
custo_km = 0.15*km
custo_total = custo_km + custo_dia

print("O total a pagar é de R$ {:.2f}".format(custo_total))