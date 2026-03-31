#Atividade 1

idade = int(input("Digite a idade: "))

#Condicional para verificação de idade

if idade <= 12:
    print("É uma criança.")
elif idade <= 17:
    print("É um adolescente.")
elif idade <= 59:
    print("É um adulto.")
else:
    print ("É um idoso.")

print("-" * 20)

#Atividade 2

nota = int(input("Digite a nota: "))

#Condicional para verificar a nota do aluno

if nota < 5:
    print("Reprovado!")
elif nota < 7:
    print("Regular!")
elif nota < 9:
    print("Bom!")
else:
    print("Excelente!")

print("-" * 20)