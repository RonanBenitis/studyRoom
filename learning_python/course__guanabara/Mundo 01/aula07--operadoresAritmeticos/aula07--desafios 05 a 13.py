#=========================== Desafios 05 =========================

n1 = int(input(' Informe um número inteiro: '))

print('\nO número inserido foi {}.\n- Seu antecessor: {}\n- Seu sucessor: {}'.format(n1, n1-1, n1+1))

#======================= Resolução Guanabara =====================

#Guanabara fez duas soluções, 3 var e 1 var (que é o que fiz). 3 var é bom, e obrigatorio, quando você for chamar essa variável mais vezes. 1 var é bom para quando você não tem essa necessidade e fazer as coisas em menos linha de código economiza memória.

#=========================== Desafios 06 =========================
desaf = str('06')
print('\n\n{:=^20}\n\n'.format(' Desafio {} '.format(desaf)))

n1 = int(input('Informe um número: '))


print('\nO número inserido foi: {}.\n- Seu dobro: {}\n- Seu triplo: {}\n- Sua raiz quadrada: {:.2f}'.format(n1, n1*2, n1*3, n1**(1/2)))

#======================= Resolução Guanabara =====================

#Idem ao desafio 05. Raiz vale: var**(1/2) é a forma que se faz a raiz, pois, coloca-se em parenteses pra indicar que o (1/2) precisa ser executado antes. Se não fizessemos isso, seria feita uma exponenciação com 1 e sem seguida dividir por 2
#Raiz quadrada pode ser feita com a função power também, pow(n, (1/2))

#=========================== Desafios 07 =========================
desaf = str('07')
print('\n\n{:=^20}\n\n'.format(' Desafio {} '.format(desaf)))

nota1 = float(input('1º nota do aluno: '))
nota2 = float(input('2º nota do aluno: '))

print('A média da 1º nota {:.2f} e 2º nota {:.2f} é {:.2f}'.format(nota1, nota2, (nota1+nota2)/2))

#======================= Resolução Guanabara =====================

#Eu havia colocado int, esqueci de colocar float.
#Importante colocar a soma das notas entre parenteses para respeitar a ordem de precedencia. Se não colocarmos em parenteses, será feita nota1 + a nota2 dividade por 2.
#Python usa as regras algebricas de arrendondamento.

#=========================== Desafios 08 =========================
desaf = str('08')
print('\n\n{:=^20}\n\n'.format(' Desafio {} '.format(desaf)))

metro = float(input('Valor em metros: '))

print('{:.2f} metros equivale a {:.2f} centimentos e {:.2f} milimetros.'.format(metro, metro*100, metro*1000))

#======================= Resolução Guanabara =====================

#Guanabara fez com três var: medida, cm e mm, fazendo cm = medida*100 e mm = medida*1000

#=========================== Desafios 09 =========================
desaf = str('09')
print('\n\n{:=^20}\n\n'.format(' Desafio {} '.format(desaf)))

n1 = int(input('Para a tabuada, informe um numero inteiro: '))
mult = 1

print('\nTabuada do {}:'.format(n1))
print('{}x{:2} = {}'.format(n1, mult, n1*mult)) #x1
mult += 1
print('{}x{:2} = {}'.format(n1, mult, n1*mult)) #x2
mult += 1
print('{}x{:2} = {}'.format(n1, mult, n1*mult)) #x3
mult += 1
print('{}x{:2} = {}'.format(n1, mult, n1*mult)) #x4
mult += 1
print('{}x{:2} = {}'.format(n1, mult, n1*mult)) #x5
mult += 1
print('{}x{:2} = {}'.format(n1, mult, n1*mult)) #x6
mult += 1
print('{}x{:2} = {}'.format(n1, mult, n1*mult)) #x7
mult += 1
print('{}x{:2} = {}'.format(n1, mult, n1*mult)) #x8
mult += 1
print('{}x{:2} = {}'.format(n1, mult, n1*mult)) #x9
mult += 1
print('{}x{:2} = {}'.format(n1, mult, n1*mult)) #x10

#======================= Resolução Guanabara =====================

#Guanabara resolveu tudo dentro do print (format(num, 1, num*1), replica)
#Para não sair do formato so numeros que não tem duas casas decimais para quando aparecem números com duas casas decimas, Guanabara recomendou usar o {:2}. Formata todos os números em espaço de 2 casas.
#Guanabara usou o multiplicador de string para deixar mais bonito também. print('-' * 12)

#=========================== Desafios 10 =========================
desaf = str('10')
print('\n\n{:=^20}\n\n'.format(' Desafio {} '.format(desaf)))

dolEmReal = float(input('Qual é a cotação do dolar em reais?: R$'))
cart = float(input('Quantos reais você tem na carteira?: R$'))

print('Você tem R${:.2f}, correto? Você poderá comprar US${:.2f} com este valor.'.format(cart, cart/dolEmReal))
print('Cotação do dolar: U$1.00 = R${:.2f}'.format(dolEmReal))

#======================= Resolução Guanabara =====================

#Guanabara recomendo ter o R$ no input, pois, se digitar diferente de número crashará.

#=========================== Desafios 11 =========================
desaf = str('11')
print('\n\n{:=^20}\n\n'.format(' Desafio {} '.format(desaf)))

largPar = float(input('Largura da parede: '))
altPar = float(input('Altura da parede: '))
areaPar = largPar * altPar

print('A area de uma parede de {:.2f}m de largura por {:.2f}m de altura é {:.2f}m²'.format(largPar, altPar, areaPar))
print('Se 1 litro de tinta pinta uma área de 2m², então, para uma parede de {:.2f}m² precisará de {:.2f}L de tinta'.format(areaPar, areaPar*0.5))

#======================= Resolução Guanabara =====================

#Guanabara, nesse caso, trouxe a área de tinta como variavel (tinta = area/2)

#=========================== Desafios 12 =========================
desaf = str('12')
print('\n\n{:=^20}\n\n'.format(' Desafio {} '.format(desaf)))

camisa = float(input('Qual o valor da camiseta?: (decimal em ponto, não virgula) R$'))
descTx = .05 #5%. Desconto é produto - (produto*0,05)

print('Para uma camisa de R${:.2f} com {} porcento de desconto, o valor com desconto é R${:.2f}.'.format(camisa, descTx*100, camisa - (camisa*descTx)))

#======================= Resolução Guanabara =====================

#Guanabara usou a formatação da regra de 3 e montou uma variavel com isso. semdp. novo = preço - (preço * 5 / 100)
# Esse preço * 5 / 100 equivale a formatação da regra de 3. Se Preço é = 100%, 5$ de x é quanto? É preço * 5 / 100, 5 por cento de preço
#Cuidado com o simbolo de %, que no caso da programação é o resto da divisão inteira

#=========================== Desafios 13 =========================
desaf = str('13')
print('\n\n{:=^20}\n\n'.format(' Desafio {} '.format(desaf)))

salario = float(input('Qual seu salário?: (Use ponto como decimal) R$'))
aumTx = 0.15 #15%, aumento calcula como salario + (salario*15%)

print('Você teve um aumento de {:.2f} porcento! Seu salário de R${:.2f} passou a ser R${:.2f}'.format(aumTx*100, salario, salario + (salario * aumTx)))

#======================= Resolução Guanabara =====================

#Mesma lógica do exercicio 12, só que ao invés de subtrair, somaremos.
