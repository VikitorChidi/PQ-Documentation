from typing import DefaultDict, List
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    result = DefaultDict(list)  # mapping charCount to list of Anagrams

    for s in strs:
        count = [0]*26  # a-z

        # mapping a to idx 0 & z to idx 25
        for i in s:
            count[ord(i) - ord('a')] += 1

        # grouping all anagrams together
        result[tuple(count)].append(s)
    return result.values()
