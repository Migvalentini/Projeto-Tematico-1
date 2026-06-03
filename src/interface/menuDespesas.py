import questionary
from questionary import Choice
from src.classes.despesas import Despesas
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
    "Bem vindo ao Menu Despesas! O que deseja fazer?",
    choices=[
        Choice("Listar despesas", value=1),
        Choice("Cadastrar despesa", value=2),
        Choice("Editar despesa", value=3),
        Choice("Excluir despesa", value=4),
        Choice("Voltar", value=5),
    ]).ask()

    return choice

def menu_logado():
    usuarioLogado = gerenciador.getUsuarioLogado()

    opcao = 0
    while (opcao != 5):
        opcao = chama_menu()
        if opcao == 1: # Listar Despesas
            print("Despesas:")
            for despesa in gerenciador.getDespesas():
                print(f" Data: {despesa.data_inclusao.strftime('%d/%m/%Y %H:%M') if despesa.data_inclusao is not None else 'Não informada'}  - Descrição: {despesa.descricao} - Valor: R${despesa.valor}")
        elif opcao == 2: # Cadastrar Despesa
            despesavalor = questionary.text("Digite o valor da despesa:", validate=validar_valor).ask()
            despesadescricao = questionary.text("Digite a descrição da despesa:").ask()
            
            categoria = questionary.select(
                "Selecione a categoria da despesa:",
                choices=[Choice(categoria.nome + " - " + categoria.descricao, value=categoria.id_categoria) for categoria in gerenciador.getCategorias()]
            ).ask()
            print('Despesa Cadastrada com Sucesso! Valor: ' + despesavalor + ' - Descrição: ' + despesadescricao + ' - Categoria: ' + str(categoria))
            gerenciador.despesas.append(Despesas(id_usuario=usuarioLogado.id_usuario, descricao=despesadescricao, valor=despesavalor, id_categoria=categoria))
            gerenciador.gravardados()
        elif opcao == 3: # Editar Despesa
            despesa_editavel = questionary.select(
                "Selecione a despesa para edição:",
                choices=[Choice(despesa.descricao + " - R$" + despesa.valor, value=despesa) for despesa in gerenciador.getDespesas()]
            ).ask()
            
            despesadescricao = questionary.text("Digite a descrição da despesa:").ask()

            despesavalor = questionary.text("Digite o valor da despesa:").ask()

            despesa_editavel.valor = despesavalor
            despesa_editavel.descricao = despesadescricao
            gerenciador.gravardados()
        elif opcao == 4: # Excluir Despesa
            despesa_apagavel = questionary.select(
                "Selecione a despesa para exclusão:",
                choices=[Choice(despesa.descricao + " - R$" + despesa.valor, value=despesa.id_despesa) for despesa in gerenciador.getDespesas()]
            ).ask()
             
            for despesa in gerenciador.despesas:
                if despesa.id_despesa == despesa_apagavel:
                    gerenciador.despesas.remove(despesa)
                    gerenciador.gravardados()
                    print("Despesa excluída com sucesso!")
                    break

    print("Voltando ao menu...")