import questionary
from questionary import Choice

#Despesas Fixas: São aquelas que ocorrem regularmente e têm valores relativamente estáveis, como aluguel, prestações de financiamento, seguros, mensalidades escolares e serviços de assinatura.
#Despesas Variáveis: Diferentemente das fixas, essas despesas podem variar de um mês para outro. Incluem contas de luz, água, gás, telefone, alimentação, transporte e entretenimento.
#Despesas Ocasionais: São despesas que não ocorrem mensalmente, mas que podem ter um impacto significativo no orçamento, como presentes, viagens, reparos em casa, compra de eletrodomésticos e roupas.
#Despesas Emergenciais: São despesas imprevistas e, muitas vezes, urgentes, como problemas de saúde, acidentes, reparos emergenciais no carro ou na residência.
#Despesas de Lazer: Incluem atividades relacionadas ao lazer e bem-estar, como cinema, restaurantes, passeios, academias e hobbies.
#Despesas de Investimento: Embora não sejam exatamente um gasto, é importante considerar investimentos como uma parte do orçamento, incluindo aplicações financeiras, compra de imóveis e investimentos em educação.

#Por enquanto, criei de forma fixa as categorias, mas futuramente podemos criar uma funcionalidade para o usuário criar suas próprias categorias, ou até mesmo editar as categorias pré-definidas.
categorias = [
    {"id_categoria": 1, "nome": "Despesas Fixas"},
    {"id_categoria": 2, "nome": "Despesas Variáveis"},
    {"id_categoria": 3, "nome": "Despesas Ocasionais"},
    {"id_categoria": 4, "nome": "Despesas Emergenciais"},
    {"id_categoria": 5, "nome": "Despesas de Lazer"},
    {"id_categoria": 6, "nome": "Despesas de Investimento"}
]

#Dados referentes a todos os usuários, onde cada usuário terá um dicionário com suas informações, como id, renda mensal e despesas.
dados = [
    {
        'id_usuario': 0, 
        'rendas': [],
        'despesas': [],
    }
]

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
    print("Seja Muito Bem-Vindo " + dic['user'] + "!")
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
                choices=[Choice(categoria["nome"], value=categoria["id_categoria"]) for categoria in categorias]
            ).ask()        
        elif opcao == 3: #Exibir Meu Dados
            resultado = next((dado for dado in dados if dic['id_usuario'] == dado["id_usuario"]), None)
            print(resultado)
    print("Encerrando...")