import questionary
from questionary import Choice
from src.classes.rendas import Rendas
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
    "Bem vindo! O que deseja fazer?",
    choices=[
        Choice("Listar rendas mensais", value=1),
        Choice("Cadastrar renda mensal", value=2),
        Choice("Editar renda mensal", value=3),
        Choice("Excluir renda mensal", value=4),
        Choice("Voltar", value=5),
    ]).ask()

    return choice

def menu_rendas():
    usuarioLogado = gerenciador.getUsuarioLogado()

    opcao = 0
    while (opcao != 5):
        opcao = chama_menu()
        if opcao == 1: # Listar Rendas Mensais
            print("Rendas Mensais:")
            for renda in gerenciador.getRendas():
                print(f" Data: {renda.data_inclusao.strftime('%d/%m/%Y %H:%M') if renda.data_inclusao is not None else 'Não informada'} - Descrição: {renda.descricao} - Valor: R${renda.valor}")
        elif opcao == 2: # Cadastrar Renda Mensal
            rendavalor = questionary.text("Digite o valor da sua renda:", validate=validar_valor).ask()
            rendadescricao = questionary.text("Digite a descrição da sua renda:").ask()
            print('Renda Mensal Cadastrada com Sucesso! Valor: ' + rendavalor + ' - Descrição: ' + rendadescricao)
            gerenciador.rendas.append(Rendas(id_usuario=usuarioLogado.id_usuario, descricao=rendadescricao, valor=rendavalor))
            gerenciador.gravardados()
        elif opcao == 3: # Editar Renda Mensal
            renda_editavel = questionary.select(
                "Selecione a renda para edição:",
                choices=[Choice(renda.descricao + " - R$" + renda.valor, value=renda) for renda in gerenciador.getRendas()]
            ).ask()
            
            rendadescricao = questionary.text("Digite a descrição da renda:").ask()

            rendavalor = questionary.text("Digite o valor da renda:").ask()

            renda_editavel.valor = rendavalor
            renda_editavel.descricao = rendadescricao
            gerenciador.gravardados()
        elif opcao == 4: # Excluir Renda Mensal
            renda_apagavel = questionary.select(
                "Selecione a renda para exclusão:",
                choices=[Choice(renda.descricao + " - R$" + renda.valor, value=renda.id_renda) for renda in gerenciador.getRendas()]
            ).ask()
             
            for renda in gerenciador.rendas:
                if renda.id_renda == renda_apagavel:
                    gerenciador.rendas.remove(renda)
                    gerenciador.gravardados()
                    print("Renda excluída com sucesso!")
                    break

    print("Voltando ao menu...")