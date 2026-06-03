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
    
    def carregaArquivo(nome_arquivo):
        caminho = os.path.join(diretorio, nome_arquivo)
        if not os.path.exists(caminho):
            print(f"Arquivo {nome_arquivo} não encontrado. Criando...")
            
            with open(caminho, 'w', encoding='utf-8') as f:
                json.dump([], f)

            return []
            
        if os.path.exists(caminho):
            if os.path.getsize(caminho) == 0:
                return []
            try:
                with open(caminho, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                print(f"O arquivo {nome_arquivo} estava corrompido e foi ignorado.")
                return []
        return []

    dados_usuario = carregaArquivo('usuarios.json')
    usuarios.clear()
    for item in dados_usuario:
        usuarios.append(Usuario(**item))

    dados_renda = carregaArquivo('rendas.json')
    rendas.clear()
    for item in dados_renda:
        if 'data_inclusao' in item:
            item['data_inclusao'] = datetime.fromisoformat(item['data_inclusao'])
        rendas.append(Rendas(**item))

    dados_despesa = carregaArquivo('despesas.json')
    despesas.clear()
    for item in dados_despesa:
        if 'data_inclusao' in item:
            item['data_inclusao'] = datetime.fromisoformat(item['data_inclusao'])
        despesas.append(Despesas(**item))
                
    dados_categoria = carregaArquivo('categorias.json')
    categorias.clear()
    for item in dados_categoria:
        categorias.append(Categoria(**item))

def getUsuarioLogado() -> Usuario | None:
    return usuario_logado

def getRendas() -> list[Rendas]:
    if not getUsuarioLogado():
        print("Nenhum usuário logado.")
        return []
    
    return [renda for renda in rendas if renda.id_usuario == getUsuarioLogado().id_usuario]

def getDespesas() -> list[Despesas]:
    if not getUsuarioLogado():
        print("Nenhum usuário logado.")
        return []
    
    return [despesa for despesa in despesas if despesa.id_usuario == getUsuarioLogado().id_usuario]

def getUsuarios() -> list[Usuario]:
    return usuarios

def getCategorias() -> list[Categoria]:
    if not getUsuarioLogado():
        print("Nenhum usuário logado.")
        return []
    
    return [categoria for categoria in categorias if categoria.id_usuario == getUsuarioLogado().id_usuario]

def criarCategorias(cadastro) -> list[Categoria]:
    categorias.extend([
        Categoria(nome="Despesas Fixas",           descricao="Ocorrem regularmente com valores estáveis, como aluguel, financiamentos, seguros e mensalidades.",         id_usuario=cadastro.id_usuario),
        Categoria(nome="Despesas Variáveis",       descricao="Variam mês a mês, como contas de luz, água, gás, alimentação, transporte e entretenimento.",               id_usuario=cadastro.id_usuario),
        Categoria(nome="Despesas Ocasionais",      descricao="Não ocorrem mensalmente, mas impactam o orçamento, como viagens, presentes e compra de eletrodomésticos.", id_usuario=cadastro.id_usuario),
        Categoria(nome="Despesas Emergenciais",    descricao="Imprevistas e urgentes, como problemas de saúde, acidentes e reparos emergenciais.",                       id_usuario=cadastro.id_usuario),
        Categoria(nome="Despesas de Lazer",        descricao="Relacionadas ao bem-estar e entretenimento, como cinema, restaurantes, academias e hobbies.",              id_usuario=cadastro.id_usuario),
        Categoria(nome="Despesas de Investimento", descricao="Aplicações financeiras, compra de imóveis e investimentos em educação e desenvolvimento pessoal.",         id_usuario=cadastro.id_usuario),
    ])