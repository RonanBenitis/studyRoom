# Faça um programa que leia o nome completo de uma pessoa. Mostrando, em seguida, o primeiro e o ultimo nome separadamente.

# Ex: Ana Maria de Souza = primeiro: Ana, Último: Souza

# =====   Resolução Ronan   =====

nome = str(input('Insira nome completo: ').strip())
nomeSplit = nome.split()
primNome = nomeSplit[0]
indexUltNome = len(nomeSplit) - 1
    # Para pegarmos o indice do ultimo nome, independente do tamanho do nome inserido, pegamos o valor do comprimento da lista gerada pelo split, subtraindo por 1, pois, a subtração do comprimento total de uma lista por 1 equivale ao último indice de sua lista, pois os indices são iniciados por 0 e o comprimento inicia-se por 1.
    # Após isso, atribuimos o comprimento - 1 a uma variável (indexUltNome, para ficar mais semantico, pois, poderiamos jogar direto nas chaves do indice) e chamamos essa variável (indexUltNome) no endereço da lista split.
ultNome = nomeSplit[indexUltNome]

print('\nO nome inserido foi:\n- {}\n'.format(' '.join(nomeSplit))) # Feito join no nomeSplit pra apagar qualquer espaço interno extra

print("""Segue as operações desejadas:
Primeiro nome: {};
Ultimo nome: {}.
""".format(primNome, ultNome))

# =====   RESOLUÇÃO GUANABARA   =====

# Guanabara reforça, novamente, resolver um problema por etapas.

# A resolução do Guanabara foi similiar a nossa