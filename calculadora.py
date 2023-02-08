def print_boasvindas():
    print("+-*/+-*/+-*/+-*/+-*/+-*/+-*/+-*/+-*/+-*/")
    print("+-*/+-*/+-Calduladora Python+-*/+-*/+-*/")
    print("+-*/+-*/+-*/+-*/+-*/+-*/+-*/+-*/+-*/+-*/")
    print("\n")

def print_opcoes():
    print("As operações que dispomos atualmente são: \n")
    print("Soma - digite soma ou somar \n")
    print("Subtração - digite subtração ou subtrair \n")
    print("Divisão - digite divisão ou dividir \n")
    print("Multiplicação - digite multiplicação ou multiplicar \n")
    print("Tabuada Individual - digite tabuada e em seguida o numero que deseja \n")
    print("Tabuada Geral - digite tabuada e depois todos \n")

def end():
    print("Obrigado por usar nossa calculadora!")

def soma(n1, n2):
    s = n1 + n2
    print("O resultado da soma é {}".format(s))
    resposta = input("Deseja fazer outra operação? ")
    if(resposta == "sim"):
        return opcoes()
    else:
        return end()

def subtracao(n1, n2):
    sub = n1 - n2
    print("O resultado da subtração é {}".format(sub)) 
    resposta = input("Deseja fazer outra operação? ")
    if(resposta == "sim"):
        return opcoes()
    else:
        return end()

def multiplicacao(n1, n2):
    m = n1*n2
    print("O resultado da multiplicação é {}".format(m))
    resposta = input("Deseja fazer outra operação? ")
    if(resposta == "sim"):
        return opcoes()
    else:
        return end()

def divisao(n1, n2):
    div = n1/n2
    print("O resultado da divisão é {}".format(div))
    resposta = input("Deseja fazer outra operação? ")
    if(resposta == "sim"):
        return opcoes()
    else:
        return end()

def tabuada_geral():
    n1 = [numero for numero in range(1,11)]
    n2 = [numero for numero in range(1,11)]

    for numero in n1:
        print("\nTabuada de {}:".format(numero))
        for numero2 in n2:
            print("{} x {} = {}".format(numero, numero2, numero*numero2))
    resposta = input("Deseja fazer outra operação? ")
    if(resposta == "sim"):
        return opcoes()
    else:
        return end()

def tabuada_uni(n):
    n1 = [numero for numero in range(1,11)]
    n2 = [numero*n for numero in n1]
    print("Tabuada de {}".format(n))
    for num in range(10):
        print("{} x {} = {}".format(n1[num],n,n2[num]))
    resposta = input("Deseja fazer outra operação? ")
    if(resposta == "sim"):
        return opcoes()
    else:
        return end()
    
def opcoes():
    escolha = input("Qual operação deseja fazer? ")
    if(escolha == "somar" or escolha == "soma"):
        n1 = float(input("Digite o primeiro valor a ser somado: "))
        n2 = float(input("Digite o outro valor a ser somado: "))
        soma(n1,n2)
    elif(escolha == "subtração" or escolha == "subtrair"):
        n1 = float(input("Digite o primeiro valor a ser subtraido: "))
        n2 = float(input("Digite o outro valor a ser subtraido: "))
        subtracao(n1,n2)
    elif(escolha == "multiplicação" or escolha == "multiplicar"):    
        n1 = float(input("Digite o primeiro valor a ser multiplicado: "))
        n2 = float(input("Digite o outro valor a ser multiplicado: "))
        multiplicacao(n1,n2)
    elif(escolha == "divisão" or escolha == "dividir"):
        n1 = float(input("Digite o dividendo: "))
        n2 = float(input("Digite o divisor: "))
        divisao(n1,n2)
    elif(escolha == "tabuada"):
        numero = input("Selecione o número que deseja saber a tabuada: ")
        if(numero == "todos"):
            tabuada_geral()
        else:
            numero = int(numero)
            tabuada_uni(numero)
    else:
        print("Selecione uma opção valida!")
        retorno()

def geral():
    print_boasvindas()
    print_opcoes()
    opcoes()

def retorno():
    print("\n")
    opcoes()

if (__name__ == "__main__"):
    geral()