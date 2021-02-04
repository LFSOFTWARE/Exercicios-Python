"""
luiz fernando  01/02/2021
        Funções



Exercicio 1

def dobro(numero):
    return numero*2

print(dobro(2))

Exercicio 2
    meses = {1:'janeiro',2:'fevereiro',3:'março',4:'abril',5:'maio',6:'junho',7:'julho',8:'agosto',9:"setembro",10:'outubro',11:'novembro',12:'dezembro'}
def imprimir_data(dia,mes,ano):
    print(f'Dia {dia} de {meses[mes]} de {ano}')


imprimir_data(10,12,2002)

Exercicio 3

def verifica_sinal(numero):
    if numero > 0:
        return 1
    elif numero < 0:
        return -1
    return 0


print(verifica_sinal(-10))

Exercicio 4

def quadrado_perfeito(numero):

    for x in range (0,numero+1):
        if x * x == numero:
            return 'E perfieto'
    return 'nao é perfeito'


print(quadrado_perfeito(25))

Exercico 5
import  math


def volume_esfera(raio=1):
    v = (1/3)*math.pi*(raio**3)
    return f'{v:.3f}'

print(volume_esfera(1))

Exercicio 6

def conversor(hora,minuto,segundo):
    a = hora *3600
    b = minuto*60
    return a+b+segundo

print(f' a conversao para segundos é {conversor(1,1,1)}')

Exercicio 7

def Fahrenheit(graus):
    f = graus * (9.0/5.0)+32.0
    return f


print(Fahrenheit(30))

Exercicio 8
import math

def pitagoras(a,b):
    hip = math.sqrt((a**2+b**2))
    return hip

print(pitagoras(10,50))

Exercicio 9

def volume_cilindro(altura,raio):
    pi = 3.141592
    volume = pi*(raio**2)*altura
    return volume


print(volume_cilindro(10,50))

Exercicio 10


def maior_num(numero1,numero2):
    if numero1 > numero2:
        return f'o numero {numero1} é maior'
    elif numero1 < numero2:
        return f'o numero {numero2} é maior'
    return 'os dois sao iguais :)'


print(maior_num(10,5))

Exercicio 11

def media(nota1,nota2,nota3,opcao='A'):
    if opcao == 'a' or opcao =='A':
        media = (nota1 + nota2 + nota3)/3
        return media
    elif opcao =='p' or opcao =='P':
        media = ((nota1*5) + (nota2*3) + (nota3*2)) /10
        return media

print(media(0,10,10,'p'))

Exercicio 12




def soma_algorismos(numero):
    soma = 0
    if numero > 0:
        numero = str(numero)
        fragmentado = list(numero)
        for x in fragmentado:
            x = int(x)
            soma += x
        return soma
    return 'Numero invalido :('

print(soma_algorismos(1101))

Exercicio 13

def calculadora(numero1,numero2,operação='+'):

    if operação == '+':
       return numero1 + numero2
    elif operação == '-':
        return numero1 - numero2
    elif operação == '/':
         return numero1 / numero2
    elif operação == '*':
        return numero1 * numero2
    return 'ops, operação invalida :('


print(calculadora(1,1,'~l'))


Exercicio 14


def gasto(km,litros):
    gasto = km/litros

    if gasto < 8:
        return  f'o carro faz {gasto}, Venda o Carro!!'
    elif gasto >= 8 and gasto <=14:
        return f'o carro faz {gasto}, ele é Ecônomico!!!'
    elif gasto > 12:
        return f'o carro faz {gasto}KM por litro, ele é Super-Ecônomico!!!'



print(gasto(100,5))

Exercicio 15 ********************refatorar

a = input('digite tres valores')


lado1,lado2,lado3 = a.split()
try:
    lado1= int(lado1)

except:
    lado1 =  float(lado1)
try:
    lado2 = int(lado2)

except:
    lado2 = float(lado2)
try:
    lado3 = int(lado3)

except:
    lado3 = float(lado3)

def confere_se_e_triangulo(lado1,lado2,lado3):
    if lado1 < lado2 + lado3:
        print(type(lado1))
        if lado2 < lado1 + lado3:
            if lado3 < lado2 + lado1:
                return 'forma triangulo'
    return 'nao forma um triangulo'

print(confere_se_e_triangulo(lado1,lado2,lado3))

Exercicio 16

def desenha(tamanho):
    return '='*tamanho


print(desenha(500))

Exercicio 17

def soma_intervado(num1,num2):
    soma = 0
    for x in range(num1,num2+1):
        soma += x

    return soma


print(soma_intervado(0,5))

Exercicio 18


def pow(base,expoente):
    return base**expoente

print(pow(10,5))

Exercicio 20

def fatorial(numero):

    soma =0
    for x in range(numero,1-1,-1):
        if x == numero:
           soma = x * (x - 1)
        elif x == 1 :
            break
        else:
            computa = soma * (x-1)
            soma = computa


    return soma

print(fatorial(50))


exercicio 22

def desenha(n):
    for x in range(1,n+1):
        print('!'*x)

desenha(5)


Exercicio 28
def triangulo_lateral(n):
    comprimento = 2*n-1
    i = 1
    j=n
    up =True
    down = False
    for x in range(0,comprimento):

        if up == True:
            print('*'*i)
        elif down == True:
            print('*' * j)

        if i <= n:
            i += 1

        if i > n:
            up = False
            down =True

        if down == True:
            j-=1
triangulo_lateral(80)

Exercicio 25

def triangulo(n):
    i=1
    for x in range(1,n+1):
        base = 2*n-1

        print('*'*i)



        i+=2
triangulo(6)

exercico 26

def somatorio(n):
    soma= 0
    for x in range(1,n+1):
        soma +=x

    return soma

print(somatorio(5))


Exercicio 32
def simplifica(numerador,demonimador):
    for x in range (1,demonimador+numerador):
        if demonimador % x == 0 and numerador % x ==0:
            demonidaor1 = demonimador/x
            numerador1 = numerador/x

    print( f'a função simplificada é numerador: ')
    print(f'       {numerador}                       {numerador1}')
    print('    ----------              -----------')
    print(f'       {demonimador}                       {demonidaor1}')

simplifica(36,60 )

Exercicio 33


def fatorial(numero):
    soma1= 0
    soma =0
    soma2 =0
    for x in range(numero,1-1,-1):
        if x == numero:
           soma = x * (x - 1)
        elif x == 1 :
            break
        else:
            computa = soma * (x-1)
            soma = computa

    soma1 = str(soma)
    indice = list(soma1)

    for x in indice:
        soma2 += int(x)

    return f'o fatorial é {soma} e a soma dos algorismos é {soma2}'


print(fatorial(6))

Exercicio 34

def fatorial(numero):

    soma =0
    for x in range(numero,1-1,-2):
        if x == numero:
           soma = x * (x - 2)
        elif x == 1 :
            break
        else:
            computa = soma * (x-2)
            soma = computa


    return soma

print(fatorial(5))

Exercicio 39

def troca(A,B):
    Y = B
    X = A

    return f'{Y} {X}'

print(troca(100,50))


Exercio 40

def restorna_pares(*args):
    pares = []

    for x in lista:
        if x % 2 == 0:
            pares.append(x)

    return f'{pares} e o seu tamanho é {len(pares)}'



lista =[]
while True:
    dado = int(input('Digite um vetor:'))
    if dado == -1:
        break
    else:

        lista.append(dado)


print(restorna_pares(*lista))


Exercicio 41



def restorna_pares(*args):
    return f'o maior élemento da lista é {max(args)}'


lista =[]
while True:
    dado = int(input('Digite um vetor:'))
    if dado == -1:
        break
    else:

        lista.append(dado)


print(restorna_pares(*lista))
Exercicio 42
import random

def restorna_pares(*args):
    media = sum(args)/len(args)

    return media





lista =[]
while True:
    dado = int(input('Digite um vetor:'))
    if dado == -1:
        break
    else:

        lista.append(dado)


print(restorna_pares(*lista))


Exerciio 43

import random

def restorna_pares(*args):
    cheio = []

    while len(cheio) < len(args):
        dado = random.randrange(1,1000000000)
        cheio.append(dado)

    return cheio
lista =[]
while True:
    dado = int(input('Digite um vetor:'))
    if dado == -1:
        break
    else:

        lista.append(dado)


print(restorna_pares(*lista))
Exercicio 48
import random

def restorna_pares(*args):
    pares = []
    impares = []

    for x in args:
        if  x % 2 ==0:
            pares.append(x)
        if  x % 2 ==1:
            impares.append(x)


    return f'A:{pares} B:{impares}'


lista =[]
while len(lista) < 30:
    dado = int(input('Digite um vetor:'))
    if dado == -1:
        break
    else:

        lista.append(dado)


print(restorna_pares(*lista))
Excercicio 46

import random

def prita_vetor(*args):
    return args

def inversao(*args):
    return args[::-1]

def media(*args):
    return sum(args)/len(args)



lista =[]
while True:
    dado = int(input('Digite um vetor:'))
    if dado == -1:
        break
    else:

        lista.append(dado)


print(prita_vetor(*lista))
print(inversao(*lista))
print(media(*lista))

Exerciico 47



vetor= [
        [], [], [], [],
       ]

maior = []
for i in range(0,4):
    while len(vetor[i]) < 4 :
        x = int(input('digite um valor:'))
        vetor[i].append(x)
        print(vetor)

        if x > 10:
            maior.append(x)


print(f'os numeros maiores que 10 é :{maior}')

Exercicio 59


def uniao(*args):

    A = set(args[0])
    B = set(args[1])

    uniao = A.union(B)

    return uniao


a = [1,2,3]
b = [1.2,3,4]



print(uniao(a, b))

"""





