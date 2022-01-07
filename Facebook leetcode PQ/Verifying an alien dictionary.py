from typing import List


def isAlienSorted(self, words: List[str], order: str) -> bool:
    orderIdx = {val: i for i, val in enumerate(order)}

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        for j in range(len(w1)):
            if j == len(w2):
                return False
            if w1[j] != w2[j]:
                if orderIdx[w2[j]] < orderIdx[w1[j]]:
                    return False
                break
    return True
