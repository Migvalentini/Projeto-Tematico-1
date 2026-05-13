import questionary
from questionary import Choice
from src.classes.usuarios import Usuario
from src.classes.despesas import Despesas
from src.classes.rendas import Rendas
from src.classes.categorias import Categoria
from src.armazenamento import gerenciador


despesas_logado = None
rendas_logado = None
categorias_logado = None

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
        Choice("Editar Renda Mensal", value=6),
        Choice("Excluir Renda Mensal", value=7),
        Choice("Cadastrar Despesa", value=2),
        Choice("Editar Despesa", value=8),
        Choice("Excluir Despesa", value=9),
        Choice("Exibir Meu Dados", value=3),
        Choice("Cadastrar categorias", value=4),
        Choice("Voltar para o Menu Principal", value=5),
    ]).ask()

    return choice

def menu_logado(dic = {}):
    print("===============================================================================================")
    print("Seja Muito Bem-Vindo " + dic.nome + "!")
    print("Aqui é o menu para usuários logados, onde você pode acessar as funcionalidades do sistema!")
    print("===============================================================================================")
    
    despesas_logado = [despesa for despesa in gerenciador.despesas if despesa.id_usuario == dic.id_usuario]
    renda_logado = [renda for renda in gerenciador.rendas if renda.id_usuario == dic.id_usuario]

    
    print(despesas_logado)

    opcao = 0
    while (opcao != 5):
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
        elif opcao == 4: #Cadastar categorias
            categorianome = questionary.text("Digite o nome da nova categoria").ask()
            categoriadesc = questionary.text("Digite a descrição da nova categoria").ask()
            gerenciador.categorias.append(Categoria(nome=categorianome, descricao=categoriadesc))
            gerenciador.gravardados()
        elif opcao == 6:
            renda_editavel = questionary.select(
                "Selecione a renda para edição:",
                choices=[Choice(renda.descricao + " - R$" + renda.valor, value=renda) for renda in renda_logado]
            ).ask()
            
            rendadescricao = questionary.text("Digite a descrição da renda:").ask()

            rendavalor = questionary.text("Digite o valor da renda:").ask()

            renda_editavel.valor = rendavalor
            renda_editavel.descricao = rendadescricao
            gerenciador.gravardados()
        elif opcao ==7:
            renda_apagavel = questionary.select(
                "Selecione a renda para exclusão:",
                choices=[Choice(renda.descricao + " - R$" + renda.valor, value=renda.id_renda) for renda in renda_logado]
            ).ask()
             
            for renda in gerenciador.rendas:
                if renda.id_renda == renda_apagavel:
                    gerenciador.rendas.remove(renda)
                    break
            gerenciador.gravardados()
        elif opcao == 8:
            despesa_editavel = questionary.select(
                "Selecione a despesa para edição:",
                choices=[Choice(despesa.descricao + " - R$" + despesa.valor, value=despesa) for despesa in despesas_logado]
            ).ask()
            
            despesadescricao = questionary.text("Digite a descrição da despesa:").ask()

            despesavalor = questionary.text("Digite o valor da despesa:").ask()

            despesa_editavel.valor = despesavalor
            despesa_editavel.descricao = despesadescricao
            gerenciador.gravardados()
        elif opcao == 9:
            despesa_apagavel = questionary.select(
                "Selecione a despesa para exclusão:",
                choices=[Choice(despesa.descricao + " - R$" + despesa.valor, value=despesa.id_despesa) for despesa in despesas_logado]
            ).ask()
             
            for despesa in gerenciador.despesas:
                if despesa.id_despesa == despesa_apagavel:
                    gerenciador.despesas.remove(despesa)
                    break
            gerenciador.gravardados()
            pass

    print("Encerrando...")