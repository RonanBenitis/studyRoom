# === O QUE É CADEIA DE CARACTERES ===
    # O que entendemos como frase, é interpretado, na computação, como uma cadeia de caracteres (string).
    # No Python, ela aparecerá entre aspas simples ou duplas.

# === ATRIBUIÇÃO DE STRING ===
    # Quando atribuimos uma frase de um texto, sendo uma string, em uma variável, a frase não é indexada por inteiro, mas sim indexa-se letra por letra fazendo que cada letra "ocupe micro espaços" (na real, a frase inteira ocupara um espaço na memória, mas cria-se endereço para cada letra incluindo os espaços vazios), ou seja, para a cadeira de caractereses "Ronan", os endereços dessa cadeira será R(0)o(1)n(2)a(3)n(5), (no caso, o caracter (seu_endereço)).
    # Esse endereçamento caracter por caracter possibilita realizar diversas operações.

# === SUMÁRIO: OPERAÇÕES EM STRINGS ===
    # 1) Fatiamento
    # 2) Análise
    # 3) Transformação
    # 4) Divisão
    # 5) Junção
    # EXTRA: PRINTANDO MULTILINHAS
    # EXTRA2: OBJETOS E COMBINAÇÃO DE MÓDULOS

# === OPERAÇÕES: FATIAMENTO ===
    # Veja o seguinte código, para uma variavel frase = 'Curso em Vídeo Python' (contém 21 caracteres, indices que vão do 0 ao 20):
frase = 'Curso em Vídeo Python'

    # = Retorna um caracter especifico =
    # Se pedimos para printar frase[9], retorna-se a string no indice 9, que será o "V" (retornou maíusculo igual ao do texto).
print(frase[9])

    # = Retorna range de caracter =
    # Se printarmos frase[9:13], retornará "Víde", caracteres de indice 9, 10, 11, 12 excluindo o ultimo, sempre um a menos no final.
print(frase[9:13])
    # Reforçando, quando trabalhamos com Range, sempre inicia no indice indicado, e para sempre um indice a menos do número indicado no final
    # Se colocarmos frase[9:21], apesar de não ter o indice 21, como retorna até um indice a menos do indicado no range final, retornará até o indice 20, ou seja, o retorno deste fatiamento é: Vídeo Python
        ## !!Nota minha: Creio queo fatiamento, então, seja var[indice_inicio:tamanho_da_lista], pois, uma lista de tamanho 21 vai do indice 0 ao 20. Logo, creio que esse "21" é o tamanho final do recorte desejado: Do indice 9, até o tamanho 21.
        ## !!Nota minha: Pra facilitar, podemos pensar var[indice_inicio:casa_tamanho_lista], ou seja, frase[9:21] significa que inicia no indice 9 e vai até a 21º casa (indice 20).

    # = Retonar range de caracter, pulando de 2 em 2
    # frase[9:21:2], retornará "VdoPto" (9, 11, 13, 15, 17, 19)
print(frase[9:21:2])

    # = Fatiando sem indicar inicio ou fim =
    # frase[:5], começa do indice 0 e vai até a 5º casa da lista, ou seja, o 4º indice. Retorna "Curso"
print(frase[:5])

    # frase[15:], mesma lógica acima, inicia no indice 15, vai até o final da extensão da lista. Retorna "Python"
print(frase[15:])

    # frase[9::3], frase[começa no indice 9:vai até o fim:vai de 3 em 3], retorna VePh
print(frase[9::3])

# === OPERAÇÕES: ANÁLISE (muito util) ===

    # Função len() (de Length, comprimento), retorna o tamanho total da cadeia de caracters. No caso de len(frase), retorna 21 (caracteres/micro-espaços)
print(len(frase))

    # Método variavel.count() conta quantas vezes aparece o valor inserido. No caso de frase.count('o'), retorna 3 (vezes que o caracter 'o' aparece na frase atribuida)
        ## Nota: 'o' minusculo e maiusculo são valores diferentes e esse módulo é case-sensitive, logo, está contando quantos 'o' minusculos tem na frase, não contanto os maíusculos.
print(frase.count('o'))

        ## Contar e fatiar: variavel.count(valor, indice_inicio, até_qual_extensão_lista), ou eja, frase.count('o',0,13) retorna 1 'o'. Lembrando que esse 13 é até a extensão de 13 caractereses, correspondendo ao 12º indice.
print(frase.count('o',0,13))

    # Método variavel.find() encontra em qual indice o valor inserido se encontra, ou seja, frase.find('deo') retornará 11 (iniciou no 11º indice)
print(frase.find('deo'))
        ## Quando não encontra-se a string deseja, retorna-se o valor de -1. em frase.find('Android'), esse será o retorno.
