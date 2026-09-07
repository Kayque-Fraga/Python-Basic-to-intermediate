n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m >= 7:
    print('Aprovado!')
else:
    print('Reprovado!')
print('Primeira nota do aluno: {:.1f}\nSegunda nota do aluno: {:.1f}\nA média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, n1, n2, m))