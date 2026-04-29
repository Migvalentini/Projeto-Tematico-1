import questionary
from questionary import Choice
from src.classes.usuario import Usuario
from src.classes.despesas import Despesas
from src.classes.rendas import Rendas
from src.classes.categoria import Categoria
from src.armazenamento.gerenciador import *

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
        Choice("Cadastrar Renda Mensal", value=1),
        Choice("Cadastrar Despesa", value=2),
        Choice("Exibir Meu Dados", value=3),
        Choice("Sair", value=4),
    ]).ask()

    return choice

def menu_logado(dic = {}):
    print("Seja Muito Bem-Vindo " + dic.nome + "!")
    print("Aqui é o menu para usuários logados, onde você pode acessar as funcionalidades do sistema!")
    print(dic)
    
    opcao = 0
    while (opcao != 4):
        opcao = chama_menu()
        if opcao == 1: #Cadastrar Renda Mensal
            renda = questionary.text("Digite o valor da sua renda:", validate=validar_valor).ask()
        elif opcao == 2: #Cadastrar Despesa
            valor = questionary.text("Digite o valor da despesa:", validate=validar_valor).ask()
            categoria = questionary.select(
                "Selecione a categoria da despesa:",
                choices=[Choice(categoria.nome + " - " + categoria.descricao, value=categoria.id_categoria) for categoria in categorias]
            ).ask()   
            print(categoria)     
        elif opcao == 3: #Exibir Meu Dados
            # TODO fazer algo
            print("Em produção")
    print("Encerrando...")