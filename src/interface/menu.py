import questionary
from questionary import Choice
from src.classes.usuarios import Usuario
from src.classes.despesas import Despesas
from src.classes.rendas import Rendas
from src.classes.categorias import Categoria
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
        Choice("Cadastrar Renda Mensal", value=1),
        Choice("Cadastrar Despesa", value=2),
        Choice("Exibir Meu Dados", value=3),
        Choice("Voltar para o Menu Principal", value=4),
    ]).ask()

    return choice

def menu_logado(dic = {}):
    print("===============================================================================================")
    print("Seja Muito Bem-Vindo " + dic.nome + "!")
    print("Aqui é o menu para usuários logados, onde você pode acessar as funcionalidades do sistema!")
    print("===============================================================================================")
    
    opcao = 0
    while (opcao != 4):
        opcao = chama_menu()
        if opcao == 1: #Cadastrar Renda Mensal
            rendavalor = questionary.text("Digite o valor da sua renda:", validate=validar_valor).ask()
            rendadescricao = questionary.text("Digite a descrição da sua renda:").ask()
            print('Renda Mensal Cadastrada com Sucesso! Valor: ' + rendavalor + ' - Descrição: ' + rendadescricao)
            gerenciador.rendas.append(Rendas(id_usuario=dic.id_usuario, descricao=rendadescricao, valor=rendavalor))
            gerenciador.gravardados()
        elif opcao == 2: #Cadastrar Despesa
            despesavalor = questionary.text("Digite o valor da despesa:", validate=validar_valor).ask()
            despesadescricao = questionary.text("Digite a descrição da despesa:").ask()
            categoria = questionary.select(
                "Selecione a categoria da despesa:",
                choices=[Choice(categoria.nome + " - " + categoria.descricao, value=categoria.id_categoria) for categoria in gerenciador.categorias]
            ).ask()   
            print('Despesa Cadastrada com Sucesso! Valor: ' + despesavalor + ' - Descrição: ' + despesadescricao + ' - Categoria: ' + str(categoria))
            gerenciador.despesas.append(Despesas(id_usuario=dic.id_usuario, descricao=despesadescricao, valor=despesavalor, id_categoria=categoria))
            gerenciador.gravardados()
        elif opcao == 3: #Exibir Meu Dados
            print("Rendas:")
            for renda in gerenciador.rendas:
                if renda.id_usuario == dic.id_usuario:
                    print(renda.toString())
            print("Despesas:")
            for despesa in gerenciador.despesas:
                if despesa.id_usuario == dic.id_usuario:
                    print(despesa.toString())
            print("Usuário:")
            for usuario in gerenciador.usuarios:
                if usuario.id_usuario == dic.id_usuario:
                    print(usuario.toString())
    print("Encerrando...")