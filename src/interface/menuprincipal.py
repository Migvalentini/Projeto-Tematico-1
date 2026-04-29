from src.interface import menu
import questionary
from src.classes.usuario import Usuario
from questionary import Choice
from src.armazenamento.gerenciador import *

# python -m src.interface.menuprincipal

def chama_menu_principal():
    choice = questionary.select(
    "Bem vindo! O que deseja fazer?",
    choices=[
        Choice("Fazer Login", value=1),
        Choice("Criar usuário", value=2),
        Choice("Sair", value=3),
        Choice("Print", value=4),
    ]).ask()

    return choice

def menu_cadastro():
    usuario_info = questionary.text("Informe seu usuário: ").ask()
    senha_info = questionary.password("Informe sua senha: ").ask()

    usuario_novo = Usuario(nome=usuario_info, senha=senha_info)
    return usuario_novo

user = Usuario(nome="Diego", senha="123")
usuarios.append(user)

opcao = 0
while (opcao != 3):
    opcao = chama_menu_principal()
    validado = True
    if opcao == 1: #Login
        usuario_info = questionary.text("Informe seu usuário: ").ask()
        resultado = next((usuario for usuario in usuarios if usuario_info == usuario.nome), None)
        if not resultado:
            print("Usuário informado não localizado no sistema!")
            validado = False
        if validado:
            senha_info = questionary.password("Informe sua senha: ").ask()
            if senha_info != resultado.senha:
                print("Senha incorreta")
                validado = False
        if not validado:
            print('Não foi possivel fazer login!')
        else:
            usuario_logado = resultado
            menu.menu_logado(usuario_logado)
    elif opcao == 2: #Criar usuário
        print('Vamos realizar seu cadastro! Favor informe os seguintes dados:')
        cadastro = menu_cadastro()
        usuarios.append(cadastro)
    elif opcao == 4: #Print
        print(usuarios)
print("Encerrando...")