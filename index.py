def cortando_texto(obj, substring = None, start = 0, qtd = None):
    qtd = len(obj) if qtd is None else qtd

    if substring:
        inicio = obj.find(substring)
        return obj[inicio:inicio+qtd]
    elif not substring:
        return obj[start:start+qtd]


def manipula_dados(caminho_arquivo):
    conteudo = open(caminho_arquivo, 'r', encoding='UTF-8')
    conteudo_formatado = conteudo.read()

    loops = len(conteudo_formatado) / 81
    inicio_corte = 0

    array_dados_formatados = []

    for index in range(len(conteudo_formatado)):
        dados = conteudo_formatado[inicio_corte: -1]
        
        if index < loops:
            dado_formatado = {
                "tipo": cortando_texto(dados, "", 0, 1).rstrip(),
                "data": cortando_texto(dados, "", 1, 8).rstrip(),
                "valor": cortando_texto(dados, "", 9, 10).rstrip(),
                "cpf": cortando_texto(dados, "", 19, 11).rstrip(),
                "cartao": cortando_texto(dados, "", 30, 12).rstrip(),
                "hora": cortando_texto(dados, "", 42, 6).rstrip(),
                "dono_da_loja": cortando_texto(dados, "", 48, 14).rstrip(),
                "nome_da_loja": cortando_texto(dados, "", 62, 19).replace("\n", "").rstrip()
            }
            
            array_dados_formatados.append(dado_formatado)
            inicio_corte = inicio_corte + 81

    return array_dados_formatados


manipula_dados("/home/allan/CNAB.txt")