class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized = "".join(c.lower() for c in s if c.isalnum()) # normaliza jogando tudo para minusculo e verificando se a str é alfanumérica
        return normalized == normalized[::-1] # compara a string com ela invertida (da pra usar reversed também)