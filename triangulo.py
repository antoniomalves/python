"""
  Faça um Programa que peça os três lados de um triângulo. 
  O programa deverá informar se os valores podem ser um triângulo. 
  Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
"""

a = int(input('Informe o 1º lado do triângulo... '))
b = int(input('Informe o 2º lado do triângulo... '))
c = int(input('Informe o 3º lado do triângulo... '))

if (a < (b + c)) and (b < (a + c)) and (c <(b + c)):
    if (a == b) and (b == c):
        print("Triângulo equilátero.")        
    elif (a != b) and (b != c) and (a != c):
        print("Triângulo escaleno.")
    else:
        print("Triângulo isosceles.")
else:
    print("Os lados não correspondem a um triângulo!")
