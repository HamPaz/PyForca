# Jogo da forca para exercício de aprendizado de Python
# Autor: Hamilton Paz
# Versão 2.0 a partir da versão de demonstração do professor
# Total permissão para efetuar qualquer alteração e/ou distribuição

# Passo 01: Importações das palavras e desenhos
import random
from palavras import categoria_palavra
from desenhos import categoria_desenho

# Passo 02: Criação das listas e variáveis para o jogo
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '-'
]
continuar   = 'S'

# Passo 03: Criação dos módulos
# 3.1 - Desenhos na tela
def desenha(catego, chance):
    print(catego[chance])
    return

def mostra_letras():
    print('═' * 71)
    print('Letras restantes:')
    for let in letras:
        if let not in let_certas and let not in let_erradas:
            print('\b', let)
        else:
            print('\b .')
    print('═' * 71)
    print('Letras acertadas:')
    for let in letras:
        if let in let_certas:
            print('\b', let)
        else:
            print('\b .')
    print('Letras erradas..:')
    for let in letras:
        if let in let_erradas:
            print('\b', let)
        else:
            print('\b .')
    return

# Passo 04: Definição do laço principal
while continuar != 'N':
    nume = 1
    categoria = {}
    for cat in categoria_palavra:
        print(nume,'\b:', cat)
        categoria.update({nume: cat})
        nume += 1
    num_cat = int(input('Por favor, selecione o número da categoria desejada: '))
    palavra = random.choice(categoria_palavra.get(categoria[num_cat])).upper()
    let_erradas = []
    let_certas = []
    chances = 6
    resolvido = 'N'
    while chances > 0 and resolvido != 'S':
        if chances <= 5: desenha(categoria_desenho.get(categoria[num_cat]), chances)
        mostra_letras()
        print('─' * 71)
        print('\n')
        for letr in palavra:
            if letr in let_certas:
                print('\b', letr)
            else:
                print('\b _')
        palpite = input('\nInforme uma letra: ').upper()
        if palpite in let_certas or palpite in let_erradas:
            print('Você já tentou a letra', palpite, 'antes. Por favor, escolha outra:')
            continue
        elif palpite not in palavra:
            print('Que pena! Tente novamente.')
            let_erradas.append(palpite)
            chances -= 1
        elif palpite in palavra:
            print('É isso aí!')
            let_certas.append(palpite)
        correto = 0
        for l in palavra:
            if l in let_certas: correto += 1
        if len(palavra) == correto:
            mostra_letras()
            print('Você ACERTOU!!! A palavra é', palavra)
            resolvido = 'S'
    if chances == 0:
        desenha(categoria_desenho.get(categoria[num_cat],5))
        print('Que pena! Você perdeu.')
    continuar = input('\nDeseja continuar? ').upper()

    






