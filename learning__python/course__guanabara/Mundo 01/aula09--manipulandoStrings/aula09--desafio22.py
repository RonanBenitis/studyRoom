# Crie um programa que leia o nome completo de uma pessoa e mostre: 1) O nome com todas as letras maiusculas 2) O nome com todas minusculas 3) Quantas letras ao todo (sem considerar espaços) 4) Quantas letras tem o primeiro nome

# =====   RESOLUÇÃO RONAN   =====

nomeComp = str(input('Escreva seu nome completo: ').strip()) # Lê nome completo. Aplicado strip() para retirar espaços iniciais e finais
splitNome = nomeComp.split() # Lista dos nomes separados
primNome = splitNome[0] # Configurando o Primeiro Nome
nomeCompTrat = ' '.join(splitNome) # Tratamento do nome completo para deixar apenas um espaço entre os nomes, independente da quantidade de espaços o usuário inserir.

print('\nO valor inserido foi {}!\n'.format(nomeCompTrat)) # Informa o valor inserido

print("""Certo, {nome}, seguem as operações conforme desejado:
- Com todas as letras maíuscular: {tudoMai}
- Com todas as letras minusculas: {tudoMin}
- Seu nome completo tem: {contTudo} letras
- Seu primeiro nome tem: {contNome} letras""".format(
    nome = primNome, 
    tudoMai = nomeCompTrat.upper(),
    tudoMin = nomeCompTrat.lower(),
    contTudo = len(''.join(splitNome)),
    contNome = len(primNome))
    ) # VER CORREÇÃO 01 E ALTERNATIVA 01 ABAIXO

# =====   RESOLUÇÃO GUANABARA   =====

# Guanabara solicitou para atribuirmos o tipo do valor de forma expressa. Fizemos isso usando o str() para string.
# Guanabara disse que para usarmos os módulos de string, precisamos indicar que é string, por isso fizemos o passo acima.
# Com isso, Guanabara utilizou o módulo .strip() após o input para retirar os vazios antes e depois.

# =====   DIFERENÇAS   =====

#  CORREÇÃO 01: Guanabara, para contagem das letras, utilizou (len(nomeComp) - nomeComp.count(' '), dessa maneira será subtraido todo valor de caracter vazio ao total da string, assim, não importa quantos espaços vazios tenha o código retornará correto.

# ALTERNATIVA 01: Para a quantidade de letras no primeiro nome, Guanabara usou nome.find(' '), pois, esse código encontrar o endereço (indice) do primeiro espaço vazio (ou seja, o espaço entre as palavras). Como o indice é sempre um número abaixo do comprimento, dará o valor certinho da quantidade de letras do primeiro nome. A outra alternativa para resolver este problema foi o que utilizamos mesmo.