class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Para agrupar os anagramas, precisaremos primeiro identificar quais palavras são anagramas uma das outras.
        groups = {} # {"aet": ["eat"]}

        for word in strs:
            sorted_word = "".join(sorted(word)) # ordeno a palavra
            if not sorted_word in groups: # se a palavra ordenada não existir como chave dentro do grupo
                groups[sorted_word] = [] # inicia o par chave/valor onde a chave é a palavra ordenada e o valor é a lista vazia
            groups[sorted_word].append(word) # junta a palavra na chave correspondente

        return list(groups.values()) # retorna a lista apenas dos valores do grupo, que são as palavras originais não ordenadas

            

