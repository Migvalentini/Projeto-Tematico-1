import questionary
from questionary import Choice

usuario_logado = {'user': '', 'senha': ''}

usuarios = []


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
    usuario_info = questionary.text("Informe seu usuário").ask()
    senha_info = questionary.password("Informe sua senha").ask()

    usuario_novo = {'nome':usuario_info, 'senha': senha_info, 'id': len(usuarios) + 1}
    return usuario_novo

user = {'nome':'diego','senha':'123', 'id':1}
usuarios.append(user)

opcao = 0
while (opcao !=3):
    opcao = chama_menu_principal()
    validado = True
    if opcao == 1:
        usuario_info = questionary.text("Informe seu usuário").ask()
        if usuario_info != user['nome']:
            print("Usuário informado não localizado no sistema")
            validado = False
        if validado:
                senha_info = questionary.password("Informe sua senha").ask()
                if senha_info != user['senha']:
                    print("Senha incorreta")
                    validado = False
        if not validado:
            print('Não foi possivel fazer login!')
        else:
            usuario_logado['user'] = usuario_info
            usuario_logado['senha'] = senha_info
            print('Seja bem-vindo ' + usuario_logado['user'])
    elif opcao == 2:
        print('Vamos realizar seu cadastro! Favor informe os seguintes dados:')
        cadastro = menu_cadastro()
        usuarios.append(cadastro)
    elif opcao == 4:
        print(usuarios)
print("Encerrando...")