'''with open("primeiro_arquivo.txt", "a") as arquivo:
    arquivo.write("\n Carpe Diem")'''


'''arquivo = open("primeiro_arquivo.txt", "w")

arquivo.write("Meu primeiro arquivo! \o/")

arquivo.close()'''

with open("primeiro_arquivo.txt", "r") as arquivo:
    conteudo = arquivo.read()
    print(conteudo)


