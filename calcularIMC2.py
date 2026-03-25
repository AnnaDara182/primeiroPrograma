#Entrada de dados
peso= float(input('Qual o seu peso? '))
altura= float(input('Qual a sua altura? '))

#Calculo do IMC
imc= peso / (altura * altura)

#Condições para classificação do IMC
if imc < 18.5:
    print('Baixo peso')

elif imc < 25:
    print('Peso normal')

elif imc < 30:
    print('Sobrepeso')

else:
    print('Obesidade')