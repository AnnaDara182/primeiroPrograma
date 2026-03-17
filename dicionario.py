#Criando dicionários

aluno={"ID": 1, "nome":"Anna", "curso": "ADS"}
pessoa={"nome":"Bruno", "idade": 20}

print("-----------------------------------------")
print("O nome da pessoa é:", pessoa["nome"])
print("-----------------------------------------")
print("O nome do aluno é:", aluno["nome"])

#Adicionando nova chave no dicionário

aluno["cidade"]= "Jundiai"
aluno["idade"]= 30
print("-----------------------------------------")
print("Aluno atualizado:", aluno)
print("-----------------------------------------")

#Removendo chave do dicionário

pessoa.pop("idade")
print("Chave removida('idade'):", pessoa)

#Tamanho

print("-----------------------------------------")
print("Tamanho do dicionário aluno:", len(aluno))
print("-----------------------------------------")
print("Tamanho do dicionário pessoa:", len(pessoa))
print("-----------------------------------------")

#Listar chaves, valores e itens

print("Chaves do dicionário aluno:", aluno.keys())
print("-----------------------------------------")
print("Valores do dicionário aluno:", aluno.values())
print("-----------------------------------------")
print("Itens do dicionário aluno:", aluno.items())
print("-----------------------------------------")

#Verificar se uma chave existe

print("Tem 'curso' no dicionário aluno?", "curso" in aluno)
print("-----------------------------------------")
print("Tem 'sobrenome' no dicionário aluno?", "sobrenome" in aluno)
print("-----------------------------------------")

#atualizar várias chaves de uma vez

aluno.update({"curso": "Engenharia", "idade": 25})
print("Aluno atualizado:", aluno)

