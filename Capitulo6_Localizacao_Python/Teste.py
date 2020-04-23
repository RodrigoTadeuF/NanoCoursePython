import platform
import getpass
from datetime import datetime


print("Nome maquina:...............", platform.node())
print("Arquitetura:................", platform.architecture())
print("Sistema Operacional:........", platform.system())
print("Versão do SO:...............", platform.release())
print("Processador:................", platform.processor())
print("Versão do Python:...........", platform.python_version())


print(datetime.now())

usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha:...")

if usuario == 'usertricaster' and senha == 'Hello':
    print('Bem vindo Adele')
else:
    print('Você não tem acesso')