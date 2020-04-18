"""
nome = "Humberto Delgado"
empresa = "FIAP"
qtde_funcionarios = 500
mediaMensalidade = 856.50

print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, "funcionarios")
print("A média da mensalidade é de: " + str(mediaMensalidade))
"""

nome = input("Digite um funcionário: ")
empresa = input("Digite a instituição: ")
qtde_funcionarios = int(input("Digite a quantidade de funcionários: "))
mediaMensalidade = float(input("Digite a média da mensalidade: "))

print(nome + " trabalha na empresa " + empresa)
print("Possui: ", qtde_funcionarios, "funcionarios")
print("A média da mensalidade é de: " + str(mediaMensalidade))

print("=============================Verifique os tipos de dados abaixo: =============================")
print("O tipo do dado da variável 'nome' é: ", type(nome))
print("O tipo do dado da variável 'empresa' é: ", type(empresa))
print("O tipo do dado da variável 'qtde_funcionarios' é: ", type(qtde_funcionarios))
print("O tipo do dado da variável 'mediaMensalidade' é: ", type(mediaMensalidade))
