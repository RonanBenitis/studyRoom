# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo
    # Existe um principio matematico que identifica isso

# =====   RESOLUÇÃO RONAN   =====

# Em pesquisa, o princípio matemático é a "condição de existência de um triangulo">
    # A soma de dois lados (seja qual for) sempre deverá ser maior que o terceiro lado, ou seja, a + b > c | b + c > a | a + c > b
    # Referência: https://brasilescola.uol.com.br/matematica/triangulo.htm#:~:text=Dados%20tr%C3%AAs%20segmentos%20de%20reta,menor%20que%20o%20terceiro%20lado.

a = float(input('Informe um comprimento de reta: '))
b = float(input('Informe outro comprimento de reta: '))
c = float(input('Informer mais um comprimento de reta: '))

# Resolução com as ferramentas que temos:
if a + b > c:
    if a + c > b:
        if b + c > a:
            print('SIM! Com os comprimentos de reta {:.2f}, {:.2f} e {:.2f} pode-se formar um triângulo!'.format(a, b, c))
        else:
            print('NÃO! Com os comprimento de reta {:.2f}, {:.2f} e {:.2f} não se pode formar um triângulo!'.format(a, b, c))
    else:
        print('NÃO! Com os comprimento de reta {:.2f}, {:.2f} e {:.2f} não se pode formar um triângulo!'.format(a, b, c))
else:
    print('NÃO! Com os comprimento de reta {:.2f}, {:.2f} e {:.2f} não se pode formar um triângulo!'.format(a, b, c))
    
# Resolução com operadores lógicos:
if a + b > c and a + c > b and b + c > a:
    print('SIM! Com os comprimentos de reta {:.2f}, {:.2f} e {:.2f} pode-se formar um triângulo!'.format(a, b, c))
else:
    print('NÃO! Com os comprimento de reta {:.2f}, {:.2f} e {:.2f} não se pode formar um triângulo!'.format(a, b, c))

# =====   RESOLUÇÃO GUANABARA   =====
    
print('-=' * 20)
print('Analisador de Triângulos')
print('-=' * 20)
# Vamos usar nossas variaveis
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima podem formar triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')

# Resolvemos igual ao Guanabara na 2º forma, com as diferenças que somamos primeiro e validamos depois e Guanabara estilizou com separadores inicialmente.