print(frase.find('Android'))

    # Operador 'in' também pode ser utilizado. Nele, retorna-se True/False se um valor está em uma variavel (Valor in Variavel), ou seja, 'Curso' in frase retornará True. Isso é como perguntar "Existe o valor 'Curso' na variável frase?" e o computador retornar "Sim! (True)"
        ## Note que 'in' é um OPERADOR
print('Curso' in frase)

# === OPERAÇÕES: TRANSFORMAÇÃO ===

    # Uma lista de string é IMUTÁVEL, não conseguimos mexer diretamente nela. Mas, de uma forma secundária, conseguimos transformá-la através de métodos. A rigor, não é alterar diretamente a string em si.

    # O método variavel.replace(valor_procurado,valor_a_substituir), ou seja, em frase.replace('Python','Android'), procura-se o valor 'Python' e substitui por 'Android'.
        ## Note que será necessário aumentar o comprimento da lista para essa substituição, mas, o Python automaticamente faz isso
print(frase.replace('Python','Android'))
        ## Perceba que a string, mesmo após o replace, continua a mesma. A função replace não altera a variável, mas retorna o valor substituido apenas no momento ao qual a função foi aplicada, extinguindo sua função logo após sua conclusão. Em resumo, não altera a variável alvo, apenas substitui informações a serem apresentadas NAQUELE MOMENTO
print(frase)
        ## Isso se chama 'instância', ou seja, algo que ocorre em um local a parte do local que estamos mexendo, é uma realidade alternativa.
        ## Caso queiramos salvar essa transformação, precisamos atribuir na variável seu valor substituido, veja:
fraseSubstituir = 'Esta frase não foi substituida'
print(fraseSubstituir)
fraseSubstituir = fraseSubstituir.replace('não foi substituida', 'recebeu o .replace')
print(fraseSubstituir)
        ## Importante dizer que para alterar parte de uma string só podemos fazer desta forma, pois, caso fizermos 'fraseSubstituir[0] = 'A'', não retornará "Asta frase [...]" e sim retornará erro. Mas é possível atribuir um novo valor POR COMPLETO nessa variável. Ou seja, se quiser alterar parte do texto já atribuído em uma variável, use o replace (atribuindo ou não na variável)
        ## Note que quando usamos o replace + atribuição, estamos dizendo que vamos atribuir na variável o valor de retorno inicial da string recebendo o método de transformação .replace(). Ou seja, não estamos alterando parte da string, estamos recebendo-a inteira, mexendo nela, demonstrando e em seguida reatribuindo, sendo a mesma forma, mas automatizada, de reescrever todo o texto e atribuir com 'Esta frase recebeu o .replace'.

    # Método variavel.upper() torna os valores inseridos em maíusculo, o que já éra maísculo, continua maísuculo. O que era minusculo, vira maiusculo. A lógica de apresentar os dados transformados sem alterar a variável mantêm-se. Logo, em frase.upper(), 'Curso em Vídeo Python' se tornará 'CURSO EM VÍDEO PYTHON'
        ## Nota: Mais para frente, em Programação Orientada a Objeto, será esclarecido o que são Métodos
print(frase.upper())

    # Método variavel.lower() mesma lógica da de cima, só que tornando-o em minusculo.
print(frase.lower())

    # Método variavel.capitalize() mesma lógica acima, mas, torna o primeiro caracter da cadeia de caracteres em maiuscula, e a restante minuscula.
        ## Note que é o PRIMEIRO CARACTER, ou seja, se o primeiro caracter for um espaço, esse espaço que se torna "maiusculo" e o restante da frase ficará em minusculo
print(frase.capitalize())

    # Método variável.title() mesma lógica cima, mas, este método analisa quantas palavras tem a string entendendo como uma nova palavra por interpretar os espaços como quebras, ou seja, cada espaço separa uma nova palavra. Após essa interpretação, tornará a primeira letra de cada palavra como maíuscula, e o restante das palavras em minusculo.
print(frase.title())

    # Método variável.strip() retira todos os espaços em branco 'inuteis' da string, ou seja, os espaços em branco antes e depois dos caracteres não-vazios.
        ## Note que no exemplo abaixo, o espaço do meio é mantido
        ## Note, também, que isso alterará o comprimento da string, uma vez que os espaços também são contabilizados dentro do comprimento (length)
fraseComVazio = '   Aprenda Python   '
print(fraseComVazio)
print('A frase acima, sem strip, contém {} caracteres'.format(len(fraseComVazio)))
print(fraseComVazio.strip())
print('A frase acima, com strip, contém {} caracteres'.format(len(fraseComVazio.strip())))
    # Podemos acrescentar o modificador 'r' (right) ou 'l' (left) antes do método para indicar o sentido que o método será operacionalizado.
print(fraseComVazio.rstrip()) # Tira espaços a direita (depois dos caracteres não-vazios)
print(fraseComVazio.lstrip()) # Tira espaços a esquerda (antes dos caracteres não-vazios)

