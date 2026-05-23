from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs.sort()
        wordDict = defaultdict(list)

        for word in strs:
            newWord = "".join(sorted(word))
            
            wordDict[newWord].append(word)
        
        return list(wordDict.values())
        