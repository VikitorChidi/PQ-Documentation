from typing import List


def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {} #hashmap/array
        for index, val in enumerate(order):
            orderMap[val] = index
        
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]): return False
                if words[i][j] != words[i + 1][j]:
                    if orderMap[words[i][j]] > orderMap[words[i + 1][j]]: return False
                    break
        return True

#     def isAlienSorted(self, words: List[str], order: str) -> bool:
#         # first differing char
#         # if word A is prefix of word B, word B must be after word A
        
#         orderInd = {c : i for i, c in enumerate(order)}
        
#         for i in range(len(words) - 1):
#             w1, w2 = words[i], words[i + 1]
            
#             for j in range(len(w1)):
#                 if j == len(w2):
#                     return False
                
#                 if w1[j] != w2[j]:
#                     if orderInd[w2[j]] < orderInd[w1[j]]:
#                         return False
#                     break
#         return True