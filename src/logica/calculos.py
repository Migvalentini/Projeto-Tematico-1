from datetime import datetime
from src.armazenamento import gerenciador

def DataInicialConvertida(dataInicial):
    return datetime.strptime(dataInicial, "%d/%m/%Y").date()

def SaldoRestante(dataInicial):
    dataInicialConvertida = DataInicialConvertida(dataInicial)

    despesas = sum(float(despesa.valor) for despesa in gerenciador.getDespesas() if despesa.data_inclusao is not None and despesa.data_inclusao.date() >= dataInicialConvertida)
    rendas = sum(float(renda.valor) for renda in gerenciador.getRendas() if renda.data_inclusao is not None and renda.data_inclusao.date() >= dataInicialConvertida)
    
    saldo_restante = rendas - despesas
    porcentagem_restante = (saldo_restante / rendas * 100) if rendas != 0 else 0

    return rendas, despesas, saldo_restante, porcentagem_restante

def TotalDeDespesas(dataInicial):
    dataInicialConvertida = DataInicialConvertida(dataInicial)
                
    total_despesas = sum(float(despesa.valor) for despesa in gerenciador.getDespesas() if despesa.data_inclusao is not None and despesa.data_inclusao.date() >= dataInicialConvertida)

    return total_despesas

def TotalDeDespesasPorCategoria(dataInicial):
    dataInicialConvertida = DataInicialConvertida(dataInicial)

    rendas = sum(float(renda.valor) for renda in gerenciador.getRendas() if renda.data_inclusao is not None and renda.data_inclusao.date() >= dataInicialConvertida)
    categorias = {}
    for despesa in gerenciador.getDespesas():             
        if despesa.data_inclusao is not None and despesa.data_inclusao.date() >= dataInicialConvertida:
            categoria_nome = next((categoria.nome for categoria in gerenciador.getCategorias() if categoria.id_categoria == despesa.id_categoria), "Sem Categoria")
            categorias[categoria_nome] = categorias.get(categoria_nome, 0) + float(despesa.valor)

    return categorias

def TotalDeRendas(dataInicial):
    dataInicialConvertida = DataInicialConvertida(dataInicial)

    total_rendas = sum(float(renda.valor) for renda in gerenciador.getRendas() if renda.data_inclusao is not None and renda.data_inclusao.date() >= dataInicialConvertida)

    return total_rendas

def MaiorDespesa(dataInicial):
    dataInicialConvertida = DataInicialConvertida(dataInicial)
                
    maior_despesa = max((float(despesa.valor) for despesa in gerenciador.getDespesas() if despesa.data_inclusao is not None and despesa.data_inclusao.date() >= dataInicialConvertida), default=0)

    return maior_despesa

def MaiorRenda(dataInicial):
    dataInicialConvertida = DataInicialConvertida(dataInicial)

    maior_renda = max((float(renda.valor) for renda in gerenciador.getRendas() if renda.data_inclusao is not None and renda.data_inclusao.date() >= dataInicialConvertida), default=0)

    return maior_renda

def ImpactoDeCategoriaSobRenda(categoria):
    despesas_categoria = sum(float(despesa.valor) for despesa in gerenciador.getDespesas() if despesa.id_categoria == categoria.id_categoria)
    total_rendas = sum(float(renda.valor) for renda in gerenciador.getRendas())

    porcentagem_impacto = (despesas_categoria / total_rendas * 100) if total_rendas != 0 else 0

    return despesas_categoria, porcentagem_impacto

def MediaDiariaDeDespesas():
    despesas_por_dia = {}
    for despesa in gerenciador.getDespesas():
        if despesa.data_inclusao is not None:
            data_str = despesa.data_inclusao.strftime("%d/%m/%Y")
            despesas_por_dia[data_str] = despesas_por_dia.get(data_str, 0) + float(despesa.valor)

    return despesas_por_dia