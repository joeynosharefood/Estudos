import random
c = 0#contador de vitorias
while True:
    x = random.randrange(0, 11)#numeros colocados pelo computador
    print(x)
    y = random.randrange(1, 3)#escolha do computador (1 para impar/2 para par)
    print(y)
    z = int(input('Insira um valor : '))#numeros colocados pelo usuario
    if z > 10:
        print(f'Você tem {z} dedos ? ')
        break
    else:
        r = x + z
        if y%2 == 0:#computador escolhendo par
            if r%2 == 0:#computador ganhando
                print(r)#comprovação da vitoria, demonstrando a soma 
                print(c)#print da contagem de vitorias
                break
            else:
                c += 1
        else:#computador escolhendo impar
            if r%2 == 0:#computador perdendo
                c+= 1
            else:
                print(r)#comprovação da vitoria, desmontrando a soma
                print(c)
                break

            

                