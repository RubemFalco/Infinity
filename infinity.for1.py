numero = int(input('Digite um número para que seja impressa a tabuada: '))
print(f'tabuada do {numero}:')
for item in range(1,11,1):
    print(f'{numero} x {item} = {numero * item}')
