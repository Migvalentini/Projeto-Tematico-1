import questionary
from questionary import Choice
from src.classes.categorias import Categoria
from src.armazenamento import gerenciador
from src.utils.utils import perguntar

def chama_menu():
    choice = perguntar(questionary.select(
    "Bem vindo ao Menu Categorias! O que deseja fazer?",
    choices=[
        Choice("Listar categorias", value=1),
        Choice("Cadastrar categoria", value=2),
        Choice("Editar categoria", value=3),
        Choice("Excluir categoria", value=4),
        Choice("Voltar", value=5),
    ]))

    return choice

def menu_logado():
    usuarioLogado = gerenciador.getUsuarioLogado()

    opcao = 0
    while (opcao != 5):
        try:
            opcao = chama_menu()
            if opcao == 1: # Listar categorias
                print("Categorias:")
                for categoria in gerenciador.getCategorias():
                    print(f" - {categoria.nome}: {categoria.descricao}")
            elif opcao == 2: # Cadastrar categorias
                cria_categoria(usuarioLogado)
            elif opcao == 3: # Editar categorias
                categoria_editavel = perguntar(questionary.select(
                    "Selecione a categoria para edição:",
                    choices=[Choice(categoria.nome + " - " + categoria.descricao, value=categoria) for categoria in gerenciador.getCategorias()]
                ))
                
                categorianome = perguntar(questionary.text("Digite o nome da categoria:"))

                categoriadesc = perguntar(questionary.text("Digite a descrição da categoria:"))

                categoria_editavel.nome = categorianome
                categoria_editavel.descricao = categoriadesc
                gerenciador.gravardados()
            elif opcao == 4: # Excluir categorias
                categorias_excluir = gerenciador.getCategorias()
                if not categorias_excluir:
                    print("Nenhuma categoria disponível para exclusão.")
                    continue
                categoria_apagavel = perguntar(questionary.select(
                    "Selecione a categoria para exclusão:",
                    choices=[Choice(categoria.nome + " - " + categoria.descricao, value=categoria.id_categoria) for categoria in gerenciador.getCategorias()]
                ))

                indApaga = True

                for despesa in gerenciador.getDespesas():
                    if despesa.id_categoria == categoria_apagavel:
                        print("Não é possível excluir esta categoria, pois ela está associada a uma ou mais despesas.")
                        indApaga = False
                        break
                
                if indApaga:
                    for categoria in gerenciador.getCategorias():
                        if categoria.id_categoria == categoria_apagavel:
                            gerenciador.categorias.remove(categoria)
                            gerenciador.gravardados()
                            print("Categoria excluída com sucesso!")
                            break
        except LookupError:
            opcao = 0
            pass

    print("Voltando ao menu...")

def cria_categoria(usuarioLogado):
    categorianome = perguntar(questionary.text("Digite o nome da nova categoria"))
    categoriadesc = perguntar(questionary.text("Digite a descrição da nova categoria"))
    gerenciador.categorias.append(Categoria(nome=categorianome, descricao=categoriadesc, id_usuario=usuarioLogado.id_usuario))
    gerenciador.gravardados()