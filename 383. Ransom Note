from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        r_occurences = Counter(ransomNote)
        m_occurences = Counter(magazine)

        for ch, occ in r_occurences.items():
            if ch not in m_occurences: return False
            if m_occurences[ch] < occ: return False
        
        return True
    





        
