import requests
import datetime


# Seleciona parte do texto que será manipulado
# cortando_texto(obj = texto, substring = palavra chave para iniciar o corte, start = index para começar o corte, qtd = quantidade de caracteres a ser buscada)
def cortando_texto(obj, substring = None, start = 0, qtd = None):
    qtd = len(obj) if qtd is None else qtd

    if substring:
        inicio = obj.find(substring)
        return obj[inicio:inicio+qtd]
    elif not substring:
        return obj[start:start+qtd]


# Recebe o caminho do arquivo que será manipulado e trata os dados
def manipula_dados(caminho_arquivo):
    conteudo = open(caminho_arquivo, 'r', encoding='UTF-8')
    conteudo_formatado = conteudo.read()

    loops = len(conteudo_formatado) / 81
    inicio_corte = 0

    array_dados_formatados = []

    tipos = ["Null", "Débito", "Boleto", "Financiamento", "Crédito", "Recebimento", "Vendas", "Recebimnto TED", "Recebimento DOC", "Aluguel"]

    for index in range(len(conteudo_formatado)):
        dados = conteudo_formatado[inicio_corte: -1]
        regex = '{}:{}:{}'
        hora = cortando_texto(dados, "", 42, 6).rstrip()
        # Intera sobre cada parte de texto armazenado em "dados" e salva em sua respectiva chave.
        if index < loops:
            dado_formatado = {
                "tipo": tipos[int(cortando_texto(dados, "", 0, 1).rstrip())],
                "data": cortando_texto(dados, "", 1, 8).rstrip(),
                "valor": int(cortando_texto(dados, "", 9, 10).rstrip()) / 100.00,
                "cpf": cortando_texto(dados, "", 19, 11).rstrip(),
                "cartao": cortando_texto(dados, "", 30, 12).rstrip(),
                "hora": regex.format(hora[:2], hora[2:4], hora[4:6]),
                "dono_da_loja": cortando_texto(dados, "", 48, 14).rstrip(),
                "nome_loja": cortando_texto(dados, "", 62, 19).replace("\n", "").rstrip()
            }
            
            array_dados_formatados.append(dado_formatado)
            inicio_corte += 81

    return array_dados_formatados


# Recebe o caminho do arquivo
print("Digite o caminho até o arquivo:")
caminho = input()

# Faz a requisição para salvar no banco de dados os dados que foram tratados
for dict_data in manipula_dados(caminho):
    requisicao = requests.post("http://127.0.0.1:8000/api/trasacoes/", data=dict_data)

