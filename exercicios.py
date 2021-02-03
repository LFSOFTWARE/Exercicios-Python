"""
list and tuplas exercise

#exercicio 1

A= ['1', '0', '5', '-2', '-5', '7']

soma = A[0]+A[1]+A[5]
A[4]=100
#print(soma)
for i in A:
    print(i)

#exercicio 2
vetor = ['']

for x in range(0,6):
    n=int(input('Digite um valor:\n'))

    vetor.append(n)


for valor in vetor:
    print(valor)

#exercicio 3
dado = ['']
result = ['']

for x in range(0, 10):
    valor = int(input('digite um valor real\n'))
    # calcula o quadrado de todo valor informado via teclado

    quadrado = valor ** 2

    dado.append(valor)
    result.append(quadrado)

for numero in dado:
    print(numero)

for numero in result:
    print(numero)
    #exercicio 4
    vetor = []


for x in range(0,8):
    valor = int(input('digite um valor'))
    vetor.append(valor)

x=int(input())
y=int(input())


resultado  = vetor[x]+vetor[y]

print(f'o resultado da soma da posição {x}={vetor[x]} + {y}={vetor[y]} = {resultado}')
********************
# exercico 5


 #exercico 6
    vetor = []

for x in range(0, 10):
    valor = int(input('digite um valor real\n'))
    vetor.append(valor)

print(f'Minimo: {min(vetor)}')
print(f'Maximo: {max(vetor)}')

#exerccio 7

vetor = []

for x in range(0, 3):
    valor = int(input('digite um valor real\n'))
    vetor.append(valor)


maximo = max(vetor)
print(f'o maior elemento :{maximo}')
print(f'index : {vetor.index(maximo)}')

print('o vetor é :')


for x,y in enumerate(vetor):
    print(f'index:{x} valor :{y}')

#exercicio 8:
vetor = []


while len(vetor) < 6:
    x = int(input('digite um valor:'))

    vetor.append(x)


for i in range(5, 0 , -1):
    print(vetor[i])

exercicio 10

notas = []

soma = 0
while len(notas) < 15:
    nota = int(input('Digite a nota do aluno:'))
    notas.append(nota)

for x in notas:
    soma +=x

print(f'A media dos alunos é {soma/15}')


#exercicio 11
vetor = []

somaN = 0
somaP = 0

while len(vetor) < 10:
    nota = int(input('Digite um numero:'))
    if nota < 0 :
        somaN += 1
    else:
        somaP += nota
    vetor.append(nota)

print(f"a soma dos numeroas positivos desse vetor é {somaP} e a ")
print(f"quantidade de numeros negativos é {somaN}")



#exercicio 13


vetor = []

while len(vetor) < 5:
    nota = int(input('Digite um numero:'))
    vetor.append(nota)

maior = max(vetor)
menor = min(vetor)

print(f' O maior numero esta no indice :{vetor.index(maior)}')
print(f' O maior numero esta no indice :{vetor.index(menor)}')

exercicio 14

vetor = []
rep = []

while len(vetor) < 10:
    nota = int(input('Digite um numero:'))
    vetor.append(nota)

for numeros in vetor:
    quantas_vezes = vetor.count(numeros)
    if numeros in rep:
        continue

    if quantas_vezes > 1:
        print('Os valores repetidos neste vetor é:')
        print(f'{numeros}, {quantas_vezes} vezes')
        rep.append(numeros)

#exercicio 15
vetor = []

while len(vetor) < 20:
    valor = int(input('digite um valor'))
    vetor.append(valor)

x = set(vetor)

for i in x:
    print(i)

exercicio 16

vetor = []
op = 0


while len(vetor) < 5:
    valor = int(input('Valor:'))
    vetor.append(valor)


while True:
    x = 'oi'

    while True:
        try:
            op = int(input('Dite um valor'))
        except:
            print('Digite um inteiro')

        if type(op) == int:

            break
    if op == 0:
        print('saindo...')
        break
    elif op == 1:
        for x in vetor:
            print(x)
    elif op == 2:
        for num in range(4,0-1,-1):
            print(vetor[num])

    else:
        print('codigo invalido!')



exercicio 17
vetor = []

while len(vetor) < 10:
    x = int(input('Digite um valor:'))

    if x < 0:
        vetor.append(0)
    else:
        vetor.append(x)


print(vetor[::])


#exercicio 19

vetor = []

for x in range(0,51):
    i = x

    valor = (i+5*i)%(i+1)
    vetor.append(valor)

for indice,valor in enumerate(vetor):

    print(f'valor:{valor} indice:{indice}')


  #exercicio 20

A = []
B = []



resultado = []

def preencher(nome,name):
    print(f'Preencha o Vetor {name}: \n')

    while len(nome) < 10:
        dado = int(input('Digite um valor:'))
        nome.append(dado)


preencher(A,'A')
preencher(B,'B')

for i in range(0,9+1):
    valor  = A[i] * B[i]
    resultado.append(valor)


print(resultado[::])



#exercicio 24


A = []
B = []

resul = 0
def preencher(nome,name):
    print(f'Preencha o Vetor {name}: \n')

    while len(nome) < 5:
        dado = int(input('Digite um valor:'))
        nome.append(dado)


preencher(A,'A')
preencher(B,'B')


for x in range(0,4):
    resul += (A[x]*B[x])


print(resul)

exercio 24

aluno = {}

while len(aluno) < 10:
    numero = int(input('Digite o numero do aluno:'))
    altura = float(input('Digite a altura do aluno:'))

    aluno.update({altura:numero})

print(f'O menor(-) aluno é o numero {aluno.get(min(aluno))}, Com altura de {min(aluno)} M')
print(f'O Maior(+) aluno é o numero {aluno.get(max(aluno))}, Com altura de {max(aluno)} M')


#exercicio 25


a = []
numero = 0

letra = ''

while len(a) < 100:
    if numero < 10:
        if numero % 7 == 0:
            numero += 1
            continue
        else:
            a.append(numero)
            numero += 1
    else:
        letra = str(numero)

        if numero % 7 == 0 or letra[1] == '7':
            numero += 1
            continue
        else:
            a.append(numero)
            numero += 1


print(a)

#exercicio  28
v = []
v1 = []
v2 = []


while len(v) < 10:
    valor = int(input('Digite o valor:'))
    v.append(valor)
    if valor % 2 == 1:
        v1.append(valor)
    elif valor % 2 == 0:
        v2.append(valor)


for x in v1:
    print(f'impar {x}')
for x in v2:
    print(f'par {x}')


exercicio 29


vetor = []

num_pares = 0
soma_pares = 0
num_impares = 0
soma_impares = 0

while len(vetor) < 6:
    valor = int(input('Digite o valor:'))
    vetor.append(valor)
    if valor % 2 == 0:
        num_pares += 1
        soma_pares += valor
    elif valor % 2 == 1:
        num_impares += 1
        soma_impares += valor

print(f' N impates: {num_impares}   soma dos impares: {soma_impares}')
print(f'N pares {num_pares} soma dos pares {soma_pares}')

exercicio 31
etor1 = []
vetor2 = []

while len(vetor1) < 3:
    valor = int(input('Digite o valor:'))
    vetor1.append(valor)

while len(vetor2) < 3:
    valor = int(input('Digite o valor:'))
    vetor2.append(valor)


uniao = set(vetor1).union(vetor2)


print(uniao)

x = []
y = []
soma = 0
uniao = 0
multi = 0
dife = 0
while len(x) < 5:
    valor = int(input('Digite o valor:'))
    x.append(valor)

while len(y) < 5:
    valor = int(input('Digite o valor:'))
    y.append(valor)

for indice in range(0,5):
    soma += x[indice] + y[indice]
    multi += x[indice] * y[indice]
    dife += x[indice] - y[indice]

uniao = set(x).union(y)
ambos = set(x).intersection(y)

print(soma)
print(multi)
print(dife)
print(uniao)
print(ambos)

exercicio 33
vetor = []
i=0

while len(vetor) < 15:
    x = int(input("digite um valor"))
    vetor.append(x)


while 0 in vetor:
    if vetor[i] == 0:
        vetor.pop(i)

    i+=1

print(vetor)


exercicio 34
vetor = []


while len(vetor) < 10:
    x = int(input("digite um valor"))
    if x in vetor:
        print('Digite um novo valor!')
        continue
    else:
        vetor.append(x)
print(vetor)

a = []
b = []
mais = []
op=False
soamtoria = 0

while op != True:
    valora = int(input('digite um valor < 10000 A:\n'))
    valorb = int(input('digite um valor < 10000 B:\n'))
    if valora < 10000 and valorb < 10000:
        a = list(str(valora))
        b = list(str(valorb))
        if len(a) > len(b):
            while len(b) != len(a):
                dado= 0
                b.append(dado)
        if len(b) > len(a):
            while len(a) != len(b):
                dado= 0
                a.append(dado)

        if len(a)==len(b):
            for i in range(0,len(a)):
                s= i
                soma = int(a[i]) + int(b[i])
                if mais == [ ]:
                    if soma > 10:
                        soma = soma - 10
                        colocar = 1
                        mais.append(colocar)
                    soamtoria += soma
                elif mais[s-1] == 1:
                    soma += 1

                s=s+1

            print(soamtoria)
    else:
        print('valor invalido')
        continue




vetor = []
while len(vetor) < 10:
    x = int(input('digite um valor'))
    vetor.append(x)

vetor.sort()

print(vetor)


exercicio 37
vetor = []
ordem = []

while len(vetor) < 11:
    x = int(input('digite um valor'))
    vetor.append(x)

vetor.sort()

for i in range(11-1,5,-1):
    ordem.append(vetor[i])

print(vetor[0:6]+ordem)


exercicio 38

vetor = []

while len(vetor) < 10:
    x = int(input('digite o valor'))
    vetor.append(x)
    vetor.sort()

print(vetor)



PARTE 2 MATRIZES

$exercicio 1

vetor= [
        [], [], [], [],
       ]

dez= []
for i in range(0,4):
    while len(vetor[i]) < 4 :
        x = int(input('digite um valor:'))
        if x > 10:
            dez.append(x)
        vetor[i].append(x)
        print(vetor)


print(f'a quantidade de numeros maiores que 10 nessa matriz é {len(dez)}')
print()
for i in range(0,4):
    print(vetor[i])


exercicio 3

vetor= [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
       ]


for linha in range(0,4):
    for coluna in range(0,4):
        dado = linha * coluna
        vetor[linha][coluna]=dado

print(vetor)


exercicio 4


vetor= [
        [], [], [], [],
       ]

maior = 0
for i in range(0,4):
    while len(vetor[i]) < 4 :
        x = int(input('digite um valor:'))
        if x > maior:
            maior = x
            lin = i
            col = len(vetor[i])
        vetor[i].append(x)
        print(vetor)




for i in range(0,4):
    print(vetor[i])


print(f'o maior numero é {maior} e a localização linha: {lin} coluna:{col}')


exercicio 5

vetor= [
        [], [], [], [],[],
       ]

maior = 0
for i in range(0,4+1):
    while len(vetor[i]) < 4+1 :
        x = int(input('digite um valor:'))
        if x > maior:
            maior = x
            lin = i
            col = len(vetor[i])
        vetor[i].append(x)
        print(vetor)

tem = False
dado = int(input('DIgite o valor a ser pesqusiado:'))
for i in range(0,4+1):
    if dado in vetor[i]:
        print( vetor[i].index(dado))
        tem = True
        linha = i
        col = vetor[i].index(dado)
if tem ==True:
    print(f'A matriz contem o valor {dado}. ele esta localizado na linha  {linha+1} colua {col+1}')
for i in range(0,4+1):
    print(vetor[i])

"""

