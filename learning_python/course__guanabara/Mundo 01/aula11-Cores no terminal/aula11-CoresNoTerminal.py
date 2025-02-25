# =====   CORES NO TERMINAL   =====

# INTRODUÇÃO
    # no Python, existem inumeras formas de fazer a mesma coisa, por exemplo, colorir com o módulo Colorize, mas, utilizaremos o padrão ANSI Escape Sequence

# CÓDIGO ANSI PARA CORES
    # O código Ansi inicia com contra-barra (\ - perto do shift) seguido do código.
    # Existe uma faixa de códigos que relacionam com cores, mas o que melhor funciona com o Python é:
        # \033[m
        # Entre o "[" e o "m", coloque de 0 a 3 códigos
    
    # Sintaxe
        # \033[_style_;_text_;_backGround_m
        # Não precisa colocar tudo, caso não queira estilizar algum dos itens, coloque 0 / 37 / 40 ou não preencha o item desejado;
        # Deixar sem preencher rodará o padrão do estilo do terminal;
        # Os códigos não seguem padrão hexadecimal ou afins, é código próprio;
        # Não há ordem para colocar o parametros, cada código já carrega seu parametro: style, text e back já tem seus códigos próprios.

    # Códigos padrão ANSI
        # Style: 0 none | 1 bold | 4 underline | 7 negative
        # Text: 30 (branco) ~ coloridos ~ 37 (gray)
        # Back: 40 (branco) ~ coloridos ~ 47 (gray)
        # Essas são as configurações BÁSICAS ANSI e que funcionam bem com Python, mas, há formas mais completas também. No momento, isso é mais do que o necessário
        # É possivel gerar letra preta, por exemplo: \033[7; 30m, ou seja, letra branca e invertemos a cor com o 7 do estilo.
        # Funcionamento do estilo 7 (negativo) = Inverte a cor do texto com seu fundo.

# =====   PRATICA   =====

print('\033[1;31;43mOlá Mundo!\033[m')
    # 1 estilo bold; 31 texto vermelho ; 43 background amarelo
    # Colocamos o código ANSI no final também, sem nada, para a estilização retornar ao padrão ali. Não é errado não colocarmos no final este código, mas, a estilização seguirá por todo o código até encontrar o próximo chamamento do código ANSI ou final do código.
    # Lembre-se de colocar dentro do Print e das aspas o código ANSI

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b)) # Forma de estilizar direto no print

nome = 'Guanabara'
print('Ola! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[32m', nome, '\033[m')) # Forma de estilizar dentro do Format, note que a estilização tá em aspas

cores = {'limpa':'\033[m', 
         'azul':'\033[34m', 
         'amarelo':'\033[33m', 
         'pretoEbranco':'\033[7;30m'} # Creio que essa estrutura de variável se chama dicionário. Ou seja, toda vez que chamarmos a variável cores, no valor de limpa, significa que estamos chamando o valor \033[m.
        # Ou seja, cortes['limpa'] = '\033[m'

print('Ola! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['azul'], nome, cores['limpa']))

# === Desafio ===

# Acrescentar cores no minimo 10 e, no maximo, em todos os 35 exercicios.