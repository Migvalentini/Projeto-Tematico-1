from src.classes.usuarios import Usuario
from src.classes.categorias import Categoria
from src.classes.despesas import Despesas
from src.classes.rendas import Rendas
from dataclasses import asdict, is_dataclass
from datetime import datetime
import json
import os

usuarios = []
rendas = []
despesas = []
categorias = []

usuario_logado = None 
diretorio = 'src/armazenamento'

class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if is_dataclass(obj):
            return asdict(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

def gravardados():
    
    if not os.path.exists(diretorio):
        os.makedirs(diretorio)

    arquivos = {
        'rendas.json': rendas,
        'despesas.json': despesas,
        'categorias.json': categorias,
        'usuarios.json': usuarios
    }
    
    for nome_arquivo, lista in arquivos.items():
        caminho_completo = os.path.join(diretorio, nome_arquivo)
        
        with open(caminho_completo, 'w', encoding='utf-8') as f:
            json.dump(lista, f, indent=4, ensure_ascii=False, cls=EnhancedJSONEncoder)
            
def carregardados():    
    if not os.path.exists(diretorio):
        return

    caminho_u = os.path.join(diretorio, 'usuarios.json')
    if os.path.exists(caminho_u):
        with open(caminho_u, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            usuarios.clear()
            for item in dados:
                print(item)
                usuarios.append(Usuario(**item))

    caminho_r = os.path.join(diretorio, 'rendas.json')
    if os.path.exists(caminho_r):
        with open(caminho_r, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            rendas.clear()
            for item in dados:
                if 'data_inclusao' in item:
                    item['data_inclusao'] = datetime.fromisoformat(item['data_inclusao'])
                rendas.append(Rendas(**item))

    caminho_d = os.path.join(diretorio, 'despesas.json')
    if os.path.exists(caminho_d):
        with open(caminho_d, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            despesas.clear()
            for item in dados:
                if 'data_inclusao' in item:
                    item['data_inclusao'] = datetime.fromisoformat(item['data_inclusao'])
                despesas.append(Despesas(**item))
                
    caminho_c = os.path.join(diretorio, 'categorias.json')
    if os.path.exists(caminho_c):
        with open(caminho_c, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            categorias.clear()
            for item in dados:
                categorias.append(Categoria(**item))

categorias.extend([
    Categoria(nome="Despesas Fixas",           descricao="Ocorrem regularmente com valores estáveis, como aluguel, financiamentos, seguros e mensalidades."),
    Categoria(nome="Despesas Variáveis",       descricao="Variam mês a mês, como contas de luz, água, gás, alimentação, transporte e entretenimento."),
    Categoria(nome="Despesas Ocasionais",      descricao="Não ocorrem mensalmente, mas impactam o orçamento, como viagens, presentes e compra de eletrodomésticos."),
    Categoria(nome="Despesas Emergenciais",    descricao="Imprevistas e urgentes, como problemas de saúde, acidentes e reparos emergenciais."),
    Categoria(nome="Despesas de Lazer",        descricao="Relacionadas ao bem-estar e entretenimento, como cinema, restaurantes, academias e hobbies."),
    Categoria(nome="Despesas de Investimento", descricao="Aplicações financeiras, compra de imóveis e investimentos em educação e desenvolvimento pessoal."),
])