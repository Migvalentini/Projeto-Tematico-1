import questionary
from questionary import Choice
from src.interface import menuDespesas
from src.interface import menuRendas
from src.interface import menuCategorias
from src.interface import menuCalculos
from src.armazenamento import gerenciador

def validar_valor(texto):
    try:
        valor = float(texto.replace(",", "."))
        if valor < 0:
            return "Digite um valor positivo"
        return True
    except:
        return "Digite um número válido (ex: 10.50 ou 10,50)"

def chama_menu():
    choice = questionary.select(
    "Bem vindo ao Menu Logado! O que deseja fazer?",
    choices=[
        Choice("Menu Rendas", value=1),
        Choice("Menu Despesas", value=2),
        Choice("Menu Categorias", value=3),
        Choice("Menu Cálculos", value=4),
        Choice("Deslogar", value=5),
    ]).ask()

    return choice

def menu_logado():
    usuarioLogado = gerenciador.getUsuarioLogado()

    print("===============================================================================================")
    print("Seja Muito Bem-Vindo " + usuarioLogado.nome + "!")
    print("Aqui é o menu para usuários logados, onde você pode acessar as funcionalidades do sistema!")
    print("===============================================================================================")

    opcao = 0
    while (opcao != 5):
        opcao = chama_menu()
        if opcao == 1: # Abre menu de rendas
            menuRendas.menu_rendas()
        elif opcao == 2: #Cadastrar Despesa
            menuDespesas.menu_logado()
        elif opcao == 3: # Abrir menu de categorias
            menuCategorias.menu_logado()
        elif opcao == 4: # Abrir menu de cálculos
            menuCalculos.menu_logado()
    gerenciador.usuario_logado = None
    print("Encerrando...")