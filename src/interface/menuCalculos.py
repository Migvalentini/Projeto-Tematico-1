import questionary
from questionary import Choice
from datetime import datetime
from src.logica.calculos import *
from src.armazenamento import gerenciador
from src.utils.utils import perguntar

def validar_data(texto):
    try:
        # Tenta converter a string no formato esperado
        datetime.strptime(texto, "%d/%m/%Y")
        return True
    except ValueError:
        return "Formato inválido! Por favor, insira a data como DD/MM/AAAA."


def chama_menu():
    choice = perguntar(questionary.select(
    "Bem vindo ao Menu Cálculos! O que deseja fazer?",
    choices=[
        Choice("Saldo restante", value=1),
        Choice("Total de despesas", value=2),
        Choice("Total de despesas por categoria", value=3),
        Choice("Total de rendas", value=4),
        Choice("Maior despesa", value=5),
        Choice("Maior renda", value=6),
        Choice("Impacto de categoria sob renda", value=7),
        Choice("Média diária de despesas", value=8),
        Choice("Voltar", value=9),
    ]))

    return choice

def menu_logado():
    usuarioLogado = gerenciador.getUsuarioLogado()

    opcao = 0
    while (opcao != 9):
        try:
            opcao = chama_menu()
            if opcao == 1: # Saldo restante
                dataInicial = perguntar(questionary.text( "Insira a data de inicio para a pesquisa (DD/MM/AAAA):", validate=validar_data))
                
                rendas, despesas, saldo_restante, porcentagem_restante = SaldoRestante(dataInicial)
                
                print('Total de rendas: R$' + str(rendas))
                print('Total de despesas: R$' + str(despesas))
                print(f"Seu saldo restante é: R${saldo_restante:.2f}")
                print(f"Porcentagem restante: {porcentagem_restante:.2f}%")
            elif opcao == 2: # Total de despesas
                dataInicial = perguntar(questionary.text( "Insira a data de inicio para a pesquisa (DD/MM/AAAA):", validate=validar_data))
                
                total_despesas = TotalDeDespesas(dataInicial)
                
                print(f"Seu total de despesas é: R${total_despesas:.2f}")
            elif opcao == 3: # Total de despesas por categoria
                dataInicial = perguntar(questionary.text( "Insira a data de inicio para a pesquisa (DD/MM/AAAA):", validate=validar_data))
                
                categorias = TotalDeDespesasPorCategoria(dataInicial)

                if not categorias:
                    print("Nenhuma despesa encontrada a partir da data informada.")
                    continue
                else:
                    print("Total de despesas por categoria:")

                    for categoria, total in categorias.items():
                        print(f"  {categoria}: R${total:.2f}")
                        print(f"  Porcentagem das despesas da categoria sobre a renda total: {(total / rendas * 100) if rendas != 0 else 0:.2f}%")
            elif opcao == 4: # Total de rendas
                dataInicial = perguntar(questionary.text( "Insira a data de inicio para a pesquisa (DD/MM/AAAA):", validate=validar_data))
                
                total_rendas = TotalDeRendas(dataInicial)
                
                print(f"Seu total de rendas é: R${total_rendas:.2f}")
            elif opcao == 5: # Maior despesa
                dataInicial = perguntar(questionary.text( "Insira a data de inicio para a pesquisa (DD/MM/AAAA):", validate=validar_data))
                
                maior_despesa = MaiorDespesa(dataInicial)
                
                print(f"Sua maior despesa é: R${maior_despesa:.2f}")
            elif opcao == 6: # Maior renda
                dataInicial = perguntar(questionary.text( "Insira a data de inicio para a pesquisa (DD/MM/AAAA):", validate=validar_data))
                
                maior_renda = MaiorRenda(dataInicial)
                
                print(f"Sua maior renda é: R${maior_renda:.2f}")
            elif opcao == 7: # Impacto de categoria sob renda
                categoria = perguntar(questionary.select(
                    "Selecione a categoria para análise:",
                    choices=[Choice(categoria.nome + " - " + categoria.descricao, value=categoria) for categoria in gerenciador.getCategorias()]
                ))
                
                despesas_categoria, porcentagem_impacto = ImpactoDeCategoriaSobRenda(categoria)

                print(f"O impacto da categoria '{categoria.nome}' sobre a renda total é: R${despesas_categoria:.2f} ({porcentagem_impacto:.2f}%)")
            elif opcao == 8: # Média diária de despesas
                despesas_por_dia = MediaDiariaDeDespesas()
                
                print("Média diária de despesas:")
                for data, total in despesas_por_dia.items():
                    print(f"  {data}: R${total:.2f}")
        except LookupError:
            opcao = 0
            pass        
    print("Voltando ao menu...")