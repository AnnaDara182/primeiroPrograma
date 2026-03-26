#Entrada de dados exercicio 1
idade= int(input('Qual a sua idade? '))

#Condições para a classificação da idade
if idade < 18:
    print('Você é menor de idade!')
elif idade < 60:
    print('Você é adulto(a)!')

else:
    print('Você é idoso(a)!')

print("-----------------------------------------") 

#Entrada de dados exercicio 2
temp= float(input('Quantos graus está fazendo? '))

#Condições para classificação da temperatura
if temp < 10:
    print('O dia está muito frio.')
elif temp < 24:
    print('O dia está agradável.')
elif temp < 30:
    print('O dia está quente.')
else:
    print('O dia está muito quente.')

print("-----------------------------------------")

#Entrada de dados exercicio 3
nota= float(input('Informe a nota: '))

#Condições para saber se passou de ano
if nota < 5:
    print('Você está reprovado(a)!')
elif nota < 6.9:
    print('Você está de recuperação!')
elif nota < 8.9:
    print('Você foi aprovado(a)!')
else:
    print('Você foi aprovado com excelência, meus parabéns!')

print("-----------------------------------------")