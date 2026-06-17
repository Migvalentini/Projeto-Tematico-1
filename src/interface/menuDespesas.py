import questionary
from questionary import Choice
from src.interface.menuCategorias import cria_categoria
from src.classes.despesas import Despesas
from src.armazenamento import gerenciador
from src.utils.utils import perguntar

def validar_valor(texto):
    try:
        valor = float(texto.replace(",", "."))
        if valor < 0:
            return "Digite um valor positivo"
        return True
    except:
        return "Digite um número válido (ex: 10.50 ou 10,50)"

def chama_menu():
    choice = perguntar(questionary.select(
    "Bem vindo ao Menu Despesas! O que deseja fazer?",
    choices=[
        Choice("Listar despesas", value=1),
        Choice("Cadastrar despesa", value=2),
        Choice("Editar despesa", value=3),
        Choice("Excluir despesa", value=4),
        Choice("Voltar", value=5),
    ]))

    return choice

def menu_logado():
    usuarioLogado = gerenciador.getUsuarioLogado()

    opcao = 0
    while (opcao != 5):
        try:
            opcao = chama_menu()
            if opcao == 1: # Listar Despesas
                print("Despesas:")
                for despesa in gerenciador.getDespesas():
                    print(f" Data: {despesa.data_inclusao.strftime('%d/%m/%Y %H:%M') if despesa.data_inclusao is not None else 'Não informada'}  - Descrição: {despesa.descricao} - Valor: R${despesa.valor}")
            elif opcao == 2: # Cadastrar Despesa
                despesavalor = perguntar(questionary.text("Digite o valor da despesa:", validate=validar_valor))
                despesadescricao = perguntar(questionary.text("Digite a descrição da despesa:"))
                
                lista_despesas = gerenciador.getCategorias()

                if len(lista_despesas) == 0:
                    print('')
                    cadastrar = perguntar(questionary.select(
                        'Não há categorias cadastradas, deseja cadastrar?',
                        choices=[Choice('Sim'), Choice('Não')]
                    ))

                    if cadastrar == 'Sim':
                        cria_categoria(usuarioLogado)
                        lista_despesas = gerenciador.getCategorias()
                    elif cadastrar == 'Não':
                        print('Cancelando criação da despesa...')
                        break
                categoria = perguntar(questionary.select(
                    "Selecione a categoria da despesa:",
                    choices=[Choice(categoria.nome + " - " + categoria.descricao, value=categoria.id_categoria) for categoria in lista_despesas]
                ))
                print('Despesa Cadastrada com Sucesso! Valor: ' + despesavalor + ' - Descrição: ' + despesadescricao + ' - Categoria: ' + str(categoria))
                gerenciador.despesas.append(Despesas(id_usuario=usuarioLogado.id_usuario, descricao=despesadescricao, valor=despesavalor, id_categoria=categoria))
                gerenciador.gravardados()
            elif opcao == 3: # Editar Despesa
                despesa_editavel = perguntar(questionary.select(
                    "Selecione a despesa para edição:",
                    choices=[Choice(despesa.descricao + " - R$" + despesa.valor, value=despesa) for despesa in gerenciador.getDespesas()]
                ))
                
                despesadescricao = perguntar(questionary.text("Digite a descrição da despesa:"))

                despesavalor = perguntar(questionary.text("Digite o valor da despesa:"))

                despesa_editavel.valor = despesavalor
                despesa_editavel.descricao = despesadescricao
                gerenciador.gravardados()
            elif opcao == 4: # Excluir Despesa
                despesa_apagavel = perguntar(questionary.select(
                    "Selecione a despesa para exclusão:",
                    choices=[Choice(despesa.descricao + " - R$" + despesa.valor, value=despesa.id_despesa) for despesa in gerenciador.getDespesas()]
                ))
                
                for despesa in gerenciador.despesas:
                    if despesa.id_despesa == despesa_apagavel:
                        gerenciador.despesas.remove(despesa)
                        gerenciador.gravardados()
                        print("Despesa excluída com sucesso!")
                        break
        except LookupError:
            opcao = 0
            pass
    

    print("Voltando ao menu...")