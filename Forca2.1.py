# Jesus é meu Senhor e Salvador. Glória e Honra ao Filho de Deus!!!
#
# Jogo da forca para exercício de aprendizado de Python
# Autor: Hamilton Paz
# Versão 2.0 a partir da versão de demonstração do professor
# Versão 2.1 - O jogo não funciona em modo shell do Python por mostrar
# todas as listas em coluna ao invés de ser em linha. Para corrigir
# esse defeito, é necessário reescrever parte do código.
# Total permissão para efetuar qualquer alteração e/ou distribuição

# Passo 01: Importações das palavras e desenhos
import random
from palavras import categoria_palavra
from desenhos import categoria_desenho


# Passo 02: Criação dos módulos
# 2.1 - Desenhos na tela
def desenha(catego, chance):
    print(catego[chance])
    return

# 2.2 - Escrever letras para chute, acertadas e erradas
def mostra_letras():
    print('═' * 71)
    print('Letras restantes:', letras)
    print('═' * 71)
    print('Letras acertadas:', let_certas)
    print('Letras erradas..:', let_erradas)
    return

# Passo 03: Definição do laço principal
continuar = 'S'
while continuar != 'N':
    nume = 1
    categoria = {}
    for cat in categoria_palavra:
        print(nume,'\b:', cat)
        categoria.update({nume: cat})
        nume += 1
    num_cat = int(input('Por favor, selecione o número da categoria desejada: '))
    palavra = random.choice(categoria_palavra.get(categoria[num_cat])).upper()
    palavra2 = ''
    letras      = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z -'
    let_erradas = '. . . . . . . . . . . . . . . . . . . . . . . . . . .'
    let_certas  = '. . . . . . . . . . . . . . . . . . . . . . . . . . .'
    chances = 6
    resolvido = 'N'
    while chances > 0 and resolvido != 'S':
        if chances <= 5: desenha(categoria_desenho.get(categoria[num_cat]), chances)
        mostra_letras()
        print('─' * 71)
        print('\n')
        palavra2 = ''
        for letr in palavra:
            if letr in let_certas:
                palavra2 += letr + ' '
            else:
                palavra2 += '_ '
        print(palavra2)
        palpite = input('\nInforme uma letra: ').upper()
        if palpite in let_certas or palpite in let_erradas:
            print('Você já tentou a letra', palpite, 'antes. Por favor, escolha outra:')
            continue
        elif palpite not in palavra:
            print('Que pena! Tente novamente.')
            let_err2 = ''
            conta = 0
            pos = letras.find(palpite)
            letras = letras.replace(palpite, '.')
            for let in let_erradas:
                if conta != pos:
                    let_err2 += let_erradas[conta]
                else:
                    let_err2 += palpite
                conta += 1
            let_erradas = let_err2
            chances -= 1
        elif palpite in palavra:
            print('É isso aí!')
            let_cert2 = ''
            conta = 0
            pos = letras.find(palpite)
            letras = letras.replace(palpite, '.')
            for let in let_certas:
                if conta != pos:
                    let_cert2 += let_certas[conta]
                else:
                    let_cert2 += palpite
                conta += 1
            let_certas = let_cert2
        correto = 0
        for l in palavra:
            if l in let_certas: correto += 1
        if len(palavra) == correto:
            mostra_letras()
            print('Você ACERTOU!!! A palavra é', palavra)
            resolvido = 'S'
    if chances == 0:
        desenha(categoria_desenho.get(categoria[num_cat]), chances)
        print('Que pena! Você perdeu. A palavra era ', palavra)
    continuar = input('\nDeseja continuar? ').upper()

