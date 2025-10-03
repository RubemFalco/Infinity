# idade=int(input('Insira aqui a sua idade: '))
# if idade<12:
#     print('Criança')
# elif idade<18:
#     print('Adolecente')
# else:
#     print('Adulto')

# listanumeros = []
# for i in range(0,3):
#     numero = int(input(f'INSIRA AQUI O {i+1}º NÚMERO: '))
#     listanumeros.append(numero)
# print(max(listanumeros))
# print(min(listanumeros))

# par = []
# impar = []
# for i in range(0,10,1):
#     numero = int(input(f'Digite aqui o {i+1} número: '))
#     if numero%2==0:
#         par.append(numero)
#     else:
#         impar.append(numero)
# print(par)
# print(impar)

# def pareimpar():
#     par = []
#     impar=[]
#     for i in range(10):
#         numero=int(input(f'Digite o {i+1}º ítem: '))
#         if numero%2==0:
#             par.append(numero)
#         else:
#             impar.append(numero)
#     print(par)
#     print(impar)
# pareimpar()


# idadestotal = []
# def idades():
#     for i in range(5):
#         idade= int(input(f'Digite aqui a idade do {i+1}º membro: '))
#         idadestotal.append(idade)
# def mediaidades():
#     media = sum(idadestotal)/len(idadestotal)
#     print(media)
#     if media<25:
#         print('media menor que 25!')
#     elif media==26:
#         print('A média é 26!')
#     elif media<60:
#         print('A média é maior que 26!')
#     elif media==60:
#         print('A média é 60!')
#     else:
#         print('A média é maior que 60!')
# idades()
# mediaidades()

numeros = []
def listar_numeros():
    for i in range(5):
        numero = int(input(f'Digite o {i+1}º número: '))
        numeros.append(numero)
def trabalhar_numeros():
    print(f'o maior número é {max(numeros)}')
    print(f'o menor número é {min(numeros)}')
    print(f'a soma dos números é {sum(numeros)/len(numeros)}')
listar_numeros()
trabalhar_numeros()


