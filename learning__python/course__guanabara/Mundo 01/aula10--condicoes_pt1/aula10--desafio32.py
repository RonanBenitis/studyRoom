# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
    # Tente entender como funciona um ano bissexto e aplica no código

# =====   RESOLUÇÃO RONAN   =====
from datetime import date # Ver ALTERAÇÃO 1

ano = int(input('Para ver se o ano inserido é bissexto, insira o ano desejado OU coloque 0 para analisar o ano atual: ')) # Ver ALTERAÇÃO 1

# Ano Bissexto = Anos divisiveis por 4, exceto terminados em 00

# Ver ALTERAÇÃO 1
if ano == 0:
    ano = date.today().year

# Resolução utilizando as ferramentas que aprendemos até o momento:
if ano % 4 == 0:
    if ano % 10 != 0:
        print ('SIM! O ano {} é bissexto!'.format(ano))
    else:
        print('NÃO! O ano {} não é bissexto!'.format(ano))

# Resolução utilizando operadores relacionais e lógicos:
if ano % 4 == 0 and ano % 10 != 0 : # Ver CORREÇÃO 1.
    print ('SIM! O ano {} é bissexto!'.format(ano))
else:
    print('NÃO! O ano {} não é bissexto!'.format(ano))

# Código correto:

# Ano Bissexto = Anos divisiveis por 4, exceto multiplos de 100 que não são multiplos de 400.
    # Logo, para o ano ser bissexto, ele deve ser divisível por 4 (ano % 4 == 0) E (and) ele não pode ser multiplo de 100 (ano % 100 != 0). Somente é bissexto sendo divisível por 100 (ano % 100 != 0) se este for multiplo de 400 (ano % 400 == 0).
    # O código ficará, então com as seguintes declarações: (A) ano % 4 == 0 / and / (B) ano % 100 != 0 / or / (C) ano % 400 == 0. 
        # Fizemo isso pois a condição A SEMPRE deverá ser verdadeira, logo, usou-se and.
        # Já a declaração B e C precisamos que, no minimo, uma delas seja verdadeira:
            # O número É divisivel por 4 (A = T), não é multiplo de 100 (B = T) e é divisivel por 400 (C = T): T and T or T = True
            # O número é divisivel por 4 (A = T), é multiplo de 100 (B = F) e é divisivel por 400 (C = T): T and F or T = True. Essa é a exceção traduzida em código, quando o número É multiplo de 100, mas também é de 400.
            # O número é divisivel por 4 (A = T), não é multiplo de 100 (B = T) e não é divisivel por 400 (C = F). Essa é a ocorrência mais comum, quando não é multiplo de 100 e também não é de 400. Ele continua sendo bissexto.
            # O número é divisíveel por 4 (A = T), é multiplo de 100 (B = F) e não é divisível por 400 (C = F): T and F or F = False. Logo, essa é a exceção de ser bissexto quando multiplo de 100. Se ele for multiplo de 100 e não é multiplo de 400, ele não é bissexto.
    
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ('SIM! O ano {} é bissexto!'.format(ano))
else:
    print('NÃO! O ano {} não é bissexto!'.format(ano))


# =====   RESOLUÇÃO GUANABARA   =====

# Guanabara resolveu com os operadores lógicos e, em regra que ele pesquisou, o ano não pode ser divisível por 100 OU 400.
    
# CORREÇÃO 1
    # Onde vimos, indicava que o ano não pode terminar em 00, logo, não pode ser divisível por 100, e não por 10.
    # Em pesquisa do Guanabara, foi verificado que não pode ser por 400 também.

# ALTERAÇÃO 1
    # Guanabara ensinou um módulo para conseguir buscar o ano do sistema e criou um método com condição para o usuário selecionar essa opção.
    # Além das linhas de código criadas, alterou-se o texto também para possibilitar essa opção.