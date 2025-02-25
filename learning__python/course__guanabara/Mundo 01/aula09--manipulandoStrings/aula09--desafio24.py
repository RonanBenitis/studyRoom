# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

# =====   Resolução Ronan   =====

cidade = str(input('Digite o nome de sua cidade: ').strip())
cidadeSplit = cidade.upper().split() 
    # Splitamos o input, pois, como o nome das cidades, quando há SANTO, são compostos, logo, podemos separar cada nome em uma lista (cidadSplit, variável de validação) e fazer a pergunta se eixeste o valor 'SANTO' apenas o indice 0, já que o requisito é saber quem começa com o nome 'SANTO'.
    # Importante o uso do upper, pois assim conseguimos tornar a validação Case Insencitive, já que colocarmos a pesquisa para ser feita em Maíusculo e tornamos essa variável também em Maíusculo, independente de como o valor será inserido.


print('O valor inserido foi {}!'.format(cidade))

print('Esta cidade começa com "Santo"? (True/False): {}'.format('SANTO' in cidadeSplit[0])) # VER ALTERNATIVA 01

# =====   RESOLUÇÃO GUANABARA   =====

# Guanabara testou com print(cidade[:5] == 'Santo') para validar se a cidade começa com Santo. Esse código retorna True/False para o teste lógico de se do indice 0 ao 5 a variável Cidade tem o valor 'Santo'. O problema deste código é que qualquer variação do 'Santo' (tipo, qualquer minusculo ou maiusculo diferente dessa configuração) e se existir espaços antes já retornará como false. Pois, '   Santo' e 'SANTO' é diferente de 'Santo'.
# Guanabara iniciou retirando os espaços com .strip(), assim como fizemos.
# Para resolver isso, Guanabara fez parecido mas com a seguinte alternativa:

# ALTERNATIVA 01 - cid[:5].upper() == 'SANTO', isso também chega ao resultado desejado.