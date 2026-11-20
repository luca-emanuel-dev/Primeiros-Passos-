emali_gerente = {"Iguatemi": "eu@gmail.com","Parangaba":"ameliauribeiro0807","Benfica":"benfica@0344"}

#pegar um item
email = emali_gerente["Iguatemi"]
print(email)

# adicionar um item
emali_gerente["Leblon"] = "aluno"
print(emali_gerente)

# editar um item
emali_gerente["Iguatemi"] = "renato roseno"
print(emali_gerente)

# remover um item
item_removido = emali_gerente.pop("Iguatemi")
print(emali_gerente)
print(item_removido)

# Verificar se o item existe
print("renato roseno" in emali_gerente)

#transformar em lista apenas as chaves

lista_dicionario = list(emali_gerente.keys())
print(lista_dicionario

# Exercício

produtos_valores = {"ipode":2000,"notebook": 3000, "fone": 5000}

achar_produto = input("Digite o produto que você quer: ")
 
if achar_produto in  produtos_valores.keys():
    print(f"O produto existe e custa {produtos_valores[achar_produto]}")
else:
    print("O produto não existe")
 