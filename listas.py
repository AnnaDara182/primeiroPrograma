frutas= ['amora', 'banana', 'laranja', 'uva', 'pera', 'goiaba', 'abacaxi', 'melancia', 'manga', 'morango']
numeros= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Primeira fruta da lista: ', frutas[0])
print('Última fruta da lista: ', frutas[-1])

frutas[0] = 'amora-silvestre'
print('Lista atualizada: ', frutas)

frutas.append('kiwi')
frutas.insert(2, 'cereja')
print('Lista após adicionar novas frutas: ', frutas)

frutas.remove('banana')
print('Lista após remover a banana: ', frutas)
frutas.pop()
print('Lista após remover a última fruta: ', frutas)

print('Número de frutas na lista: ', len(frutas))
print('Fatiando a lista de frutas: ', frutas[2:5])
print('Tem "kiwi" na lista? ', 'kiwi' in frutas)

print('Lista original "numeros":', numeros)
print('Soma dos numeros:', sum(numeros))
print('Maior número:', max(numeros))
print('Menor número:', min(numeros))

numeros.reverse()
print('Resersa:', numeros)

numeros.sort()
print('Ordenada crescente:', numeros)

numeros.sort(reverse=True)
print('Ordenada decrescente:', numeros)

for fruta in frutas:
    print('Fruta:', fruta)

quadrados= [n * n for n in [1, 2, 3, 4, 5]]
print('Quadrados:', quadrados)
