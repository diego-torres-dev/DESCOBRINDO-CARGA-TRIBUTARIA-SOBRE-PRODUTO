# Dados do produto
preco_final = 1500
custo_unitario = 400
lucro = 800


def obter_carga_tributaria(preco, custo, lucro):
    """Calcula a carga tributária que incide sobre um produto

    Parâmetros:
        preco (float): preço final do produto
        custo (float): custo unitário do produto
        lucro (float): lucro obtido com a venda de uma unidade do produto

    Retorno:
        carga_tributaria (float): carga tributária que incide sobre o produto
    """
    carga_tributaria = (preco - custo - lucro) / preco
    return carga_tributaria


# Calcula a carga tributária para o produto
carga_tributaria = obter_carga_tributaria(preco_final, custo_unitario, lucro)

# Exibe o valor da carga tributária
print('Carga Tributária: {:.2%}'.format(carga_tributaria))
