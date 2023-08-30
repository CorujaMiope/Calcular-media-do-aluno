#Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, 
#mostrando uma mensagem no final, de acordo com a média atingida:

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota: '))
nf = (n1 + n2)/2

if nf >= 6:
    print('O aluno foi aprovado com a nota {}'.format(nf))

elif nf >= 5 and nf < 6:
    print('O aluno ficou com {}, então está de recuperação'.format(nf))

else:
    print('O aluno ficou com {} então está reprovado'.format(nf))