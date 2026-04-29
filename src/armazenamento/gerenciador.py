from src.classes.usuario import Usuario
from src.classes.categoria import Categoria
from src.classes.despesas import Despesas
from src.classes.rendas import Rendas

usuarios = []
usuario_logado = Usuario()

#Dados referentes a todos os usuários, onde cada usuário terá um dicionário com suas informações, como id, renda mensal e despesas.
rendas = [
    Rendas(id_usuario=1, descricao="salario", valor="1800")
]

despesas = [
    Despesas(id_usuario=1, descricao="conta de luz", valor="15000")
]

#Por enquanto, criei de forma fixa as categorias, mas futuramente podemos criar uma funcionalidade para o usuário criar suas próprias categorias, ou até mesmo editar as categorias pré-definidas.
categorias = [
    Categoria(nome="Despesas Fixas",           descricao="Ocorrem regularmente com valores estáveis, como aluguel, financiamentos, seguros e mensalidades."),
    Categoria(nome="Despesas Variáveis",       descricao="Variam mês a mês, como contas de luz, água, gás, alimentação, transporte e entretenimento."),
    Categoria(nome="Despesas Ocasionais",      descricao="Não ocorrem mensalmente, mas impactam o orçamento, como viagens, presentes e compra de eletrodomésticos."),
    Categoria(nome="Despesas Emergenciais",    descricao="Imprevistas e urgentes, como problemas de saúde, acidentes e reparos emergenciais."),
    Categoria(nome="Despesas de Lazer",        descricao="Relacionadas ao bem-estar e entretenimento, como cinema, restaurantes, academias e hobbies."),
    Categoria(nome="Despesas de Investimento", descricao="Aplicações financeiras, compra de imóveis e investimentos em educação e desenvolvimento pessoal."),
]