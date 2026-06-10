from src.interface import menu
from src.armazenamento import gerenciador
from src.classes.usuarios import Usuario
import questionary
from questionary import Choice

# python -m src.interface.menuprincipal
    
def chama_menu_principal():
    choice = questionary.select(
    "Bem vindo ao Menu Principal! O que deseja fazer?",
    choices=[
        Choice("Fazer Login", value=1),
        Choice("Criar usuário", value=2),
        Choice("Sair", value=3),
    ]).ask()

    return choice

def menu_cadastro():
    usuario_info = questionary.text("Informe seu usuário: ").ask()
    senha_info = questionary.password("Informe sua senha: ").ask()

    usuario_novo = Usuario(nome=usuario_info, senha=senha_info)
    return usuario_novo

def main():
    gerenciador.carregardados()

    opcao = 0
    while (opcao != 3):
        opcao = chama_menu_principal()
        validado = True
        if opcao == 1: #Login
            usuario_info = questionary.text("Informe seu usuário: ").ask()
            resultado = next((usuario for usuario in gerenciador.usuarios if usuario_info == usuario.nome), None)
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
                gerenciador.usuario_logado = resultado
                menu.menu_logado()
        elif opcao == 2: #Criar usuário
            print('Vamos realizar seu cadastro! Favor informe os seguintes dados:')
            cadastro = menu_cadastro()
            gerenciador.usuarios.append(cadastro)
            gerenciador.criarCategorias(cadastro);
            gerenciador.gravardados()
            print('Usuário criado com sucesso!')
    print("Encerrando...")
    
if __name__ == "__main__":
    main()