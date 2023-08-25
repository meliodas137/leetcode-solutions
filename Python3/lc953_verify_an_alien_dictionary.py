class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        pos = {}
        for i in range(len(order)):
            pos[order[i]] = i

        for w in range(len(words)-1):
            curr = 0
            all_l = min(len(words[w]), len(words[w+1]))
            while(curr < all_l and words[w][curr] == words[w+1][curr]):
                curr +=1
            if (curr < all_l and pos[words[w][curr]] > pos[words[w+1][curr]]):
                return False
            if curr == len(words[w+1]) and curr != len(words[w]):
                return False
                
        return True