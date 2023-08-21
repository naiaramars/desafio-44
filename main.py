# 1) Faça um programa que mostre a mensagem "hello world" cinco vezes. 

for x in range(5):
    print("Hello World")

# 2) Faça um programa que mostre todos os números de 1 até 150. 

import time

for x in range(1, 151):
    print(x)

    time.sleep(0.5)

# 3) Faça um programa que mostre uma contagem regressiva que inicia em 10 e termina em 0. 

import time

for x in range(10,0,-1):
    print(x)

    time.sleep(1)

# 4) Faça um programa que mostre todos os números pares de 1 até 200. 

for x in range(0,202,2):
    print(x)

# 5) Faça um programa que gere as tabuadas do 1 até o 10.

for num in range(1, 11):
    print(f"Tabuada do {num}:")
    for x in range(1, 11):
        resultado = num * x
        print(f"{num} x {x} = {resultado}")

# 6) Faça um programa em que o usuário digita um número inteiro e o programa exibe todos os números ímpares do 1 até o valor inserido.

def main():
    try:
        num = int(input("Digite um número inteiro que deseja obter os ímpares: "))
        print("Números ímpares de 1 até", num, ":")
        for x in range(1, num + 1):
            if x % 2 != 0:
                print(x, end=" ")
        print() 
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir um número inteiro.")

if __name__ == "__main__":
    main()