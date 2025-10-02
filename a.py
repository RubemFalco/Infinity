numero = 8


while True:  
    tentativa = ""
    tentativas_restantes = 3
    
#EDITA EDITA
    while tentativa != numero and tentativas_restantes > 0:
        tentativa = int(input("digite um numero aleatorio: "))
        
        if tentativa != numero:
            tentativas_restantes -= 1
            print(f"numero errado! Você ainda tem {tentativas_restantes} tentativa(s).")

    if tentativa == numero:
        print("voce acertou!")
    else:
        print("Número máximo de tentativas atingidas")

    resposta = input("vamo novamente? (s/n): ")
    if resposta.lower() != "s":
        print("Encerrando o programa...")

        break
