class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = "" # inicializa a string codificada
        for x in strs:
            encoded += f"{len(x)}#{x}"  # toda string terá o formato '5#abcde' onde 5 é o len depois do '#'; daí vamos concatenando todas as strings
        return encoded

    def decode(self, s: str) -> List[str]: # supor a string ("3#abc4#12345#ab9876#######"")
        decoded = []
        i = 0
        while i < len(s): # enquanto o índice for menor do que o tamanho de s 
            j = s.find('#', i) # e.g: j = 1 na primeira iteração do nosso exemplo; não posso assumir que é tudo pra trás e nem o primeiro atrás por causa de números muito grandes como 50 ou 894352795487432
            size = int(s[i:j]) # o número convertido em tamanho vai do índice 0 até o índice j, mas como o intervalo é aberto, ele fatia até antes do '#'. (e.g: 84123#...... j estaria na posição 5, mas [i:j] vai de 0 a 5 aberto, então de fato é 0 a 4
            word = s[j+1:j+1+size] # a palavra começa imediatamente após o '#' (por isso j+1) e termina no índice representado por onde ele começa (j+1) mais seu tamanho (size). Portanto, j+1+size
            decoded.append(word) # colocamso a palavra no dicionário

            i = j + 1 + size # preciamos que o índice 0 da próxima iteração seja exatamente na str que representa o tamanho da palavra; pra isso, precisamos pular o '#'(j+1) e pular a palavra inteira (ou seja, o size) assim como feito acima => (j+1+size)
                     
        return decoded
