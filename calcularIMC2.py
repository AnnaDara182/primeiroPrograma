#Entrada de dados
peso= float(input('Qual o seu peso? '))
altura= float(input('Qual a sua altura? '))

#Calculo do IMC
imc= peso / (altura * altura)

#Condições para classificação do IMC
if imc < 18.5:
    print(f'Seu IMC é: {imc:.2f}! Você está com baixo peso.')

elif imc < 25:
    print(f'Seu IMC é: {imc:.2f}! Você está com peso normal.')

elif imc < 30:
    print(f'Seu IMC é: {imc:.2f}! Você está com sobrepeso.')

else:
    print(f'Seu IMC é: {imc:.2f}! Você está com obesidade.')