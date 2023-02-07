def print_boasvindas():
    print("+-*/+-*/+-*/+-*/+-*/+-*/+-*/+-*/+-*/+-*/")
    print("+-*/+-*/+-Calduladora Python+-*/+-*/+-*/")
    print("+-*/+-*/+-*/+-*/+-*/+-*/+-*/+-*/+-*/+-*/")

def soma(n1, n2):
    s = n1 + n2
    print("O resultado da soma é {}".format(s))
    resposta = input("Deseja fazer outra operação? ")
    if(resposta == "sim"):
        return opcoes()
    else:
        return end()

def subtracao(n1, n2):
    return n1 - n2 
    resposta = input("Deseja fazer outra operação? ")
    if(resposta == "sim"):
        return opcoes()
    else:
        return end()

def multiplicacao(n1, n2):
    return n1*n2
    resposta = input("Deseja fazer outra operação? ")
    if(resposta == "sim"):
        return opcoes()
    else:
        return end()

def divisao(n1, n2):
    return n1/n2
    resposta = input("Deseja fazer outra operação? ")
    if(resposta == "sim"):
        return opcoes()
    else:
        return end()

def tabuada_geral():
    n = range(1,11)
    n1 = range(1,11)
    #tabuada = [n * n1 for ]
    resposta = input("Deseja fazer outra operação? ")
    if(resposta == "sim"):
        return opcoes()
    else:
        return end()

def tabuada_uni(n):
    n1 = [numero for numero in range(1,11)]
    n2 = [numero*n for numero in n1]
    for num in range(10):
        print("A multiplicação de {} x {} = {}".format(n1[num],n,n2[num]))
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
    elif(escolha == "tabuada"):
        numero = int(input("Selecione o número que deseja saber a tabuada: "))
        tabuada_uni(numero)

def end():
    print("Obrigado por usar nossa calculadora!")

def geral():
    print_boasvindas()
    opcoes()

if (__name__ == "__main__"):
    geral()