def custo_mercadoria(estoque_inicial, estoque_final, compras):
    cmv = estoque_final + compras - estoque_inicial
    print ("O estoque atual é de:", cmv)


def valor_compras_periodo(estoque_inicial, estoque_final):
    valor_compras_periodo = estoque_final - estoque_inicial
    print (" valor de compras:", valor_compras_periodo)
    