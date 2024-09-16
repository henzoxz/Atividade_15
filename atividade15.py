# Crie um programa que receba dois números e uma operação (soma, subtração, multiplicação ou divisão) e execute a operação desejada.
numero1 = int(input(" Digite o 1º Número "))
numero2 = int(input(" Digite o 2º Número "))
operacao = input(" Escolha a Operação desejada: Soma, Subtração, Multiplicação ou Divisão:  ")
if(operacao=="Soma"):
    resultado = (numero1 + numero2)
    print(f" Seu Resultado é: {resultado}")

if(operacao=="Subtração"):
    resultado = (numero1 - numero2)
    print(f" Seu Resultado é:  {resultado}")

if(operacao=="Multiplicação"):
    resultado = (numero1 * numero2)
    print(f" Seu Resultado é:  {resultado}")
      
if(operacao=="Divisão"):
    resultado = (numero1/numero2)
    print(f" Seu Resultado é:  {resultado}")

