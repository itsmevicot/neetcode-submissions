class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: # [1,2,3,1]
        seen = set()
        
        for num in nums: # para cada numero na lista
            if num in seen: # se o número já está no set
                return True # returna true
            seen.add(num) # adicione o numero ao set
        return False # se não retorna falso ao percorrer toda a lista

