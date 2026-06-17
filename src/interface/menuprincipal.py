from src.interface import menu
from src.armazenamento import gerenciador
from src.classes.usuarios import Usuario
import questionary
from questionary import Choice
from src.utils.utils import perguntar

# python -m src.interface.menuprincipal
    
def chama_menu_principal():
    choice = perguntar(questionary.select(
    "Bem vindo ao Menu Principal! O que deseja fazer?",
    choices=[
        Choice("Fazer Login", value=1),
        Choice("Criar usuário", value=2),
        Choice("Sair", value=3),
    ]))

    return choice

def menu_cadastro():
    usuario_info = perguntar(questionary.text("Informe seu usuário: "))
    senha_info = perguntar(questionary.password("Informe sua senha: "))

    usuario_novo = Usuario(nome=usuario_info, senha=senha_info)
    return usuario_novo

def main():
    gerenciador.carregardados()

    opcao = 0
    while (opcao != 3):
        try:
            opcao = chama_menu_principal()
            validado = True
            if opcao == 1: #Login
                usuario_info = perguntar(questionary.text("Informe seu usuário: "))
                resultado = next((usuario for usuario in gerenciador.usuarios if usuario_info == usuario.nome), None)
                if not resultado:
                    print("Usuário informado não localizado no sistema!")
                    validado = False
                if validado:
                    senha_info = perguntar(questionary.password("Informe sua senha: "))
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
        except LookupError:
            opcao = 0
            pass
    print("Encerrando...")
    
if __name__ == "__main__":
    main()