class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        temp = ''
        ptr = 0

        while(ptr < min(len(word1), len(word2))):
            temp += word1[ptr] + word2[ptr]
            ptr += 1
        
        return temp+word1[ptr:]+word2[ptr:]