# === OPERAÇÕES: DIVISÃO ===

    # Método variável.split() separa uma string única, em seus espaços vazios, em novas strings, armazendo as novas cadeias de caracteres em uma lista. Cada cadeia de caracter recebe um endereço de indexação na lista onde estão armazenadas e cada caracter recebe endereço de indexação frente a nova realidade da string splitada. 
        ## Lógica dos indices das Cadeias de Caracter: Quando feito o split, 'Curso em Vídeo Python' passa a ser 'Curso'/'em'/'Vídeo'/'Python'. Cada seção do corte passa a ter um indice dentro de uma lista dos splitados, sendo 'Curso' o indice 0, 'em' indice 1 e por aí vai.
        ## Lógica dos indices de caracter: Antes o 'P', que tinha o indice 15 na string unitária, agora passa a ter o indice 0, uma vez que 'Python' passou a ser uma string unica e não faz mais parte da string 'Curso em Vídeo Python'. Ou seja, uma Cadeia de Caracter se comporta, também, como uma lista (pois é uma lista),
        ## Conclusão: Split gerará uma lista que armazena a divisão de uma Cadeia de Caracter (que por si só também é uma lista). Na lista do Split, terá todas as palavras separadas da string única onde, cada string splitada se comportará como uma lista dentro de uma lista.
print(frase.split())
        ## Podemos, também, atribuir à uma váriavel a lista gerada pelo split e, em seguinda, pedir para demonstrar um item especifico desta lista utilizando o seu índice:
dividido = frase.split()
print(dividido)
print(dividido[0])
        ## Caso quisermos mostrar um caracter especifico de um elemento da lista da variável que recebe a outra variável splitada, podemos fazer da seguinte forma:
print(dividido[2]) # Sò para mostrar a 3º palavra para nós, para conferência
print(dividido[2][3]) # Estamos pedindo para mostrar o 4º caracter (indice 3) do 3º elementos (indice 2) da variável dividido

# === OPERAÇÕES: JUNÇÃO ===

    # Método 'caracter_desejado'.join(variável) une todos os caracteres de uma string com o caracter_desejado. Veja a diferença entre utilizar o join em uma variável sem split e com split:
print('-'.join(frase))
print('Na frase acima, uniu cada caracter com o caracter_desejados, ou seja, cada letra e espaço vazio será conectado por - e o comprimento da variável passou de {} para {}'.format(len(frase), len('-'.join(frase))))
print('-'.join(frase.split()))
print('Já na frase acima, por termos utilizado o método .split na variável, cada porção não-vazia da string transformou-se em elementos unitários de uma lista. Utilizando o método .join fará a junção de cada porção com o caracter_desejado. Caso queiramos, podemos atribuir esse valor na mesma variável ou em uma váriavel diferente unido, novamente, a frase splitada. Essa operação fez com que o comprimento da lista frase.split(), o qual contém as frases splitadas, de {} passou a ter o comprimento da frase juntada com {} de comprimento'.format(len(frase.split()), len('-'.join(frase.split()))))

# === EXTRA: PRINTANDO MULTILINHAS ===

    # Para printar um texto longo, pulando linhas, de uma forma facil podemos utilizar colocar o texto entre 3 aspas dentro do print. Dessa forma, ele respeitará a quebra de linha do próprio texto sem precisar printar linha por linha. Veja exemplo abaixo:
print("""Mussum Ipsum, cacilds vidis litro abertis. 
Nec orci ornare consequat. Praesent lacinia ultrices consectetur. 
Sed non ipsum felis. Mauris nec dolor in eros commodo tempor. 
Aenean aliquam molestie leo, vitae iaculis nisl. 
Suco de cevadiss, é um leite divinis, 
qui tem lupuliz, matis, aguis e fermentis. 
Sapien in monti palavris qui num significa nadis i pareci latim.""")
        ## Este método é similar, mas mais facil, do que fazer print linha por linha, por exemplo:
print('Mussum Ipsum, cacilds vidis litro abertis.')
print('Nec orci ornare consequat. Praesent lacinia ultrices consectetur.')
print('[...]')

# === EXTRA2: OBJETOS E COMBINAÇÃO DE MÓDULOS ===

    # Em Python, todas as variáveis são objetos, podendo receber aplicação de módulos e combinação destes, por exemplo:
print(frase.count('O')) # Retorna 0, uma vez que há nenhum 'O' MAIUSCULO na frase 'Curso em Vídeo Python'
print(frase.upper().count('O')) # Aqui já retorna 3, pois, em frase existe nenhum 'O' MAIUSCULO, mas, em frase.upper() (ou seja, frase quando tranformada em maísculo) passa a existir 3 'O' MAIUSCULOS.

# EXERCICIO

    # Método split tem algumas funcionalidades a mais além de deixar os parenteses vazios var.split(), veja as outras funcionalidades