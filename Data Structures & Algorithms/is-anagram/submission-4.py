class Solution:
    def isAnagram(self, s: str, t: str) -> bool: # versão 1
        # A ideia é iterar todas as letras de S e T e comparar 
        # se elas tem o mesmo tamanho,
        # se as letras são as mesmas e
        # se a quantidade de letras repetidas são as mesmas.
        # Então, se eu armazenar a quantidade de letras de S e T
        # eu consigo saber se são anagramas.

        if len(s) != len(t): # tamanhos diferentes
            return False

        letters = {}

        for letter in s: # para cada letra da string "s"
            if letter not in letters: # se a letra ainda não está no dicionário
                letters[letter] = 1 # adiciona e inicia o contador
            else: # caso já esteja
                letters[letter] += 1 # adiciona 1 ao contador
        # ao final do loop, já temos as letras e a quantidade

        for letter in t: # para cada letra de t
            if letter not in letters or letters[letter] == 0: # se a letra não existir ou tiver mais do que a primeira palavra:
                return False # retorna falso
            letters[letter] -= 1 # tira 1 das letras
        return True # se passou por todo o loop, todas as letras estão zeradas, então é anagrama
        