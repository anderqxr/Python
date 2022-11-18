import random

#   interação com o usuario...
name = input("Qual seu nome? ")
print("Boa sorte! ", name)

#   bloco com palavras 
palavras = ['computador', 'ciencia', 'python', 'matematica', 'jogador',
            'condicao', 'reverso', 'agua', 'geeks', 'futebol', 'volei']

#   selecionar uma palavra aletoria do bloco
word = random.choice(palavras)

print("Adivinhe a palavra!")

#   numero de palpites 
palpites = ''
rodadas = 5

#   while ate  não ter mais palpites
while rodadas > 0:
    failed = 0

#   verificar se contem o caracter na palavra 
    for char in word:
        if char in palpites: #  condição para colocar o caracter casa contenha 
            print(char)
        else:               #   caso não tenha diminui no numero de tentativas 
            print("__")
            failed -=1

    if failed == 0:         #   caso acerte a palavra imprime a mensagem de parabéns, e para o laço while
        print( "ganhou parabens" )
        print("A palavra é: ", word)
        break

    procurar =  input("Informe um caracter: ")
    palpites +=procurar

    if procurar not in word: #  caso não acerte imprime "você perdeu" e para o while com as tentativas chegando a zero 0
        rodadas -=1
        print("Errou !!!") 
        print("Você tem", + rodadas, " mais palpites")

        if rodadas == 0:
            print("voce perdeu")

