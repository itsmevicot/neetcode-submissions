class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # vamos armazenar todos os números vistos
        
        for i, num in enumerate(nums): # para cada número e seu índice na lista
            complement = target - num # calculamos o complemento, isso é, o número que somado ao numero iterado atinge o alvo

            if complement in seen: # se já vimos o complemento e só existe 1 resposta, então podemos assumir que já achamos
                return sorted([seen.get(complement), i])  # então retornamos a lista ordenada

            seen[num] = i  # caso contrário, só adicionamos o número ao dicionário de números vistos       
