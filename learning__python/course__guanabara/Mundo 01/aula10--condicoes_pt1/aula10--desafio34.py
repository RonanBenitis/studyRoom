# Escreva um programa que pergunte o salário de um funcionário e calcule o valor de seu aumento.
    # Para salários superiores a R$1.250,00, calcule um aumento de 10%;
    # Para os inferiores ou iguais, o aumento é de 15%.

# =====   RESOLUÇÃO RONAN   =====
salario = float(input('Qual seu salario?: R$'))

if salario > 1250:
    aumento = salario * 0.10
    salarioAum = salario + aumento
    print('Parabéns pelo aumento de R${:.2f} (10%)! Agora seu salário passou a ser R${:.2f}'.format(aumento, salarioAum))
else:
    aumento = salario * 0.15
    salarioAum = salario + aumento
    print('Parabéns pelo aumento de R${:.2f} (15%)! Agora seu salário passou a ser R${:.2f}'.format(aumento, salarioAum))

# =====   RESOLUÇÃO GUANABARA   =====
    
if salario <= 1250: # Basicamente, Guanabara resolveu validando salários inferiores ou iguais a 1250, só validamos os superiores a 1250. Então, inferte o if/else;
    novo = salario + (salario * 15 / 100) # Guanabara perfere calcular porcentagem assim. Algo * 15 por cento, por cem, / 100, de algo.
else:
    novo = salario + (salario * 10 /100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))