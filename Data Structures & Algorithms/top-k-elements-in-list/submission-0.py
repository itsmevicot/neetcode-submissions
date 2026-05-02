import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []
        result = []

        for x in nums: # construir o dicionário de frequências
            if x not in freq:
                freq[x] = 1
            else:
                freq[x] += 1

        for key, value in freq.items(): # para cada par de chave, valor
            heapq.heappush(heap, (value, key)) # jogamos no heap como uma tupla de valores invertidos, ou seja, primeiro a frequência e depois o valor. Ex: (3, 1) significa que o número 1 apareceu 3 vezes
            if len(heap) > k: # se o tamanho do heap for maior do que a frequência "k"
                heapq.heappop(heap) # a gente tira o elemento raiz, que é o número que aparece menos vezes

        # ao final do loop, vamos ter percorrido todo o dicionário de valores e frequências de aparição,
        # e como todo heappush já faz um heapify(), a menor frequência sempre estará no topo, então todo 
        # heappop remove da raiz a tupla de menor frequência, restando no heap apenas o top K frequent numbers 
        # em formato de tupla.

        for freq, num in heap: # percorrendo as tuplas com duas variaveis, uma pra cada valor da tupla | poderíamos fazer for x in heap e x seria a tupla, bastariamos acessar o indice do número, que seria x[1]
            result.append(num)

        return result        
