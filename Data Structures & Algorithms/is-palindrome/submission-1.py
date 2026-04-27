class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 # inicia um indice na esquerda (inicio da string)
        right = len(s) - 1 # inicia um indice na direita (fim da string); subtraimos 1 pois índices começam em 0, então "abcd" tem tamanho 4, mas o indice de "d" é 3

        while left < right: # enquanto o indice da esquerda for menor que o da direita, isso é, enquanto eles não passarem um do outro
            if not s[left].isalnum(): # se os caracteres não são alfanuméricos (ou seja, caracteres inválidos como espaços em branco e pontuações)
                left += 1 # aumente o indice da esquerda
                continue # passa para a próxima iteração do loop

            if not s[right].isalnum(): # mesma coisa para a direita: verifica se é alfanumérico
                right -= 1 # > DIMINUI < o indice da direita (no exemplo "abcd", ele estaria olhando para o "c" agora)
                continue # passa para a próxima iteração do loop
        
            if s[left].lower() != s[right].lower(): # se os 2 caracteres são válidos, comparamos eles (minúsculas); se forem diferentes, não é palíndromo
                return False
            left += 1 # aumenta o indice da esquerda para olhar o proximo char
            right -= 1 # diminui o indice da direita para olhar o proximo char
        return True