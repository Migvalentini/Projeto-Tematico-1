import questionary
from questionary import Choice
from src.classes.categorias import Categoria
from src.armazenamento import gerenciador

def chama_menu():
    choice = questionary.select(
    "Bem vindo ao Menu Categorias! O que deseja fazer?",
    choices=[
        Choice("Listar categorias", value=1),
        Choice("Cadastrar categoria", value=2),
        Choice("Editar categoria", value=3),
        Choice("Excluir categoria", value=4),
        Choice("Voltar", value=5),
    ]).ask()

    return choice

def menu_logado():
    usuarioLogado = gerenciador.getUsuarioLogado()

    opcao = 0
    while (opcao != 5):
        opcao = chama_menu()
        if opcao == 1: # Listar categorias
            print("Categorias:")
            for categoria in gerenciador.getCategorias():
                print(f" - {categoria.nome}: {categoria.descricao}")
        elif opcao == 2: # Cadastrar categorias
            categorianome = questionary.text("Digite o nome da nova categoria").ask()
            categoriadesc = questionary.text("Digite a descrição da nova categoria").ask()
            gerenciador.categorias.append(Categoria(nome=categorianome, descricao=categoriadesc, id_usuario=usuarioLogado.id_usuario))
            gerenciador.gravardados()
        elif opcao == 3: # Editar categorias
            categoria_editavel = questionary.select(
                "Selecione a categoria para edição:",
                choices=[Choice(categoria.nome + " - " + categoria.descricao, value=categoria) for categoria in gerenciador.getCategorias()]
            ).ask()
            
            categorianome = questionary.text("Digite o nome da categoria:").ask()

            categoriadesc = questionary.text("Digite a descrição da categoria:").ask()

            categoria_editavel.nome = categorianome
            categoria_editavel.descricao = categoriadesc
            gerenciador.gravardados()
        elif opcao == 4: # Excluir categorias
            categorias_excluir = gerenciador.getCategorias()
            if not categorias_excluir:
                print("Nenhuma categoria disponível para exclusão.")
                continue
            categoria_apagavel = questionary.select(
                "Selecione a categoria para exclusão:",
                choices=[Choice(categoria.nome + " - " + categoria.descricao, value=categoria.id_categoria) for categoria in gerenciador.getCategorias()]
            ).ask()

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

    print("Voltando ao menu...")