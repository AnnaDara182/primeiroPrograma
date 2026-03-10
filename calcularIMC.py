nome= input('Qual o seu nome? ')
peso= float(input('Qual o seu peso? '))
altura= float(input('Qual a sua altura? '))

imc= peso/(altura*altura)
print(f'{nome}, o seu IMC é {imc:.2f}')

baixo_peso= imc < 18.5
peso_normal= (imc >= 18.5) and (imc < 25)
sobrepeso= (imc >= 25) and (imc < 30)
obesidade= imc >= 30

print('Baixo peso: ', baixo_peso)
print('Peso normal: ', peso_normal)
print('Sobrepeso: ', sobrepeso)
print('Obesidade: ', obesidade)